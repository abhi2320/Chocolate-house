# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the instance directory for the SQLite database
RUN mkdir -p /app/instance

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production  

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
