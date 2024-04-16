## Soal dan Jawaban Prioritas 1 - Data Engineering in The Cloud

1. Sebuah survei mengenai pengembangan software telah dilakukan dan didapatkan data sebagai berikut. Buatlah sebuah pipeline ETL sederhana dengan kriteria berikut:
    - Lakukan proses ekstrak data dari csv.
    - Lakukan proses transformasi data. Transformasi bisa berupa proses data cleaning untuk menghindari data duplikat dan data yang tidak lengkap.
    - Lakukan proses load data dalam format csv ke dalam Google Storage.

2. Sebuah platform e-commerce telah merekap data transaksi. Buatlah sebuah pipeline ETL sederhana dengan kriteria berikut:
    - Lakukan proses ekstrak data.
    - Lakukan proses transformasi data yaitu dengan mengambil data transaksi yang menggunakan metode pembayaran kartu kredit (credit card) dan status nya success
    - Lakukan proses load data dalam format csv ke dalam Google Storage.

**Jawaban :**

- **Melakukan pembuatan project di Google Storage (Firebase):**

    ![Create Project](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/01_create-project-google-storage.png?raw=true)

    ![Create Project](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/02_project-created.png?raw=true)

- **Setup pengaturan Cloud Storage:**

    ![Setup cloud storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/03_setup-cloud-storage.png?raw=true)

    ![Setup cloud storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/04_setup-cloud-storage2.png?raw=true)

- **Storage Bucket Created:**

    ![Storage Bucket Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/05_storage-bucket-created.png?raw=true)

- **Atur Hak akses:**

    ![Atur Hak akses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/06_atur-hak-akses.png?raw=true)

- **Create Service Account:**

    ![Create Service Account](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/07_create-service-account.png?raw=true)

- **Install Library yang dibutuhkan (pandas, firebase admin, requests):**

    ![Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/08_install-library-firebase-admin.png?raw=true)

    ![Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/09_install-library-pandas.png?raw=true)

**Jawaban No.1 :**

- **Download file dataset**

    ![Gambar Download file dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_download-dataset-survey.csv.png?raw=true)

- **Code Inisialisasi Firebase**

    ![Gambar Code Inisialisasi Firebase](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_Code-inisialisasi-firebase.png?raw=true)

    **Dengan kode ini, aplikasi Python sudah siap untuk berinteraksi dengan Firebase Storage menggunakan Firebase Admin SDK**

- **Code Function ETL**

    ![Gambar Code Function ETL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_Code-function-ETL.png?raw=true)

    **extract_data(file_path): Fungsi ini digunakan untuk mengekstrak data dari file CSV yang diberikan. Ini menggunakan pustaka pandas untuk membaca file CSV ke dalam sebuah DataFrame. transform_data(data): Fungsi ini bertanggung jawab untuk melakukan transformasi data yaitu menghapus baris duplikat dan baris yang memiliki nilai NULL dari DataFrame. load_data_to_firebase_storage(data, file_name): Fungsi ini digunakan untuk memuat data yang telah di-transformasi ke Firebase Storage dalam format CSV.**

- **Code Function Main**

    ![Gambar Code Function Main](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_Code-main-function.png?raw=true)

    **Kode ini merupakan fungsi utama (main) yang menggabungkan langkah-langkah ekstraksi, transformasi, dan pemrosesan data ke Firebase Storage. Terakhir, pesan "Data has been successfully processed and uploaded to Firebase Storage." dicetak ke konsol untuk memberikan informasi bahwa proses telah berhasil.**

- **Running Code Success**

    ![Gambar Running Code Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_running-code-success.png?raw=true)

    **Terlihat pesan "Data has been successfully processed and uploaded to Firebase Storage." dicetak ke konsol untuk memberikan informasi bahwa proses telah berhasil.**

- **File csv berhasil di load ke firebase storage**

    ![Gambar File csv berhasil di load](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_file-csv-berhasil-di-load-ke-storage.png?raw=true)

    **Telihat file output_survey.csv berhasil di load.**

- **Isi file output_survey.csv**

    ![Gambar Isi file output_survey.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-1_isi-file-output_survey.csv.png?raw=true)

    **Telihat menampilkan data yang telah ditransformasikan sehingga memunculkan data yang tidak ada duplikasi dan menghilangkan baris yang memiliki nilai null.**

**Jawaban No.2 :**

- **Code Inisialisasi Firebase**

    ![Gambar Code Inisialisasi Firebase](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-2_Code-inisialisasi-firebase.png?raw=true)

    **Dengan kode ini, aplikasi Python sudah siap untuk berinteraksi dengan Firebase Storage menggunakan Firebase Admin SDK**

- **Code Function ETL**

    ![Gambar Code Function ETL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-2_Code-function-ETL.png?raw=true)

    **extract_data(url): Fungsi ini mengambil data dari URL yang diberikan. Menggunakan pustaka requests, data JSON diunduh dari URL, kemudian dikonversi menjadi DataFrame menggunakan pustaka pandas. transform_data(data): Fungsi ini melakukan transformasi data pada DataFrame yang diberikan. Data difilter berdasarkan dua kriteria: pembayaran dengan kartu kredit ('payment_method' == 'credit card') dan status yang sukses ('status' == 'success'). load_data_to_firebase_storage(data, bucket_name, file_name): Fungsi ini memuat data hasil transformasi ke Firebase Storage dalam format CSV.**

- **Code Function Main**

    ![Gambar Code Function Main](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-2_Code-main-function.png?raw=true)

    **Dengan demikian, kode ini akan mengeksekusi langkah-langkah tersebut secara berurutan, mulai dari mengunduh data, melakukan transformasi, hingga memuatnya ke Firebase Storage, ketika skrip dijalankan sebagai program utama.**

- **Running Code Success**

    ![Gambar Running Code Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-2_running-code-success.png?raw=true)

    **Terlihat pesan "Data has been successfully loaded to Firebase Storage with filename : output_transactions.csv" dicetak ke konsol untuk memberikan informasi bahwa proses telah berhasil.**

- **File csv berhasil di load ke firebase storage**

    ![Gambar File csv berhasil di load](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-2_file-csv-berhasil-di-load-ke-storage.png?raw=true)

    **Telihat file output_transactions.csv berhasil di load.**

- **Isi file output_transactions.csv**

    ![Gambar Isi file output_transactions.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-1/Soal-2_isi-file-output_transactions.csv.png?raw=true)

    **Telihat menampilkan data yang telah ditransformasikan sehingga memunculkan data dengan metode pembayaran : credit card dengan status : success.**
