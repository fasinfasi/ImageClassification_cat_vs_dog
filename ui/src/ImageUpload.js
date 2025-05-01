import React, { useState } from 'react';
import axios from 'axios';

function ImageUpload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:5000/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setResult(res.data.prediction);
    } catch (error) {
      console.error('Upload failed:', error);
      setResult('Failed to get prediction');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Upload an Image</h2>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload & Predict</button>
      <p>{result}</p>
    </div>
  );
}

export default ImageUpload;
