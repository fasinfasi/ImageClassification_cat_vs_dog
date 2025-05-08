# 🐶🐱 Cat vs Dog Image Classifier 😺🐶

A deep learning project that classifies images as either **cat** or **dog** using a **Convolutional Neural Network (CNN)** built with **Keras**. The model is trained, evaluated, compressed and deployed as a Flask API and Dockerized for easy deployment.

#### Dataset
Dogs vs Cats Dataset from Kaggle. link: [kaggle.com](https://www.kaggle.com/datasets/vrajesh0sharma7/cat-vs-dog-classification)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Model Architecture](#-model-architecture)
- [Project Architecture](#-project-structure)
- [Setup](#-setup)
- [Usage](#-usage)
- [containerization](#-docker-deployment)
- [Deployment]((#deploy-on-rendercom))
- [License](#-license)

---

## 📖 About the Project

This project trains a CNN to classify images of cats and dogs using TensorFlow/Keras. The trained model is then served via a Flask API and containerized using Docker for scalable deployment.

---

## ✨ Features

- Image preprocessing with `ImageDataGenerator`
- CNN built with Conv2D, MaxPooling2D, and Dense layers
- Accuracy up to **98%** on validation data
- Flask-based REST API for predictions
- Docker support for easy deployment
- Render.com deployment-ready

## ⛏ Tech Stack

---

| Category        | Tools Used                     |
|----------------|--------------------------------|
| backend        | Python                          |
| frontend        | Javascript (react)             |
| Libraries       | TensorFlow, Keras, NumPy, Flask|
| Model Deployment| Flask, Gunicorn, Docker        |
| Hosting         | Render.com                     |

---

## 🧠 Model Architecture

```text
Input Layer (150x150x3)
↓
Conv2D → MaxPooling2D
↓
Conv2D → MaxPooling2D
↓
Conv2D → MaxPooling2D
↓
Flatten → Dense (128) → Dense (1, sigmoid)
```

## 📚 Project Structure

```
cat-vs-dog-classifier/
│
├── app/
│   ├── model/
│   │   └── model_fp32.tflite   # Trained model
│   ├── templates
|   ├── Dockerfile
|   ├── requirements.txt        # Required libraries
│   ├── main.py                 # Flask app
│   └── utils.py                # Helper functions
|
├── ui/
│   ├── src/
|   |   ├── App.js
|   |   ├── config.js                # Configering file(url)
|   |   ├── ImageUpload.css
|   |   ├── index.js
│   │   └── components
|   |          └── ImageUpload.js    # Main js
│   ├── .env
│   ├── Dockerfile
│   └── nginx.conf
|
├── docker-compose.yml
├── README.md
└── .gitignore
```

## 🧑🏻‍💻 Setup

#### 1. Clone the Repository
```
git clone https://github.com/fasinfasi/ImageClassification_cat_vs_dog.git
cd cat-vs-dog-classifier
```
#### 2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
#### 3. Install Dependencies

```  
pip install -r requirements.txt
```

#### 4. Run Locally
**To run backend**
```
cd app
python main.py
```
Visit: http://localhost:8000

```
cd ui
npm start
```
Visit: http://localhost:3000

## 🤔 Usage
You can upload an image via the frontend or make a prediction via API.
#### Upload via Frontend
- Go to http://localhost:8000
- Upload a cat/dog image(png or jpg)
- See the prediction

#### You can use Postman or Curl
**Use curl:**

```
curl -X POST -F "file=@cat.jpg" http://localhost:8000/predict
```

**Result:**
```
{
  "prediction": "Cat",
  "confidence": 0.93
}
```

**Use Postman**

---
| Endpoint  | Method    | Description  |
|-----------|-----------|----------------|
| /        | GET        | Home page (optional frontend)  |
| /predict   | POST     | Accepts image and returns result  |

---
## 📦 Docker Deployment
#### 1. Build Docker Image

```
docker build -t cat-dog-app . 
```
#### 2. Run Docker Container

```    
docker run -d -p 8000:8000 cat-dog-app
```
#### 3. Access App
Visit: http://localhost:8000

## ☁️ Deploy on Render.com
#### 1. Prep & Push Your Code
**Ensure your repo layout (in GitHub) is:**

```
├── app/              ← Flask backend + Dockerfile  
└── ui/               ← React frontend + Dockerfile or build scripts
```

**Commit & push all changes (including Dockerfiles) to your default branch (e.g. main).**
#### 2. Deploy the Backend First
1. On Render, click “New” → “Web Service”.
2. Connect to your GitHub repo and select branch main.
3. Language: Python
4. Name: imageclassify-backend (What you want name)
5. Root Directory: app
6. Environment: Docker (it will auto-detect your app/Dockerfile)
7. Port override: 8000
8. Env Vars (in Render dashboard):

     ```FLASK_ENV=production```
   
10. Create Service → Wait for build & deploy → note the Backend URL, e.g.
    
     ```https://imageclassify-backend.onrender.com ```

#### 3. Update CORS & Frontend Settings
1. In your Flask CORS setup, allow your new backend domain if needed (optional):
   
```    
CORS(app, origins=["https://imageclassify-frontend.onrender.com"])
```
2. In your React code’s .env (or Render’s Env Vars), set:

``` 
REACT_APP_BACKEND_URL=https://imageclassify-backend.onrender.com
```

### 4. Deploy the Frontend
1. On Render, click “New” → “Static Site”.
2. Connect to the same repo and branch main.
4. Name: imageclassify-frontend (What you want the name)
5. Root Directory: ui
6. Build Command: npm install && npm run build
7. Publish Directory: build
8. Env Vars:
   
```
REACT_APP_BACKEND_URL=https://imageclassify-backend.onrender.com
```
8. Create Static Site → Wait for build → note the Frontend URL, e.g.

```
https://imageclassify-frontend.onrender.com
```

#### 5. Verify End-to-End
- Open your Frontend URL in browser.
- Upload an image -> Check that requests go to
  
```
https://imageclassify-backend.onrender.com/predict
```

- You should see live predictions.

## 📃 License
This project is licensed under the MIT License - see the [License](LICENSE) file for details.

#### 🥰😘 Thanks bro, spending your valuable time to read my ReadMe....😘

#### Remember my name Fasin 🙋🏻‍♂️
