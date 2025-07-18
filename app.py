# ========================================
# 🌐 Streamlit Web App: Tabel Periodik 2D
# ========================================

# 📦 Import library
import streamlit as st
import json
import os
from PIL import Image

# ⚙️ Konfigurasi halaman
st.set_page_config(page_title="Tabel Periodik", layout="wide")
st.title("🧪 Tabel Periodik Interaktif dengan Gambar 2D")

# 📥 Load data JSON
with open("elements.json") as f:
    elements = json.load(f)

# 🧠 Buat dictionary dari simbol → data unsur
element_dict = {el['symbol']: el for el in elements}

# 🎨 Warna berdasarkan kategori
category_colors = {
    "nonmetal": "lightblue",
    "noble gas": "lightgreen",
    "alkali metal": "lightcoral",
    "alkaline earth metal": "orange",
    "metalloid": "khaki",
    "halogen": "violet",
    "post-transition metal": "silver",
    "transition metal": "lightsalmon",
    "lanthanide": "plum",
    "actinide": "lightpink"
}

# 🧾 Fungsi tampilkan detail unsur
def show_element_details(el):
    st.markdown(f"## {el['name']} ({el['symbol']})")
    cols = st.columns([1, 2])
    with cols[0]:
        img_path = f"images/{el['symbol']}.png"
        if os.path.exists(img_path):
            st.image(img_path, width=150)
        else:
            st.warning("Gambar tidak tersedia.")
    with cols[1]:
        st.markdown(f"**Nomor Atom:** {el['number']}")
        st.markdown(f"**Massa Atom:** {el['atomic_mass']}")
        st.markdown(f"**Kategori:** {el['category']}")

# 📊 Tampilkan tombol grid tabel periodik
cols = st.columns(18)
for idx, el in enumerate(elements):
    col = cols[idx % 18]
    color = category_colors.get(el['category'], "lightgray")
    if col.button(el['symbol']):
        show_element_details(el)
    col.markdown(f"<div style='text-align:center;background-color:{color};padding:4px;border-radius:4px'>{el['symbol']}</div>", unsafe_allow_html=True)

# 📌 Petunjuk
with st.expander("ℹ️ Petunjuk"):
    st.markdown("""
    - Klik simbol unsur untuk melihat detail dan gambar 2D-nya.
    - Tambahkan gambar di folder `images/` dengan nama file sesuai simbol (misal: `C.png`, `O.png`, dll).
    - Data unsur diambil dari file `elements.json`.
    - Bisa di-deploy ke [Streamlit Cloud](https://share.streamlit.io).
    """)
