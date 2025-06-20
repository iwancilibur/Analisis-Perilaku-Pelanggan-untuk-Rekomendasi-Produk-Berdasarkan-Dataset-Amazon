from flask import Flask, render_template, abort
import analysis_lib as a_lib
import datetime # <-- TAMBAHKAN IMPORT INI

app = Flask(__name__)

# Caching data dan hasil analisis agar tidak dihitung ulang setiap kali refresh
try:
    print("Mulai memuat dan memproses data...")
    # 1. Muat dan bersihkan data
    df = a_lib.load_and_clean_data('amazon.csv')

    # 2. Buat visualisasi
    a_lib.generate_top_categories_plot(df)
    a_lib.generate_rating_distribution_plot(df)

    # 3. Dapatkan rekomendasi
    POPULAR_RECOMMENDATIONS = a_lib.get_popular_recommendations(df, top_n=10)
    print("Data dan analisis siap.")

except FileNotFoundError as e:
    print(f"ERROR: {e}")
    # Jika file tidak ada, kita akan menampilkan error di web
    df = None 
    POPULAR_RECOMMENDATIONS = []


@app.route('/')
def index():
    """
    Route utama untuk menampilkan dashboard.
    """
    # Jika dataset gagal dimuat, tampilkan halaman error
    if df is None:
        abort(500, description="File 'amazon.csv' tidak ditemukan. Pastikan file berada di direktori yang benar.")

    # <-- DAPATKAN TAHUN SAAT INI
    current_year = datetime.datetime.now().year

    # Kirim path gambar dan data rekomendasi ke template
    return render_template(
        'index.html', 
        top_categories_plot='images/top_categories.png',
        rating_dist_plot='images/rating_distribution.png',
        recommendations=POPULAR_RECOMMENDATIONS,
        current_year=current_year # <-- KIRIM TAHUN KE TEMPLATE
    )

# Menambahkan error handler untuk menampilkan pesan yang lebih baik
@app.errorhandler(500)
def internal_error(error):
    return f"<h1>Terjadi Kesalahan Internal</h1><p>{error.description}</p>", 500


if __name__ == '__main__':
    app.run(debug=True)