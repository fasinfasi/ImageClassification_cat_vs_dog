import os
import requests

MODEL_URL = "https://huggingface.co/fasinfasi/cat_dog_classifier/resolve/main/cat_dog_classifier.h5"
MODEL_PATH = "models/cat_dog_classifier.h5"

def download_model_if_needed():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model file...")
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        response = requests.get(MODEL_URL, stream=True)
        response.raise_for_status()
        
        with open(MODEL_PATH, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Model downloaded successfully")
