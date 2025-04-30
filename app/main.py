from flask import Flask, jsonify, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)
model = load_model('model/cat_dog_classifier.h5')

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def predict_image(image_path):
    img = load_img(image_path, target_size=(150,150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)/255.0

    prediction = model.predict(img_array)[0][0]
    if prediction > 0.5:
        return 'This is a dog.'
    else:
        return 'This is a cat.'
    

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in the request'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        result = predict_image(file_path)
        return jsonify({'prediction': result})
    return "Image Classification API is working"

if __name__ == '__main__':
    app.run(debug=True)
