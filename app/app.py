"""
Streamify Lite - Simple Web Application
Berjalan di EC2. Membaca data dari file CSV.
Tidak memakai Lambda / DynamoDB / API Gateway.
"""

import csv
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Path ke folder data (relatif terhadap lokasi app.py)
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_csv(filename):
    """Baca file CSV dan kembalikan list of dict."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@app.route("/")
def index():
    """Halaman utama frontend."""
    return render_template("index.html")


@app.route("/api/contents")
def list_contents():
    """
    GET /api/contents
    GET /api/contents?genre=Action
    Mengembalikan daftar konten (bisa difilter genre).
    """
    genre = request.args.get("genre", "").strip()
    contents = load_csv("content_catalog.csv")

    if genre:
        contents = [c for c in contents if c.get("genre", "").lower() == genre.lower()]

    # Urutkan rating tertinggi
    contents = sorted(contents, key=lambda x: float(x.get("avg_rating", 0)), reverse=True)

    return jsonify({
        "success": True,
        "count": len(contents),
        "data": contents
    })


@app.route("/api/recommend")
def recommend():
    """
    GET /api/recommend?user_id=U001
    Rekomendasi sederhana berdasarkan favorite_genre user.
    """
    user_id = request.args.get("user_id", "").strip()

    if not user_id:
        return jsonify({
            "success": False,
            "error": "Parameter user_id wajib diisi. Contoh: /api/recommend?user_id=U001"
        }), 400

    users = load_csv("user_profiles.csv")
    user = next((u for u in users if u.get("user_id") == user_id), None)

    if not user:
        return jsonify({
            "success": False,
            "error": f"User {user_id} tidak ditemukan"
        }), 404

    favorite_genre = user.get("favorite_genre", "Action")
    contents = load_csv("content_catalog.csv")

    # Filter genre yang sama, ambil top 5 rating tertinggi
    recommendations = [
        c for c in contents
        if c.get("genre", "").lower() == favorite_genre.lower()
    ]
    recommendations = sorted(
        recommendations,
        key=lambda x: float(x.get("avg_rating", 0)),
        reverse=True
    )[:5]

    return jsonify({
        "success": True,
        "user_id": user_id,
        "user_name": user.get("name"),
        "favorite_genre": favorite_genre,
        "subscription_plan": user.get("subscription_plan"),
        "recommendations": recommendations,
        "message": f"Rekomendasi berdasarkan genre favorit: {favorite_genre}"
    })


@app.route("/api/users")
def list_users():
    """GET /api/users — daftar semua user (untuk debugging)."""
    users = load_csv("user_profiles.csv")
    return jsonify({
        "success": True,
        "count": len(users),
        "data": users
    })


if __name__ == "__main__":
    # host=0.0.0.0 agar bisa diakses dari luar EC2
    # port=5000
    print("=" * 50)
    print("  Streamify Lite berjalan di http://0.0.0.0:5000")
    print("  Buka browser: http://[EC2-PUBLIC-IP]:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=False)
