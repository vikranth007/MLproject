# use a lightweight Python image
FROM python:3.9-slim

# Set Working directory
WORKDIR /app

# Copy all project files
COPY . . 

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Cloud Run uses
EXPOSE 8080

# Run Your FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
