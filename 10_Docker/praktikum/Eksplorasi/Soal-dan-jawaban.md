## Soal Eksplorasi - Docker 

1. Buatlah sebuah aplikasi ETL sederhana dengan menggunakan Python dan Docker yang memiliki kriteria sebagai berikut:
    - Dataset diambil dengan menggunakan API berikut: https://jsonplaceholder.typicode.com/posts?userId=1 
    - Dataset yang diambil kemudian ditambahkan ke dalam database.
    - Menggunakan Docker Compose sebagai container orchestration untuk aplikasi Python dan database.
    - Jenis database yang digunakan bebas. Boleh menggunakan database relasional seperti MySQL maupun non relasional seperti MongoDB.
    - Arsitektur aplikasi diilustrasikan pada gambar berikut: API > python app > DB

**Jawab :**

**Persiapkan file main.py yang merupakan code program utama**

![Gambar Code main.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/01_Code-main.py.png?raw=true)

![Gambar Code main.py2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/01_Code-main.py2.png?raw=true)

![Gambar Code main.py3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/01_Code-main.py3.png?raw=true)

Impor modul: **os** untuk variabel lingkungan, **requests** untuk mengirim permintaan HTTP, dan **mysql.connector** untuk berinteraksi dengan database MySQL. Terdapat dua fungsi utama: **get_post_data()**: Fungsi ini mengirim permintaan ke **API JSONPlaceholder** untuk mendapatkan data posting. Kemudian, data tersebut diambil dalam format JSON. **insert_into_mysql(posts)**: Fungsi ini bertanggung jawab untuk menyisipkan data posting ke dalam tabel **MySQL**. Secara singkat code diatas memiliki fungsi untuk mengambil data posting dari API JSONPlaceholder dan menyimpannya ke dalam database MySQL.

**Persiapkan Dockerfile**

![Gambar Code Dockerfile](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/02_Code-Dockerfile.png?raw=true)

Seperti biasanya **Dockerfile** ini digunakan untuk membangun sebuah container Docker yang menjalankan aplikasi Python, memastikan semua dependensi terinstal, dan kemudian menjalankan skrip Python saat container dimulai.

**Persiapkan requirements.txt**

![Gambar Code requirements.txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/03_Code-requirements.txt.png?raw=true)

**requests==2.31.0**: Ini adalah dependensi yang diperlukan untuk melakukan permintaan **HTTP**. **mysql-connector-python==8.3.0**: Dependensi ini diperlukan untuk berinteraksi dengan database **MySQL** dari aplikasi Python. 

**Persiapkan docker-compose.yml**

![Gambar Code docker-compose.yml](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/04_Code-docker-compose.png?raw=true)

![Gambar Code docker-compose.yml](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/04_Code-docker-compose2.png?raw=true)

file **docker-compose** yang mendefinisikan dua layanan (services): **app-service** dan **database-service**. **app-service** adalah layanan yang akan membangun aplikasi dari direktori saat ini (.), menetapkan variabel lingkungan yang diperlukan untuk koneksi database, dan menetapkan ketergantungan pada **database-service**.  Ini akan dihubungkan ke jaringan **my-network**. Command **--init-file** digunakan untuk menjalankan inisialisasi SQL saat kontainer pertama kali dibuat. Jaringan **my-network** didefinisikan sebagai jaringan **bridge** untuk menghubungkan kedua layanan.

**Persiapkan .env**

![Gambar Code .env](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/05_Code-env.png?raw=true)

ini adalaha variabel lingkungan yang diperlukan untuk konfigurasi koneksi ke basis data MySQL dalam lingkungan Docker. Yang diperlukan mulai dari alamat host, port, username, password, dan nama database.

**Persiapkan init.sql**

![Gambar Code init.sql](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/06_Code-init.sql.png?raw=true)

Perintah SQL tersebut digunakan untuk membuat basis data baru dengan nama **etl_db**, jika basis data tersebut belum ada.

**Build dan Jalankan Container**

![Gambar Build dan Jalankan Container](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/07_Build-dan-Jalankan-Container.png?raw=true)

Perintah **docker-compose up -d** digunakan untuk memulai semua layanan yang didefinisikan dalam file **docker-compose.yml** dan menjalankannya di **latar belakang** (mode detached).

**Build Success**

![Gambar Build Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/08_Build-dan-Jalankan-Container-Success.png?raw=true)

Terlihat bahwa semua layanan termasuk container berhasil dijalankan dan dibangun seperti network, container app service, dan container database service (Health).

**Pengecekan Container Berhasil Dijalankan**

![Gambar Pengecekan Container](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/09_Container-berhasil-dijalankan.png?raw=true)

Perintah **docker ps -a** digunakan untuk menampilkan daftar semua container yang ada di mesin Docker, termasuk container yang sedang berjalan dan yang sudah berhenti. Terlihat bahwa **container app service** berhasil dijalankan dan langsung berhenti setelah dieksekusi. **container database service** sedang berjalan dan berstatus **Healthy**.

**Data Berhasil Diinsert ke Database MySQL**

![Gambar Data Insert to MySQL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/10_Data-success-insert-to-mysql.png?raw=true)

Perintah logs pada container database service menunjukkan hasil **(200)** menandakan respon **API Oke** yaitu data berhasil diambil dan muncul **Data Inserted Successfuly into MySQL** menandakan bahwa data yang telah diambil berhasil diinsert ke **Database MySQL**.

**Pengecekan Database**

![Gambar Pengecekan Database](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/11_Pengecekan-di-database.png?raw=true)

Dengan menjalankan perintah tersebut, maka akan masuk ke dalam shell di dalam container Docker my-etl-app-database-service-1 dengan hak akses root dan password yang telah ditentukan. Ini digunakan untuk menjalankan perintah SQL di shell MySQL.

**Database dan Table berhasil dibuat**

![Gambar Database dan Table Success Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/12_Database-dan-table-berhasil-dibuat.png?raw=true)

Terlihat bahwa **etl_db** berhasil dibuat dan digunakan. Lalu melakukan perintah **SHOW TABLES;** untuk menunjukan bahwa tabel berhasil dibuat yaitu **tabel posts**.

**Data berhasil diinsert di tabel posts**

![Gambar Data berhasil diinsert di dalam tabel](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/13_Data-berhasil-diinsert-di-table-posts.png?raw=true)

![Gambar Data berhasil diinsert di dalam tabel](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/14_Data-berhasil-diinsert-di-table-posts(2).png?raw=true)

Perintah **SELECT * FROM posts;** digunakan untuk menampilkan data di dalam **tabel posts**. Terlihat bahwa data **id**, **userId**, **title**, dan **body** berhasil ditampilkan.

**Layanan dan Container dihentikan**

![Gambar Layanan Dihentikan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/10_Docker/screenshots/Eksplorasi/15_Container-dihentikan.png?raw=true)

Perintah **docker-compose down** digunakan untuk menghentikan dan membersihkan semua layanan yang dijalankan menggunakan Docker Compose. Layanan network, container app service, container database service berhasil dihentikan.