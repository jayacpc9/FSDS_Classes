import os
import subprocess
import sys
from PIL import Image
import streamlit as st

st.sidebar.title("Streamlit : Image Data Generator")

uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
save_prefix = st.sidebar.text_input("Enter file name prefix", "Image")
pick_save_format = st.sidebar.selectbox("Save Image As", ["jpeg", "png", "jpg"])
rotation_range = st.sidebar.slider("Rotation Range", min_value=0, max_value=180, value=40)
max_images = st.sidebar.number_input("Max Images", min_value=1, max_value=100, value=30)

output_folder = "my_local_folder"

if uploaded_file is not None:
    st.image(Image.open(uploaded_file).resize((300, 300)), caption="Original Image")

    if st.sidebar.button("Generate Augmented Images"):
        with st.spinner("Generating augmented images via isolated background process..."):
            # Step 1: Save the temporary file
            temp_dir = "temp_uploads"
            os.makedirs(temp_dir, exist_ok=True)
            local_image_path = os.path.join(temp_dir, uploaded_file.name)
            with open(local_image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            script_dir = os.path.dirname(os.path.abspath(__file__))
            tf_script_path = os.path.join(script_dir, "tf_augment.py")

            python_bin = "/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/DeepLearning/Ann_env/bin/python"  # Replace with your actual env path

            command = [
                python_bin, 
                tf_script_path,
                local_image_path,
                output_folder,
                save_prefix,
                pick_save_format,
                str(rotation_range),
                str(max_images)
            ]

            # Run process and capture potential errors
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                st.success(f"Successfully generated {max_images} images inside `{output_folder}`!")
#
            # Load and display all generated images from the output directory
                if os.path.exists(output_folder):
                    valid_extensions = (".jpg", ".jpeg", ".png")
                    generated_files = [
                        f
                        for f in os.listdir(output_folder)
                        if f.lower().endswith(valid_extensions)
                    ]

                    if generated_files:
                        st.divider()
                        st.subheader(f"Generated Images ({len(generated_files)})")

                        # Display images in a grid layout (4 images per row)
                        num_cols = 5
                        cols = st.columns(num_cols)

                        for idx, img_file in enumerate(generated_files):
                            img_path = os.path.join(output_folder, img_file)
                            col = cols[idx % num_cols]
                            with col:
                                st.image(img_path, caption=img_file, use_container_width=True)
#
                
            else:
                st.error("TensorFlow script failed in background!")
                st.code(result.stderr)  # Print full TF crash output safely in Streamlit UI
else:
    st.info("Please upload an image from the sidebar to start.")