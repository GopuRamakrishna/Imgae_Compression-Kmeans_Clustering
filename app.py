import streamlit as st
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import io

# Set page configuration
st.set_page_config(page_title="Image Compression using KMeans", layout="wide")

st.markdown("""
    <h1 style="text-align: center; color: #4CAF50;">Image Compression using KMeans</h1>
    <p style="text-align: center;">Upload an image and compare compression results for up to 3 different K values side-by-side.</p>
""", unsafe_allow_html=True)

# Upload file
uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])
k_values = st.multiselect("🎯 Choose up to 3 K values to compare", [4, 8, 16, 32, 64], default=[8, 16])

if len(k_values) > 3:
    st.warning("⚠️ Please select no more than 3 K values for side-by-side comparison.")
elif uploaded_file is not None and k_values:
    # Load and preprocess image
    img = Image.open(uploaded_file).convert("RGB")
    image = np.array(img) / 255.0
    w, h, d = image.shape
    pixels = image.reshape(-1, 3)

    # Show original image and size
    st.subheader("🖼️ Original Image")
    original_buf = io.BytesIO()
    img.save(original_buf, format="JPEG")
    original_size = original_buf.tell() / 1024

    # Columns for original + compressed images
    col_layout = [1] * (len(k_values) + 1)
    columns = st.columns(col_layout)

    with columns[0]:
        st.image(img, caption="Original")
        st.markdown(f"📦 `{original_size:.2f} KB`")

    # Compressed image blocks
    for idx, k in enumerate(k_values):
        with st.spinner(f"Compressing with K={k}..."):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(pixels)
            compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
            compressed_img = compressed_pixels.reshape(w, h, 3)
            compressed_img_uint8 = (compressed_img * 255).astype(np.uint8)

            # Calculate size of compressed image
            compressed_buf = io.BytesIO()
            Image.fromarray(compressed_img_uint8).save(compressed_buf, format="JPEG")
            compressed_size = compressed_buf.tell() / 1024
            ratio = original_size / compressed_size if compressed_size else 0

            with columns[idx + 1]:
                st.image(compressed_img_uint8, caption=f"K = {k}")
                st.markdown(f"🗜️ `{compressed_size:.2f} KB`  \n🔻 `{ratio:.2f}x`")
                st.download_button(
                    label="📥 Download",
                    data=compressed_buf.getvalue(),
                    file_name=f"compressed_k{k}.jpg",
                    mime="image/jpeg",
                    key=f"download_{k}"
                )

    st.success("✅ Comparison ready!")
