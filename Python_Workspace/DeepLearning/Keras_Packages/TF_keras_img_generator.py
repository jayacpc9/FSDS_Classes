from tensorflow.keras.utils import image_dataset_from_directory
import tensorflow as tf
import tensorflow.keras as keras
from keras.utils import array_to_img,img_to_array, load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def generate_augmented_images(imgage_path, max_images=30, output_folder_path="temp_output_folder", file_prefix="image",file_type="jpeg"):
    datagen = ImageDataGenerator(rotation_range=40,
                                width_shift_range = 0.2,
                                height_shift_range = 0.2,
                                shear_range = 0.2,
                                zoom_range = 0.2,
                                horizontal_flip = True,
                                fill_mode ='nearest'
                                )
    img = load_img(r""+image_path)

    x = img_to_array(img)
    x = x.reshape((1,)+x.shape)
    i = 0
    # for batch in datagen.flow(x, batch_size=1,save_to_dir=r""+output_folder_path, save_prefix="dog_",save_format='jpeg'):
    for batch in datagen.flow(x, batch_size=1):
        image_array=batch[0]
        save_to_file=f"{output_folder_path}/{file_prefix}_{i}.{file_type}"

        print("Save to File = ", save_to_file)
        tf.keras.utils.save_img(save_to_file,image_array)
        i+=1
        if i > max_images:
            break



input_folder_path="/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/DeepLearning/Keras_Packages/Input_Data"
image_path =input_folder_path+"/beagle-hound-dog.jpg"
output_folder_path ="/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/DeepLearning/Keras_Packages/temp_output"

generate_augmented_images(image_path,30,output_folder_path)
