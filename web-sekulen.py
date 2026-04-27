import streamlit as st
import pandas as pd

# Set judul halaman
st.set_page_config(page_title="Pearl's Sukulen Store", layout="centered")

# --- 1. TULISAN DI ATAS BANNER (Sesuai Permintaan) ---
st.markdown("<h1 style='text-align: center;'>🌵 Welcome to</h1>", unsafe_allow_html=True)

# --- 2. BANNER GAMBAR ---
try:
    st.image("banner.jpg", use_container_width=True)
except:
    pass

st.divider()

# --- 3. INFORMASI PENGIRIMAN ---
with st.expander("🚚 Informasi Pengiriman", expanded=True):
    st.write("- ✅ Bisa kirim seluruh Indonesia\n- ✅ Sudah termasuk pot\n- ✅ Tanaman sehat & akar jalan\n- ✅ Packing aman\n- ⚠️ Harga belum termasuk ongkir")

st.divider()

# --- 4. BACA DATA PRODUK ---
try:
    df = pd.read_csv("Buku1.csv", sep=None, engine='python')
    df.columns = [c.strip().lower() for c in df.columns]

    for index, row in df.iterrows():
        # --- LOGIKA EMOJI SAMPING NAMA PRODUK ---
        nama_asli = row['nama']
        nama_kecil = str(nama_asli).lower()
        
        if "mini" in nama_kecil:
            nama_display = f"🪴 {nama_asli}"
        elif "medium" in nama_kecil:
            nama_display = f"🌿 {nama_asli}"
        elif "mix" in nama_kecil:
            nama_display = f"🌵 {nama_asli}"
        else:
            nama_display = f"✨ {nama_asli}"

        # Tampilkan Nama dengan Emoji
        st.subheader(nama_display)
        
        # Tampilkan Gambar
        try:
            kolom_img = 'foto' if 'foto' in df.columns else 'gambar'
            st.image(row[kolom_img], use_container_width=True)
        except:
            st.write("*(Gambar sedang disiapkan)*")
        
        # Harga & Stok
        try:
            harga_angka = int(str(row['harga']).replace('.','').replace(',',''))
            harga_format = f"{harga_angka:,}".replace(',', '.')
            st.write(f"### Rp {harga_format}/pcs")
        except:
            st.write(f"### Rp {row['harga']}/pcs")
            
        st.write(f"Stok: {row['stok']}")
        
        # Detail Ukuran
        with st.expander("Lihat Detail Ukuran"):
            if "mini" in nama_kecil:
                st.write("📏 **Diameter pot:** 5 cm")
            elif "medium" in nama_kecil:
                st.write("📏 **Diameter pot:** 10 cm")
            elif "mix" in nama_kecil:
                st.write("📏 **Diameter pot:** 15 cm (Pot Besar)")
                st.write("📦 **Isi Paket:** 2 Medium + 3 Mini")
            
        # Tombol WA
        st.link_button(f"Pesan {nama_asli}", f"https://wa.me/6281325390391?text=Halo%20Mutiara,%20saya%20mau%20pesan%20{nama_asli}")
        st.divider()

except Exception as e:
    st.error(f"Data belum muncul: {e}")

# --- 5. FOOTER ---
st.markdown("### 📞 Hubungi Kami")
st.link_button("📲 Chat via WhatsApp", "https://wa.me/6281325390391")
st.caption("© 2026 Pearl's Sukulen Store - Mutiara Atha")