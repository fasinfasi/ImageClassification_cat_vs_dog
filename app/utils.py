
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np
from model_downloader import download_model_if_needed

download_model_if_needed()

model = load_model('models/cat_dog_classifier.h5')

def predict_image(image_path):
    img = load_img(image_path, target_size=(150,150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)/255.0

    prediction = model.predict(img_array)[0][0]
    return 'This is dog.' if prediction > 0.5 else 'This is cat.'
