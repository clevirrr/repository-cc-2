/**
 * Streamify Lite Frontend
 * API dipanggil ke server yang sama (Flask di EC2)
 * Tidak perlu ganti URL — relatif ke origin.
 */

async function loadContents() {
  const genre = document.getElementById("genreFilter").value;
  const listEl = document.getElementById("contentList");
  listEl.innerHTML = "<p>Memuat...</p>";

  try {
    let url = "/api/contents";
    if (genre) url += `?genre=${encodeURIComponent(genre)}`;

    const res = await fetch(url);
    const data = await res.json();

    if (!data.success) {
      listEl.innerHTML = `<div class="error">Error: ${data.error}</div>`;
      return;
    }

    if (data.data.length === 0) {
      listEl.innerHTML = "<p>Tidak ada konten ditemukan.</p>";
      return;
    }

    listEl.innerHTML = data.data.map(item => `
      <div class="item">
        <h3>${item.title}</h3>
        <div class="meta">
          ${item.content_type} • ${item.genre} • ${item.release_year} •
          <span class="rating">★ ${item.avg_rating}</span>
          ${item.is_exclusive === "true" ? " • 🔒 Exclusive" : ""}
        </div>
      </div>
    `).join("");
  } catch (err) {
    listEl.innerHTML = `<div class="error">Gagal mengambil data.<br>${err.message}</div>`;
  }
}

async function getRecommendation() {
  const userId = document.getElementById("userId").value.trim();
  const resultEl = document.getElementById("recommendResult");

  if (!userId) {
    resultEl.innerHTML = `<div class="error">Masukkan User ID terlebih dahulu</div>`;
    return;
  }

  resultEl.innerHTML = "<p>Mencari rekomendasi...</p>";

  try {
    const url = `/api/recommend?user_id=${encodeURIComponent(userId)}`;
    const res = await fetch(url);
    const data = await res.json();

    if (!data.success) {
      resultEl.innerHTML = `<div class="error">Error: ${data.error}</div>`;
      return;
    }

    let html = `
      <div class="success-msg">
        Halo <strong>${data.user_name}</strong> (${data.subscription_plan})!<br>
        Genre favorit: <strong>${data.favorite_genre}</strong>
      </div>
    `;

    if (data.recommendations.length === 0) {
      html += "<p>Belum ada rekomendasi untuk genre ini.</p>";
    } else {
      html += data.recommendations.map(item => `
        <div class="item">
          <h3>${item.title}</h3>
          <div class="meta">
            ${item.content_type} • ${item.genre} •
            <span class="rating">★ ${item.avg_rating}</span>
          </div>
        </div>
      `).join("");
    }

    resultEl.innerHTML = html;
  } catch (err) {
    resultEl.innerHTML = `<div class="error">Gagal mengambil data.<br>${err.message}</div>`;
  }
}

// Load konten saat halaman dibuka
document.addEventListener("DOMContentLoaded", () => {
  loadContents();
});
