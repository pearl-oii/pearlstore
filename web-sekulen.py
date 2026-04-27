import streamlit as st
import pandas as pd

# Set judul halaman
st.set_page_config(page_title="Pearl's Sukulen Store", layout="centered")

# --- BANNER GAMBAR DARI CANVA ---
# Ganti 'banner.png' dengan nama file banner kamu di GitHub
try:
    st.image("banner.jpg", use_container_width=True)
except:
    st.write("*(Banner belum terload, pastikan nama filenya benar)*")

# --- JUDUL TEKS ---
st.title("🌵 Pearl's Sukulen Store")
st.write("Selamat datang! Temukan koleksi sukulen terbaik untuk mempercantik ruangan Anda.")

# ... (sisa kodingan lainnya tetap sama)

st.divider()

# --- MEMBACA DATA ---
try:
    # Pastikan file CSV kamu namanya tetap Buku1.csv di GitHub
    df = pd.read_csv("Buku1.csv")
    
    # --- LOOPING PRODUK ---
    for index, row in df.iterrows():
        # Menampilkan Nama Produk
        st.subheader(row['nama'])
        
        # Menampilkan Gambar
        st.image(row['gambar'], use_container_width=True)
        
        # Menampilkan Harga dengan /pcs
        harga_format = f"{row['harga']:,}".replace(',', '.')
        st.write(f"### Rp {harga_format}/pcs")
        
        # Menampilkan Stok
        st.write(f"Stok: {row['stok']}")
        
        # --- DETAIL UKURAN ---
        with st.expander("Lihat Detail Ukuran"):
            nama_produk = row['nama'].lower()
            if "mini" in nama_produk:
                st.write("📏 **Diameter pot:** 5 cm")
            elif "medium" in nama_produk:
                st.write("📏 **Diameter pot:** 10 cm")
            elif "mix" in nama_produk:
                st.write("📏 **Diameter pot:** 15 cm")
                st.write("📦 **Isi:** 2 Sukulen Medium + 3 Sukulen Mini")
        
        # Tombol Pesan per Produk
        st.link_button(f"Pesan {row['nama']}", f"https://wa.me/628123456789?text=Halo%20Pearl's%20Sukulen,%20saya%20mau%20pesan%20{row['nama']}")
        
        st.divider()

except Exception as e:
    st.error(f"Gagal memuat data produk: {e}")

# --- BAGIAN BAWAH (FOOTER) ---
st.markdown("### 📞 Hubungi Kami")
st.write("Klik tombol di bawah untuk tanya-tanya atau pemesanan:")
st.link_button("📲 Chat via WhatsApp", "https://wa.me/6281325390391")

st.caption("© 2026 Pearl's Sukulen Store - Mutiara")