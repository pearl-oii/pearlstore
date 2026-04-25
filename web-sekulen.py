import streamlit as st
import pandas as pd
import os

# --- 1. PENGATURAN HALAMAN ---
st.set_page_config(page_title="Pearl's Sukulen Store", layout="wide")

# --- 2. BAGIAN HEADER (JUDUL & BANNER) ---
st.title("🌵 Pearl's Sukulen Store")

# Cek apakah ada file banner.jpg atau banner.png di folder
if os.path.exists("banner.jpg"):
    st.image("banner.jpg", use_container_width=True)
elif os.path.exists("banner.png"):
    st.image("banner.png", use_container_width=True)
else:
    st.info("Tips: Masukkan file 'banner.jpg' ke folder website biar makin cantik!")

# Kotak Informasi Pengiriman (Biar mirip punya temanmu)
st.success("""
📍 **Informasi Pengiriman:**
* Tanaman sehat, akar jalan, packing aman dengan kardus tebal.
* Bisa kirim ke seluruh Indonesia.
""")

# --- 3. LOAD DATA DARI CSV ---
try:
    # Membaca CSV dengan deteksi otomatis pemisah
    df = pd.read_csv('Buku1.csv', sep=None, engine='python')
    
    # Bersihkan nama kolom (kecilkan semua & hapus spasi)
    df.columns = df.columns.str.strip().str.lower()

    if 'kategori' in df.columns:
        df['kategori'] = df['kategori'].fillna('Lainnya')
        kategori_list = df['kategori'].unique()

        # Looping per Kategori
        for kat in kategori_list:
            st.header(f"Kategori: {kat}")
            data_per_kat = df[df['kategori'] == kat]

            # Membuat kolom (max 4 produk per baris)
            cols = st.columns(4)
            for index, row in data_per_kat.reset_index().iterrows():
                with cols[index % 4]:
                    # --- LOGIKA PENCARIAN FOTO ---
                    nama_foto_csv = str(row['foto']).strip().split('.')[0]
                    foto_final = None
                    
                    # Cari file yang namanya mirip di folder
                    for file_dalam_folder in os.listdir():
                        if file_dalam_folder.lower().startswith(nama_foto_csv.lower()):
                            foto_final = file_dalam_folder
                            break
                    
                    if foto_final:
                        st.image(foto_final, use_container_width=True)
                    else:
                        st.warning(f"Foto '{nama_foto_csv}' tidak ketemu")
                    
                    # Info Produk
                    st.subheader(row['nama'])
                    st.write(f"### **Rp {row['harga']:,}**")
                    st.write(f"Stok: {row['stok']}")
                    
                    # Tombol Pesan
                    if st.button(f"Pesan {row['nama']}", key=f"btn_{index}_{kat}"):
                        st.balloons() # Efek balon biar seru!
                        st.success(f"Berhasil masuk keranjang!")
            st.divider()
    else:
        st.error("Kolom 'kategori' tidak ditemukan di CSV!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

# --- 4. SIDEBAR ---
st.sidebar.header("Hubungi Penjual")
st.sidebar.link_button("💬 Chat di WhatsApp", "https://wa.me/6281325390391")