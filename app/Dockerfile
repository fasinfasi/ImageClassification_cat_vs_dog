# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy backend files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Expose the Flask default port
EXPOSE 8000

# Run your Flask app
CMD ["python", "main.py"]
