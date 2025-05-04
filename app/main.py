from utils import predict_image
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import tempfile
import os
import requests

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
    

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        filename = secure_filename(file.filename)

        # Use a temporary file for prediction
        with tempfile.NamedTemporaryFile(delete=False, suffix=filename) as temp:
            file.save(temp.name)
            temp_path = temp.name

        try:
            result = predict_image(temp_path)
        except Exception as e:
            os.remove(temp_path)
            return jsonify({'error': f'Prediction failed: {str(e)}'})

        os.remove(temp_path)  # Clean up the file after use
        return jsonify({'prediction': result})

    return "Image Classification API is working"

@app.route('/')
def index():
    return "Flask API is running!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)