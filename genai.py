import streamlit as st
from rembg import remove
from PIL import Image
import io

# 1. Page Title aur UI setup
st.title("Background Remover")
st.write("Upload an image to remove its background instantly!")

# 2. Image Upload karne ka option
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Original image screen par dikhayen
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Original Image")
    
    # 3. Button dabane par action
    if st.button("Remove Background"):
        with st.spinner("removing background..."):
            # Background remove karne ka main function
            output_image = remove(input_image)
            
            # Result screen par dikhayen
            st.image(output_image, caption="Background Removed")
            
            # 4. Download option banane ke liye image ko bytes mein convert karna
            buf = io.BytesIO()
            output_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label="⬇️ Download Image",
                data=byte_im,
                file_name="transparent_image.png",
                mime="image/png"
            )