import streamlit as st
from PIL import Image
from rembg import remove
import io

# Passport sizes in inches (width, height)
passport_sizes_in = {
    "USA": (2, 2),
    "UK": (1.77, 1.37),
    "Canada": (2, 2.75),
    "Australia": (1.97, 1.57),
    "India": (2, 2)
}

DPI = 300

def remove_bg_and_create_passport_photo(image_bytes, country):
    width_px = int(passport_sizes_in[country][0] * DPI)
    height_px = int(passport_sizes_in[country][1] * DPI)
    target_size = (width_px, height_px)
    
    img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    output = remove(img)
    output.thumbnail(target_size, Image.Resampling.LANCZOS)
    
    background = Image.new("RGBA", target_size, (255, 255, 255, 255))
    x = (target_size[0] - output.size[0]) // 2
    y = (target_size[1] - output.size[1]) // 2
    background.paste(output, (x, y), output)
    
    final = background.convert("RGB")
    return final

st.title("Passport Photo Generator with Background Removal")

uploaded_file = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])

country = st.selectbox("Select country size", list(passport_sizes_in.keys()))

if uploaded_file and country:
    image_bytes = uploaded_file.read()
    with st.spinner("Processing image..."):
        result_img = remove_bg_and_create_passport_photo(image_bytes, country)
    
    st.image(result_img, caption="Your Passport Photo", use_column_width=True)
    
    # Save image to bytes for download
    buf = io.BytesIO()
    result_img.save(buf, format="JPEG", dpi=(DPI, DPI))
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Download Passport Photo",
        data=byte_im,
        file_name=f"passport_photo_{country}.jpg",
        mime="image/jpeg"
    )
