# 🎧 Model Card: HarmonyMatch 1.0

## 1. Model Name

**HarmonyMatch 1.0**

---

## 2. Intended Use

HarmonyMatch 1.0 is designed to recommend songs based on a user's musical preferences using a simple content-based recommendation system. It compares song features such as genre, mood, energy, and acousticness with a user's preferred taste profile. This project is intended for classroom learning and experimentation rather than real-world music streaming.

---

## 3. How the Model Works

The recommender compares each song to the user's preferences and gives it a weighted score. Songs receive bonus points when their genre and mood match the user's favorites. Numeric features such as energy are scored based on how close they are to the user's preferred value, and acousticness is rewarded or penalized depending on whether the user prefers acoustic music. After every song is scored, the system ranks all songs from highest to lowest score and recommends the top results.

---

## 4. Data

The dataset contains 18 songs covering genres such as pop, rock, lofi, indie pop, hip-hop, classical, EDM, folk, R&B, metal, reggae, and country. I expanded the original dataset to include more genres and moods. Although the dataset is more diverse, it is still small and cannot represent every type of musical taste.

---

## 5. Strengths

The recommender performs well when users have clear musical preferences. It successfully recommended pop songs for the High-Energy Pop profile, lofi songs for the Chill Lofi profile, and rock songs for the Deep Intense Rock profile. The explanation feature also helps users understand why each recommendation was selected.

---

## 6. Limitations and Bias

The recommender only considers a small number of song features and ignores lyrics, artist preferences, popularity, release year, and listening history. Because genre has a relatively high weight, the system may repeatedly recommend similar songs instead of introducing more variety. The limited dataset also creates bias because some genres have fewer songs than others.

---

## 7. Evaluation

I tested the recommender using three user profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. Each profile produced recommendations that generally matched the intended musical style. I also experimented by reducing the genre weight and increasing the energy weight. This caused high-energy songs from different genres to rank higher, making recommendations more varied but sometimes less accurate.

---

## 8. Future Work

In the future, I would include additional features such as tempo, danceability, valence, artist preference, and listening history. I would also improve recommendation diversity so users receive a wider range of songs instead of very similar recommendations.

---

## 9. Personal Reflection

This project helped me understand how recommendation systems transform user preferences into ranked suggestions using weighted scoring. As a musician, I found it interesting that a small number of musical features could still produce recommendations that felt realistic. AI tools helped me design the algorithm and debug my implementation, but I still needed to review the suggestions and decide which ideas best fit my project.