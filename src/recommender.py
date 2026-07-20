import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

# --- Scoring weights (tweak these to change how the recommender behaves) ---
GENRE_WEIGHT = 3.0
MOOD_WEIGHT = 2.0
ENERGY_WEIGHT = 2.0
ACOUSTIC_WEIGHT = 1.0

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Score a single Song against the user's taste. Higher is better."""
        score = 0.0

        # Category features: award points for an exact match.
        if song.genre == user.favorite_genre:
            score += GENRE_WEIGHT
        if song.mood == user.favorite_mood:
            score += MOOD_WEIGHT

        # Numeric feature: reward energy that is close to the target.
        # "1 - absolute difference" gives 1.0 for a perfect match, less as the gap grows.
        energy_closeness = 1 - abs(song.energy - user.target_energy)
        score += energy_closeness * ENERGY_WEIGHT

        # Acoustic preference: reward high acousticness if the user likes acoustic,
        # otherwise reward low acousticness.
        if user.likes_acoustic:
            score += song.acousticness * ACOUSTIC_WEIGHT
        else:
            score += (1 - song.acousticness) * ACOUSTIC_WEIGHT

        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Score every song, then sort from highest score to lowest.
        scored = [(song, self._score(user, song)) for song in self.songs]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        # Return just the top k Song objects.
        return [song for song, score in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append(f"it is a {song.genre} song (your favorite genre)")
        if song.mood == user.favorite_mood:
            reasons.append(f"its mood is {song.mood} (a mood you like)")

        energy_gap = abs(song.energy - user.target_energy)
        if energy_gap <= 0.2:
            reasons.append(
                f"its energy ({song.energy}) is close to your target ({user.target_energy})"
            )

        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("it is fairly acoustic, which you enjoy")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("it is not very acoustic, matching your taste")

        if not reasons:
            return f"'{song.title}' is an okay overall match for your taste."
        return f"'{song.title}' is recommended because " + ", and ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py

    Returns a list of dictionaries, one per song, with the numeric
    fields converted from text into int/float.
    """
    # These columns are numbers in the CSV but load as text, so we convert them.
    float_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song (a dict) against user preferences (a dict).
    Required by recommend_songs() and src/main.py

    user_prefs keys: "genre", "mood", "energy", and optional "likes_acoustic".
    Returns: (score, reasons)
    """
    score = 0.0
    reasons: List[str] = []

    # Category features: award points for an exact match.
    if song["genre"] == user_prefs.get("genre"):
        score += GENRE_WEIGHT
        reasons.append(f"genre matches ({song['genre']})")
    if song["mood"] == user_prefs.get("mood"):
        score += MOOD_WEIGHT
        reasons.append(f"mood matches ({song['mood']})")

    # Numeric feature: reward energy that is close to the target.
    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_closeness = 1 - abs(song["energy"] - target_energy)
        score += energy_closeness * ENERGY_WEIGHT
        if abs(song["energy"] - target_energy) <= 0.2:
            reasons.append(f"energy ({song['energy']}) is close to your target")

    # Acoustic preference (defaults to False if the caller did not set it).
    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if likes_acoustic:
        score += song["acousticness"] * ACOUSTIC_WEIGHT
        if song["acousticness"] >= 0.5:
            reasons.append("it is fairly acoustic, which you enjoy")
    else:
        score += (1 - song["acousticness"]) * ACOUSTIC_WEIGHT
        if song["acousticness"] < 0.5:
            reasons.append("it is not very acoustic, matching your taste")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py

    Scores all songs, sorts them highest to lowest, and returns the top k.
    Each returned item is: (song_dict, score, explanation)
    """
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", and ".join(reasons) if reasons else "it is an okay overall match"
        scored.append((song, score, explanation))

    # Sort by the score (the second item in each tuple), highest first.
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
