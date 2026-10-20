# Streamify Lite - Starter Code (Pemula)

Starter code untuk **Soal Latihan AWS Cloud Computing untuk Pemula**.

## Struktur Folder

```
streamify-lite/
├── app/                   # Aplikasi web (Python Flask)
│   ├── app.py             # Backend + API
│   ├── templates/
│   │   └── index.html     # Halaman frontend
│   └── static/
│       ├── style.css
│       └── app.js
├── data/                  # Sample dataset (CSV)
├── scripts/
│   └── generate_data.py   # Script generate sample data
├── requirements.txt
└── README.md
```

## Cara Pakai di EC2

1. Extract ZIP ini di EC2.
2. Install dependency:
   ```bash
   sudo yum install python3-pip -y   # Amazon Linux
   # atau: sudo apt install python3-pip -y   # Ubuntu
   pip3 install -r requirements.txt
   ```
3. (Opsional) Download data dari S3:
   ```bash
   aws s3 cp s3://NAMA-BUCKET-KAMU/raw-data/ ./data/ --recursive
   ```
4. Jalankan aplikasi:
   ```bash
   cd app
   python3 app.py
   ```
5. Buka browser: `http://[EC2-PUBLIC-IP]:5000`

## Catatan

- Tidak memakai Lambda, DynamoDB, API Gateway, CloudWatch, atau SNS.
- Semua berjalan di satu EC2 instance.
- Data dibaca dari file CSV di folder `data/`.
