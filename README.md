# Analisis Perilaku Pelanggan & Rekomendasi Produk Amazon

Ini adalah proyek untuk mata kuliah **Big Data dan Visualisasi**, yang bertujuan untuk menganalisis dataset penjualan Amazon, mengidentifikasi pola perilaku pelanggan, dan membangun aplikasi web interaktif untuk menampilkan wawasan dan rekomendasi produk.

## 📜 Deskripsi Proyek

Proyek ini melakukan analisis data eksploratif (EDA) pada dataset penjualan dan ulasan produk Amazon untuk mengungkap wawasan bisnis. Tujuannya adalah untuk memahami produk dan kategori mana yang paling populer, bagaimana distribusi rating pelanggan, dan berdasarkan temuan tersebut, membangun sistem rekomendasi sederhana. Seluruh hasil disajikan dalam sebuah *dashboard* web yang dibangun menggunakan Flask.

## ✨ Fitur Utama

  - **Pembersihan & Pra-pemrosesan Data**: Membersihkan data mentah dari dataset `amazon.csv` agar siap untuk dianalisis.
  - **Analisis Data Eksploratif (EDA)**: Mengidentifikasi tren dan pola utama dari data.
  - **Visualisasi Data**: Menampilkan wawasan dalam bentuk grafik yang mudah dipahami (Top 10 Kategori, Distribusi Rating) menggunakan Matplotlib & Seaborn.
  - **Sistem Rekomendasi**: Implementasi sistem rekomendasi sederhana berbasis popularitas (rating tertinggi & jumlah ulasan terbanyak).
  - **Dashboard Web Interaktif**: Aplikasi web yang dibangun dengan Flask untuk menyajikan hasil analisis dan rekomendasi secara dinamis.

## 📸 Tampilan Aplikasi

Berikut adalah tampilan dari *dashboard* aplikasi web yang telah selesai.
![Image](https://github.com/user-attachments/assets/7aaf5c5a-9bea-4468-ad0b-6cb035bab067)

*Dashboard menampilkan dua plot visualisasi utama di bagian atas dan tabel rekomendasi produk di bagian bawah.*

## 🛠️ Teknologi yang Digunakan

  - **Backend**: Python 3, Flask
  - **Analisis Data**: Pandas
  - **Visualisasi Data**: Matplotlib, Seaborn
  - **Frontend**: HTML5, CSS3

## 📁 Struktur Proyek

```
/proyek_bigdata/
├── app.py                  # File utama aplikasi Flask
├── analysis_lib.py         # Modul untuk analisis & rekomendasi
├── amazon.csv              # Dataset (perlu diunduh terpisah)
├── README.md               # File ini
├── requirements.txt        # Daftar dependensi Python
├── templates/
│   └── index.html          # Template HTML untuk frontend
└── static/
    ├── css/
    │   └── style.css       # File styling
    └── images/
        └── (Folder ini akan diisi oleh plot yang dihasilkan)
```

## ⚙️ Instalasi dan Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini secara lokal.

### 1\. Prasyarat

  - Python 3.7 atau lebih tinggi
  - `pip` dan `venv`

### 2\. Clone Repositori

```bash
git clone https://github.com/iwancilibur/Analisis-Perilaku-Pelanggan-untuk-Rekomendasi-Produk-Berdasarkan-Dataset-Amazon.git
cd Analisis-Perilaku-Pelanggan-untuk-Rekomendasi-Produk-Berdasarkan-Dataset-Amazon
```

### 3\. Buat Lingkungan Virtual (Virtual Environment)

Sangat disarankan untuk menggunakan lingkungan virtual agar tidak mengganggu instalasi Python global Anda.

  - **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
  - **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 4\. Instal Dependensi

Buat file `requirements.txt` dengan isi berikut:

```txt
pandas
matplotlib
seaborn
scikit-learn
flask
wordcloud
```

Kemudian instal semua library yang dibutuhkan dengan satu perintah:

```bash
pip install -r requirements.txt
```

### 5\. Unduh Dataset

  - Unduh dataset dari **[Kaggle: Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)**.
  - Ubah nama filenya menjadi `amazon.csv` (jika berbeda).
  - Letakkan file `amazon.csv` di direktori utama proyek (sejajar dengan `app.py`).

### 6\. Jalankan Aplikasi

Setelah semua langkah di atas selesai, jalankan aplikasi Flask:

```bash
python app.py
```

Aplikasi akan berjalan dan Anda akan melihat output di terminal seperti ini:

```
 * Running on http://127.0.0.1:5000
```

Buka URL `http://127.0.0.1:5000` di browser Anda untuk melihat hasilnya.

## 👥 Kontributor

Proyek ini disusun oleh:

  - [Nama Anggota 1]
  - [Nama Anggota 2]
  - [Nama Anggota 3]
  - [dst.]

## 📄 Lisensi

Proyek ini Open Source Silahkan anda Kembangkan sesuai  dengan keinginan anda
