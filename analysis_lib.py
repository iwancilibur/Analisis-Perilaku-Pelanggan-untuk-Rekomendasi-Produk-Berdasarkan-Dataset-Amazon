import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Menonaktifkan peringatan UserWarning dari Matplotlib di lingkungan non-GUI
import matplotlib
matplotlib.use('Agg')

def load_and_clean_data(filepath='amazon.csv'):
    """
    Memuat dataset, membersihkan kolom yang diperlukan, dan mengembalikan DataFrame yang bersih.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset tidak ditemukan di path: {filepath}")

    df = pd.read_csv(filepath)

    # 1. Membersihkan kolom harga dan mengubahnya menjadi numerik
    df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)
    df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)

    # 2. Membersihkan rating dan rating_count
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce') # Mengubah nilai non-numerik menjadi NaT
    df['rating_count'] = df['rating_count'].str.replace(',', '').astype(float)

    # 3. Menghapus baris dengan nilai rating atau rating_count yang kosong
    df.dropna(subset=['rating', 'rating_count', 'user_id'], inplace=True)
    
    # 4. Memisahkan kategori utama
    df['main_category'] = df['category'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')

    print("Pembersihan data selesai.")
    return df

def generate_top_categories_plot(df, save_path='static/images/top_categories.png'):
    """
    Membuat visualisasi bar plot untuk top 10 kategori utama dan menyimpannya.
    """
    plt.figure(figsize=(12, 8))
    top_categories = df['main_category'].value_counts().head(10)
    sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
    plt.title('Top 10 Kategori Produk Paling Populer', fontsize=16)
    plt.xlabel('Jumlah Produk', fontsize=12)
    plt.ylabel('Kategori', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    # Pastikan direktori ada
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, bbox_inches='tight')
    plt.close() # Menutup plot agar tidak ditampilkan di konsol
    print(f"Plot kategori disimpan di: {save_path}")

def generate_rating_distribution_plot(df, save_path='static/images/rating_distribution.png'):
    """
    Membuat visualisasi histogram untuk distribusi rating produk dan menyimpannya.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rating'], bins=20, kde=True, color='skyblue')
    plt.title('Distribusi Rating Produk', fontsize=16)
    plt.xlabel('Rating (1-5)', fontsize=12)
    plt.ylabel('Frekuensi', fontsize=12)
    
    # Pastikan direktori ada
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()
    print(f"Plot distribusi rating disimpan di: {save_path}")

def get_popular_recommendations(df, top_n=10, min_rating_count=100):
    """
    Memberikan rekomendasi produk berdasarkan popularitas (rating tinggi dan jumlah ulasan banyak).
    """
    # Filter produk dengan jumlah rating yang signifikan
    popular_df = df[df['rating_count'] >= min_rating_count].copy()
    
    # Urutkan berdasarkan rating (turun) dan jumlah rating (turun)
    recommended_products = popular_df.sort_values(by=['rating', 'rating_count'], ascending=[False, False])
    
    # Ambil top_n produk dan kolom yang relevan
    top_products = recommended_products.head(top_n)
    
    # Format hasil menjadi list of dictionaries
    recommendations = top_products[[
        'product_name', 'main_category', 'rating', 'rating_count', 'discounted_price', 'product_link'
    ]].to_dict('records')
    
    print(f"Berhasil menghasilkan {len(recommendations)} rekomendasi populer.")
    return recommendations