## Soal Prioritas 2 - Docker

1. Lakukan containerization pada aplikasi Python dengan kriteria berikut:
- Jenis aplikasi yang dipilih bebas asalkan dikembangkan dengan Python.
- Menggunakan Docker sebagai containerization.
- Menggunakan Docker Compose.

**Jawab :**

**Mempersiapkan file utama nya dulu yaitu app.py yang merupakan code program utama**

![Gambar Code app.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/01_Code-app.py.png?raw=true)

Sebuah program yang menampilkan data nama dan location menggunakan library pandas.

**Mempersiapkan dockerfile**

![Gambar Code Dockerfile](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/02_Code-dockerfile.png?raw=true)

Dockerfile di atas adalah skrip yang digunakan untuk membangun image Docker yang akan digunakan untuk menjalankan aplikasi Python.**FROM python:latest:** Ini adalah perintah untuk mendownload dan menggunakan gambar Docker resmi untuk Python dengan versi terbaru yang tersedia. **WORKDIR /app**: Perintah ini menetapkan direktori kerja di dalam container ke **/app**. **COPY . /app**: Perintah ini menyalin semua file dari direktori proyek lokal (termasuk **file app.py** dan **requirements.txt**, jika ada) ke dalam direktori **/app** di dalam container. **RUN pip install -r requirements.txt**: Ini adalah perintah yang akan dijalankan saat membangun image Docker. **CMD ["python", "app.py"]**: Ini adalah perintah default yang akan dijalankan saat container dimulai.

**Mempersiapkan requirements.txt**

![Gambar Code requirements.txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/03_Code-requirements.txt.png?raw=true)

**Pandas** adalah library yang digunakan untuk analisis data di Python dengan versi 2.1.4

**Mempersiapkan file docker-compose.yml**

![Gambar Code docker-compose.yml](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/04_Code-docker-compose.yaml.png?raw=true)

**version: '3'**: Menunjukkan versi format Docker Compose yang digunakan. **services**: Ini adalah bagian utama dari file yang mendefinisikan layanan-layanan yang akan dijalankan. **myapp**: Ini adalah nama layanan yang diberikan kepada aplikasi atau kontainer yang akan dijalankan. **build: .**: Ini adalah perintah untuk membangun image Docker dari direktori saat ini (yang mengandung Dockerfile). **ports: ["4000:4000"]**: Ini adalah perintah untuk meneruskan port dari host ke kontainer.

**Build dan Jalankan Container**

![Gambar Build dan Jalankan Container](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/05_Build-dan-Jalankan-Container.png?raw=true)

![Gambar Build dan Jalankan Container](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/06_Build-dan-Jalankan-Container(2).png?raw=true)

Perintah **docker-compose up --build** digunakan untuk membangun dan menjalankan container berdasarkan konfigurasi yang diberikan dalam file **docker-compose.yml**.

**Container Aplikasi Berhasil Dijalankan**

![Gambar Container Aplikasi Berhasil Dijalankan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/07_Aplikasi-berhasil-dijalankan.png?raw=true)

Perintah **docker ps -a** digunakan untuk menampilkan daftar semua kontainer Docker yang sedang berjalan atau telah berhenti. Terlihat container aplikasi **my-pandas-app-myapp-1** berhasil dijalankan dan otomatis berhenti setelah pengeksekusian build tadi.

**Logs Memunculkan Data**

![Gambar Logs Output Sesuai](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/08_Logs-berhasil-muncul-data.png?raw=true)

Perintah **docker logs my-pandas-app-myapp-1** digunakan untuk melihat output log dari sebuah kontainer Docker yang sedang berjalan. Terlihat muncul data sesuai dengan yang dinginkan oleh program.

**Container Docker Compose Dihentikan**

![Gambar Container Docker Compose Distop](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Prioritas-2/09_Aplikasi-dengan-docker-compose-dihentikan.png?raw=true)

Perintah **docker-compose down** digunakan untuk menghentikan dan menghapus semua kontainer yang sedang berjalan yang dibuat menggunakan Docker Compose. Terlihat container dan network berhasil dihentikan dan dihapus.