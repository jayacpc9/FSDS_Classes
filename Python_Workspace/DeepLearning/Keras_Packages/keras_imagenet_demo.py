import ssl

# Fix SSL certificate verification for downloading weights
ssl._create_default_https_context = ssl._create_unverified_context

# Import all model classes and their corresponding preprocessing tools
from tensorflow.keras.applications import (
    DenseNet121,
    EfficientNetV2B0,
    InceptionV3,
    MobileNetV2,
    NASNetLarge,
    NASNetMobile,
    ResNet50,
    ResNet50V2,
    VGG16,
    VGG19,
    Xception,
)
from tensorflow.keras.applications.densenet import (
    preprocess_input as dense_preprocess,
)
from tensorflow.keras.applications.efficientnet_v2 import (
    preprocess_input as eff_preprocess,
)
from tensorflow.keras.applications.inception_v3 import (
    preprocess_input as incep_preprocess,
)
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input as mob_preprocess,
)
from tensorflow.keras.applications.nasnet import (
    preprocess_input as nas_preprocess,
)
from tensorflow.keras.applications.resnet import (
    preprocess_input as res_preprocess,
)
from tensorflow.keras.applications.resnet_v2 import (
    preprocess_input as resv2_preprocess,
)
from tensorflow.keras.applications.vgg16 import (
    preprocess_input as vgg16_preprocess,
)
from tensorflow.keras.applications.vgg19 import (
    preprocess_input as vgg19_preprocess,
)
from tensorflow.keras.applications.xception import (
    preprocess_input as xcep_preprocess,
)

# Map each model name to its constructor and matching preprocessing function
models_map = {
    "ResNet50V2": {"class": ResNet50V2, "preprocess": resv2_preprocess},
    "VGG16": {"class": VGG16, "preprocess": vgg16_preprocess},
    "ResNet50": {"class": ResNet50, "preprocess": res_preprocess},
    "VGG19": {"class": VGG19, "preprocess": vgg19_preprocess},
    "Xception": {"class": Xception, "preprocess": xcep_preprocess},
    "InceptionV3": {"class": InceptionV3, "preprocess": incep_preprocess},
    "MobileNetV2": {"class": MobileNetV2, "preprocess": mob_preprocess},
    "DenseNet121": {"class": DenseNet121, "preprocess": dense_preprocess},
    "NASNetMobile": {"class": NASNetMobile, "preprocess": nas_preprocess},
    "NASNetLarge": {"class": NASNetLarge, "preprocess": nas_preprocess},
    "EfficientNetV2B0": {"class": EfficientNetV2B0, "preprocess": eff_preprocess},
}

# Example: Run through each model one by one
loaded_models = {}

for name, config in models_map.items():
    print(f"Loading {name}...")

    # Load weights
    model_instance = config["class"](weights="imagenet")

    # Store loaded model and preprocessor for future use
    loaded_models[name] = {
        "model": model_instance,
        "preprocess": config["preprocess"],
    }

    print(f"Successfully loaded {name}!\n")