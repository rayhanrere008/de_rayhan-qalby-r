# Gunakan base image Python Slim
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory di dalam container
WORKDIR /app

# Install dependensi aplikasi
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy aplikasi ke dalam container
COPY . .

# Command yang akan dijalankan ketika container berjalan
CMD ["python", "app.py"]
