## Soal Prioritas 1 - Docker

1. Lakukan containerization pada aplikasi Python dengan kriteria berikut:
    - Jenis aplikasi yang dipilih bebas asalkan dikembangkan dengan Python.
    - Menggunakan Docker sebagai containerization.

**Jawab :**

**Mempersiapkan file utama nya dulu yaitu app.py yang merupakan code program utama**

![Gambar Code app.py ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-1/01_Code-app.py.png?raw=true)

Sebuah program yang menampilkan data frame awal yaitu (nama, usia, dan kota) dan data manipulasi (nama, usia +1, dan kota) menggunakan library pandas.

**Mempersiapkan file Dockerfile**

![Gambar Code Dockerfile ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-1/02_Code-Dockerfile.png?raw=true)

Dockerfile di atas adalah skrip konfigurasi yang digunakan untuk membangun sebuah image Docker. **FROM python:3.11-slim**: Instruksi ini mengambil base image yang akan digunakan sebagai dasar untuk membangun image Docker. **ENV PYTHONDONTWRITEBYTECODE 1** dan **ENV PYTHONUNBUFFERED 1**: Instruksi ini mengatur variabel lingkungan di dalam container. **WORKDIR /app**: Instruksi ini menetapkan direktori kerja di dalam container menjadi **/app**. **COPY requirements.txt requirements.txt**: Instruksi ini menyalin file **requirements.txt** dari direktori host ke dalam direktori **/app** di dalam container. **RUN pip install --no-cache-dir -r requirements.txt**: Instruksi ini menjalankan perintah untuk menginstal dependensi atau paket Python yang diperlukan. **CMD ["python", "app.py"]**: Instruksi ini menentukan perintah default yang akan dijalankan ketika container berjalan

**Mempersiapkan file requirements.txt**

![Gambar Code requirements.txt ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-1/03_File-requirements.txt.png?raw=true)

**Pandas** adalah library yang digunakan untuk analisis data di Python dengan versi 2.1.4

**Melakukan build docker image**

![Gambar build docker image ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-1/04_Build-docker-image.png?raw=true)

Berikut merupakan gambar proses melakukan build docker image dengan nama **my-simple-app** dan versi yang **1.0.0**

**Pengecekan Docker Image**

![Gambar Pengecekan Docker Image](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-1/05_Docker-image-success.png?raw=true)

Perintah **docker images** digunakan untuk menampilkan daftar dari semua image Docker yang telah diunduh atau dibuat. Terlihat docker image "my-simple-app" telah dibuat.

**Menjalankan Container**

![Gambar Jalankan Container](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-1/06_Jalankan-container.png?raw=true)

Perintah **docker run --name simpleapp my-simple-app:1.0.0** digunakan untuk menjalankan sebuah container Docker dari image yang ditentukan. Jadi, perintah ini akan mencari image Docker dengan nama **my-simple-app** dan tag **1.0.0**, kemudian membuat sebuah container dari image tersebut dengan nama **simpleapp**. Container tersebut kemudian akan dijalankan dengan menggunakan konfigurasi default yang didefinisikan dalam image Docker, seperti perintah yang akan dijalankan di dalam container dan pengaturan lingkungan lainnya. Setelah proses eksekusi tersebut jika dilakukan **docker ps** maka container nya sudah berhenti.
