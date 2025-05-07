import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path='model/model_fp32.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_image(image_path):
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0).astype(np.float32) / 255.0

    # Set the tensor to point to the input data
    interpreter.set_tensor(input_details[0]['index'], img_array)

    # Run the model
    interpreter.invoke()

    # Extract the prediction
    output_data = interpreter.get_tensor(output_details[0]['index'])
    prediction = output_data[0][0]
    
    return 'This is dog.' if prediction > 0.5 else 'This is cat.'
