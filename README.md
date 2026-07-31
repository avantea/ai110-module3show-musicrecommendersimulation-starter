# 🎵 Music Recommender Simulation

## Project Summary

HarmonyMatch 1.0 is a content-based music recommender that compares song attributes with a user's taste profile. It uses weighted scoring based on genre, mood, energy, and acoustic preference to recommend songs that best match the user's preferences. The goal of this project is to demonstrate how recommendation systems transform user preferences into ranked suggestions.

---

## How The System Works

Music recommendation systems predict what users may like by comparing user behavior and song information. Collaborative filtering uses patterns from other users, such as likes, skips, playlists, and listening history. Content-based filtering uses song attributes, such as genre, mood, energy, and tempo, to recommend songs similar to what a user already enjoys.

My recommender focuses on content-based filtering by comparing song features to a user's taste profile and ranking songs with the best match. As a musician, I know that a song's overall vibe comes from a combination of factors like genre, mood, energy, and tempo rather than just one feature, so I chose to prioritize those characteristics in my recommendation system.

### Song Features

The recommender stores and compares the following song features:

- Genre
- Mood
- Energy
- Tempo (stored but not currently used for scoring)
- Valence (stored for future improvements)
- Danceability (stored for future improvements)
- Acousticness

### User Profile

Each user profile stores:

- Favorite genre
- Favorite mood
- Target energy level
- Whether the user prefers acoustic music

### Algorithm Recipe

My recommender uses a weighted scoring system.

- Genre match = +3 points
- Mood match = +2 points
- Energy is scored based on how close the song's energy is to the user's preferred energy using the formula `1 - absolute difference`.
- Acousticness is rewarded or penalized depending on whether the user prefers acoustic music.

After every song receives a score, the songs are sorted from highest score to lowest score, and the top recommendations are returned.

---

## Getting Started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the Program

```bash
python -m src.main
```

### Run the Tests

```bash
pytest
```

---

## Sample Recommendation Output

```text
Top recommendations:

Sunrise City - Score: 7.66
Because: genre matches (pop), mood matches (happy), energy is close to the target, and it is not very acoustic.

Gym Hero - Score: 5.89
Because: genre matches (pop), energy is close to the target, and it is not very acoustic.
```

---

## Experiments

I tested three different user profiles:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock

Each profile produced different recommendations that matched the user's preferences.

I also experimented with reducing the genre weight from **3.0** to **1.5** while increasing the energy weight from **2.0** to **4.0**. This caused high-energy songs from different genres to move higher in the rankings. The recommendations became more varied, but genre became less important. After the experiment, I restored the original scoring weights.

---

## Limitations and Risks

HarmonyMatch works on a small dataset of only 18 songs, so some genres and moods have limited representation. The recommender does not consider lyrics, artist popularity, listening history, or user behavior. Because genre has a relatively high weight, the recommender can create a filter bubble by repeatedly recommending songs that are very similar to the user's existing preferences.

---

## Reflection

This project helped me understand how recommendation systems convert user preferences into ranked recommendations using weighted scoring. I also learned that even simple algorithms can feel personalized when they use meaningful song features.

As a musician, I found it interesting that only a few musical characteristics could produce recommendations that felt reasonable. At the same time, I realized that real recommendation systems are much more complex and must balance personalization, diversity, and fairness.