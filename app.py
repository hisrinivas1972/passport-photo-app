import streamlit as st
from PIL import Image
from rembg import remove
import io

# Passport sizes in inches (converted to pixels at 300 DPI)
passport_sizes_in = {
    "USA": (2, 2),
    "UK": (1.77, 1.37),
    "Canada": (2, 2.75),
    "Australia": (1.97, 1.57),
    "India": (2, 2)
}

DPI = 300  # Standard printing resolution

def generate_passport_photo(image_bytes, country):
    width_px = int(passport_sizes_in[country][0] * DPI)
    height_px = int(passport_sizes_in[country][1] * DPI)
    target_size = (width_px, height_px)

    img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    subject = remove(img)

    # Resize subject proportionally to fit
    subject.thumbnail(target_size, Image.Resampling.LANCZOS)

    background = Image.new("RGBA", target_size, (255, 255, 255, 255))
    x = (target_size[0] - subject.size[0]) // 2
    y = (target_size[1] - subject.size[1]) // 2
    background.paste(subject, (x, y), subject)

    final = background.convert("RGB")
    return img.convert("RGB"), final, target_size  # return original, final, and size

# --- Streamlit Interface ---
st.set_page_config(page_title="Passport Photo Generator", layout="centered")
st.title("🛂 Passport Photo Generator")
st.markdown("Upload a photo to remove its background and convert it to passport photo size for different countries.")

uploaded_file = st.file_uploader("📤 Upload your photo", type=["jpg", "jpeg", "png"])
country = st.selectbox("🌍 Select passport size:", list(passport_sizes_in.keys()))

if uploaded_file and country:
    image_bytes = uploaded_file.read()

    with st.spinner("🧠 Processing your photo..."):
        original_img, passport_img, final_size = generate_passport_photo(image_bytes, country)

    # Layout columns for side-by-side view
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original Photo")
        st.image(original_img, use_container_width=True)
        st.text(f"Size: {original_img.size[0]} x {original_img.size[1]} px")

    with col2:
        st.subheader("✅ Passport Photo")
        st.image(passport_img, use_container_width=True)
        st.text(f"Size: {final_size[0]} x {final_size[1]} px")

    # Download
    buf = io.BytesIO()
    passport_img.save(buf, format="JPEG", dpi=(DPI, DPI))
    st.download_button(
        label="📥 Download Passport Photo",
        data=buf.getvalue(),
        file_name=f"passport_photo_{country}.jpg",
        mime="image/jpeg"
    )
else:
    st.info("Please upload an image and select a country.")
