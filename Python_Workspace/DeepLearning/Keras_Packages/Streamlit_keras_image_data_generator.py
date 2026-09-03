import os
import streamlit as st
import pandas as pd
import numpy as np
# from tensorflow.keras.utils import image_dataset_from_directory
# import tensorflow as tf
# import tensorflow.keras as keras
# from keras.utils import array_to_img,img_to_array, load_img
# from tensorflow.keras.preprocessing.image import ImageDataGenerator


# def generate_augmented_images(imgage_path, max_images =30, output_folder_path="my_local_folder", file_prefix="image",file_type="jpeg"):
#     datagen = ImageDataGenerator(rotation_range=40,
#                                 width_shift_range = 0.2,
#                                 height_shift_range = 0.2,
#                                 shear_range = 0.2,
#                                 zoom_range = 0.2,
#                                 horizontal_flip = True,
#                                 fill_mode ='nearest'
#                                 )
#     img = load_img(r""+image_path)

#     x = img_to_array(img)
#     x = x.reshape((1,)+x.shape)
#     i = 0
#     # for batch in datagen.flow(x, batch_size=1,save_to_dir=r""+output_folder_path, save_prefix="dog_",save_format='jpeg'):
#     for batch in datagen.flow(x, batch_size=1):
#         image_array=batch[0]
#         save_to_file=f"{output_folder_path}/{file_prefix}_{i}.{file_type}"

#         print("Save to File = ", save_to_file)
#         tf.keras.utils.save_img(save_to_file,image_array)
#         i+=1
#         if i > max_images:
#             break


output_folder_path ="my_local_folder"

# import TF_keras_img_generator as tf_img_generator
def show_demo_tab(file_path,file_prefix,file_type,rotation_range):
    print('button clicked :::::::::',file_path)
    # tf_img_generator.generate_augmented_images(file_path,rotation_range,output_folder_path,file_prefix,file_type)
  


 

from PIL import Image
import tempfile
st.sidebar.title("Streamlit : Image Data Generator")
loaded_file_path=""
# Create the file uploader widget
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        # Write the uploaded file's bytes into the temp file
        tmp_file.write(uploaded_file.getvalue())
        
        # 2. Get the actual file path string
        loaded_file_path = tmp_file.name
    
    st.success(f"File temporarily saved at path: {loaded_file_path}")

    # Open the image with Pillow
    image = Image.open(uploaded_file)
    
    # st.write(f"The Original uploaded image : {uploaded_file}")
    
    # Resize the image (e.g., width=400px, height=400px)
    image_resized = image.resize((300, 300))
    
    # Display the resized original image
    st.image(image_resized, caption="Original Image")

save_prefix = st.sidebar.text_input("Enter file name prefix ", "Image")

pick_save_format = st.sidebar.selectbox("Save Image As ", ["jpg", "jpeg", "png"])
rotation_range = st.sidebar.slider("Rotation Range ", min_value=0, max_value=180, value=5)
# if st.sidebar.button("Generate"):
#     show_demo_tab(loaded_file_path,save_prefix,pick_save_format,rotation_range)


if st.sidebar.button("Generate Augmented Images"):
        with st.spinner("Generating augmented images..."):
            # Step A: Save the uploaded file locally first so we have a valid path
            temp_dir = "temp_uploads"
            os.makedirs(temp_dir, exist_ok=True)
            local_image_path = os.path.join(temp_dir, uploaded_file.name)
            
            with open(local_image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Step B: Call your augmentation function using the local path
            # generate_augmented_images(
            #     image_path=local_image_path, 
            #     max_images=30, 
            #     output_folder_path=output_folder_path, 
            #     file_prefix="dog", 
            #     file_type="jpeg"
            # )
            show_demo_tab(loaded_file_path,save_prefix,pick_save_format,rotation_range)

            
        st.success(f"Successfully generated augmented images inside the `{output_folder_path}` folder!")

