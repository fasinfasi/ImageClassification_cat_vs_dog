import React, { useState, useRef } from 'react';
import './ImageUpload.css';

const ImageUpload = () => {
  const [image, setImage] = useState(null);
  const [prediction, setPrediction] = useState('');
  const fileInputRef = useRef(null);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    setImage(droppedFile);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleClick = () => {
    fileInputRef.current.click();
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('file', image);

    try {
      const res = await fetch('http://localhost:5000/', {
        method: 'POST',
        body: formData,
      });

      const data = await res.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container">
      <div className="left-panel">
        <video
          className="video-bg"
          autoPlay
          loop
          muted
          playsInline
          disablePictureInPicture
          controlsList="nodownload nofullscreen noremoteplayback"
          controls={false}
        >
          <source src="shorts_cat_dog.mp4" type="video/mp4" />
        </video>
        <div className="overlay-text">
          <h1><span>I'm a<span className="head-name"> CatDo</span></span><br />Predictor</h1>
          <p>I can detect your pet from image.</p>
        </div>
      </div>

      <div className="right-panel">
        <h2>Upload image of cat or dog, I can detect what that is</h2>
        <div
          className={`drop-zone ${image ? 'image-present' : ''}`}
          onClick={handleClick}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
        >

          {image ? (
            <img
              src={URL.createObjectURL(image)}
              alt="Uploaded preview"
              className="drop-image-preview"
            />
          ) : (
            <p>Drop or Select your image file</p>
          )}
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleImageChange}
            style={{ display: 'none' }}
          />
      </div>

        <button onClick={handleSubmit}>Predict</button>
        {prediction && <div className="result">{prediction}</div>}
      </div>
    </div>
  );
};

export default ImageUpload;
