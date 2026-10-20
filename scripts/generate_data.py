#!/usr/bin/env python3
"""
Generate sample dataset untuk Streamify Lite.
Jalankan: python3 generate_data.py
Hasil: file CSV di folder ../data/
"""

import csv
import random
import os

os.makedirs("../data", exist_ok=True)

# --- User Profiles ---
users = []
plans = ["Basic", "Standard", "Premium"]
segments = ["Casual", "Regular", "Power User"]
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]

for i in range(1, 51):
    users.append({
        "user_id": f"U{i:03d}",
        "name": f"User {i}",
        "subscription_plan": random.choice(plans),
        "favorite_genre": random.choice(genres),
        "total_streams": random.randint(5, 200),
        "customer_segment": random.choice(segments),
    })

with open("../data/user_profiles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)

# --- Content Catalog ---
titles = [
    ("The Last Horizon", "Sci-Fi"),
    ("Laugh Out Loud", "Comedy"),
    ("Midnight Shadow", "Horror"),
    ("Love in Paris", "Romance"),
    ("Iron Fist", "Action"),
    ("Broken Hearts", "Drama"),
    ("Galaxy Warriors", "Sci-Fi"),
    ("Funny Bones", "Comedy"),
    ("Dark Forest", "Horror"),
    ("Summer Romance", "Romance"),
    ("Street Fighter", "Action"),
    ("Silent Tears", "Drama"),
    ("Neon Future", "Sci-Fi"),
    ("Joke Master", "Comedy"),
    ("Haunted House", "Horror"),
    ("First Kiss", "Romance"),
    ("Speed Racer", "Action"),
    ("Family Ties", "Drama"),
    ("Alien Invasion", "Sci-Fi"),
    ("Stand Up Night", "Comedy"),
]

contents = []
for i, (title, genre) in enumerate(titles, 1):
    contents.append({
        "content_id": f"C{i:03d}",
        "title": title,
        "content_type": random.choice(["Movie", "Series"]),
        "genre": genre,
        "avg_rating": round(random.uniform(3.0, 5.0), 1),
        "release_year": random.randint(2015, 2025),
        "duration_minutes": random.randint(90, 150) if random.random() > 0.3 else random.randint(20, 50),
        "is_exclusive": random.choice(["true", "false"]),
    })

with open("../data/content_catalog.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=contents[0].keys())
    writer.writeheader()
    writer.writerows(contents)

# --- User Interactions ---
interactions = []
interaction_types = ["play", "complete", "like", "skip"]

for i in range(1, 201):
    interactions.append({
        "interaction_id": f"I{i:04d}",
        "user_id": f"U{random.randint(1, 50):03d}",
        "content_id": f"C{random.randint(1, 20):03d}",
        "interaction_type": random.choice(interaction_types),
        "watch_duration_seconds": random.randint(60, 7200),
        "timestamp": f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
    })

with open("../data/user_interactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=interactions[0].keys())
    writer.writeheader()
    writer.writerows(interactions)

print("✅ Dataset berhasil dibuat di folder data/")
print("   - user_profiles.csv (50 users)")
print("   - content_catalog.csv (20 contents)")
print("   - user_interactions.csv (200 interactions)")
