import sys
import os
# Force TensorFlow to run on CPU to prevent GPU memory locks
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.utils import img_to_array, load_img

def run_augmentation(image_path, output_folder, prefix, fmt, rotation, max_imgs):
    os.makedirs(output_folder, exist_ok=True)
    
    datagen = ImageDataGenerator(
        rotation_range=rotation,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    img = load_img(image_path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1):
        save_path = os.path.join(output_folder, f"{prefix}_{i}.{fmt}")
        tf.keras.utils.save_img(save_path, batch[0])
        i += 1
        if i >= max_imgs:
            break

if __name__ == "__main__":
    # Receive parameters passed from Streamlit
    img_path = sys.argv[1]
    out_dir = sys.argv[2]
    file_prefix = sys.argv[3]
    file_format = sys.argv[4]
    rot_range = int(sys.argv[5])
    max_count = int(sys.argv[6])

    run_augmentation(img_path, out_dir, file_prefix, file_format, rot_range, max_count)