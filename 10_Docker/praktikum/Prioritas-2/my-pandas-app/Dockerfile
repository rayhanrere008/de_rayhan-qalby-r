# Gunakan gambar Python versi terbaru
FROM python:latest

# Set direktori kerja di dalam container
WORKDIR /app

# Salin kode aplikasi dan requirements.txt ke dalam container
COPY . /app

# Instal dependensi Python
RUN pip install -r requirements.txt

# Perintah untuk menjalankan aplikasi
CMD ["python", "app.py"]
