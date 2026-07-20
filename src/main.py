"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Three example user profiles to test the recommender.
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "likes_acoustic": False,
        },
    }

    # Show the top 5 recommendations for each profile.
    for name, user_prefs in profiles.items():
        print(f"\n=== {name} ===\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} - Score: {score:.2f}")
            print(f"   Because: {explanation}\n")


if __name__ == "__main__":
    main()
