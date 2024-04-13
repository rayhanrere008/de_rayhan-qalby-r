## Soal dan Jawaban Eksplorasi - Data Ingestion

![Gambar Workflow Soal](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/01_workflow-soal.png?raw=true)

1. Ekstraksi Data dari API:
    - Gunakan Python untuk mengirim permintaan HTTP ke https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json dan terima respons dalam format JSON.
    - Ekstrak data buku yang relevan dari respons JSON, seperti judul, pengarang, tahun terbit, dan genre.
2. Pembuatan DAG di Apache Airflow:
    - Buat DAG di Apache Airflow untuk menjadwalkan dan mengotomatisasi proses ekstraksi data ini.
    - Tentukan jadwal eksekusi menggunakan cron expression, misalnya setiap minggu pada hari Senin jam 09:00.
3. Integrasi Skrip Python untuk Ekstraksi Data:
    - Integrasikan skrip Python yang telah Anda buat untuk ekstraksi data ke dalam task di Airflow menggunakan PythonOperator.
4. Pengujian dan Monitoring:
    - Jalankan DAG dan monitor prosesnya melalui UI Airflow.
    - Pastikan data berhasil diambil dan diolah sesuai jadwal yang ditentukan.

**Jawaban :**

- **Ekstrak data dari API:**

    ![Gambar Code Ekstrak Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/02_Code-ekstrak-data-dari-API.png?raw=true)

    **Code tersebut merupakan sebuah program Python yang menggunakan pustaka requests untuk mengambil data dari sebuah URL yang merupakan file JSON. Data JSON tersebut kemudian diolah menggunakan pustaka pandas untuk mengekstraksi informasi tertentu dari setiap objek dalam data tersebut, dan menyimpannya ke dalam sebuah file CSV. Data yang diambil berupa sebuah data buku yang terdiri dari title, author, year, dan genre.**

- **Hasil Ekstrak berupa file CSV:**

    ![Gambar Output Code](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/03_Output-code.png?raw=true)

    ![Gambar Data disimpan di file csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/04_Data-disimpan-di-CSV.png?raw=true)

    **Terlihat bahwa data berhasil diambil dari API dengan menyimpan sebuah file csv yang berisikan data books yang terdiri dari judul, pengarang, tahun_terbit, dan genre.**

- **Instalasi Apache Airflow :**

    ![Gambar Install Apache Airflow with Terminal](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/05_install-airflow-apache-with-terminal.png?raw=true)

    **Sebelumnya perlu mendownload ubuntu terlebih dahulu jika melakukan penginstalan di windows, setelah itu penggunaan pip sebagai proses install apache airflow.**

    ![Gambar Insialisasi Database](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/06_inisialisasi-database.png?raw=true)

    **Selanjutnya kita perlu melakukan inisialisasi database terlebih dahulu dan pembuatan akun yang akan digunakan nantinya saat login di home DAG Airflow.**

    ![Gambar Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/07_sukses-install-scheduler.png?raw=true)

    ![Gambar Jalankan Airflow Webserver](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/08_sukses-install-webserver.png?raw=true)

    **Lalu jalankan airflow scheduler dan webserver sebagai awalan untuk mengakses home dagsnya.**

    ![Gambar Masuk ke Localhost](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/09_masuk-ke-webserver-localhost-8080.png?raw=true)

    **Setelah berhasil menjalankan airflownya sekarang bisa masuk ke localhost:8080**

    ![Gambar Login to Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/10_login-to-airflow.png?raw=true)

    **Silahkan login terlebih dahulu dengan menggunakan akun yang sudah dibuat tadi**

    ![Gambar Dags berhasil diakses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/11_DAGS-success-akses.png?raw=true)

    **Tampilan akan berubah ke halaman utama dags, bertanda bahwa home dags berhasil diakses dengan menampilkan beberapa dags default.**

**Penerapan DAG Ekstraksi Data API:**

- **Import Library yang diperlukan:**

    ![Gambar Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/12_import-library.png?raw=true)

    **Import beberapa library yang diperlukan disini saya menggunakan python operator.**

- **Code function Ekstrak books:**

    ![Gambar function Ekstrak books](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/13_Code-function-extract_books.png?raw=true)

    **Fungsi extract_books() yang didefinisikan di atas bertujuan untuk mengambil data dari URL yang diberikan, mengekstraksi informasi buku yang relevan dari respons JSON, dan mencetaknya dalam bentuk list.**

- **Code Inisialisasi DAG:**

    ![Gambar Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/14_Code-insialisasi-dag.png?raw=true)

    **Code tersebut mendefinisikan sebuah Directed Acyclic Graph (DAG) menggunakan Apache Airflow, yang disebut "extract_books_dag". DAG ini dirancang untuk mengekstrak data buku yang relevan dari suatu API secara terjadwal. Dengan demikian, DAG ini akan dijalankan secara terjadwal pada hari Senin pukul 09:00 untuk mengekstrak data buku yang relevan dari suatu API menggunakan konfigurasi yang telah ditentukan. Proses penentuan schedule_interval tersebut menggunakan cron expression**

- **Code Eksekusi Task:**

    ![Gambar Eksekusi Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/15_Code-eksekusi-task.png?raw=true)

    **Dalam kode tersebut, mendefinisikan sebuah task dalam DAG yang disebut extract_books_task. Task ini menggunakan operator PythonOperator, yang memungkinkan untuk menjalankan fungsi Python di dalam DAG.**

- **Jalankan Airflow:**

    ![Gambar Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/16_jalankan-airflow.png?raw=true)

    ![Gambar Jalankan Airflow Webserver](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/17_jalankan-airflow2.png?raw=true)

    **Lalu jalankan airflow menggunakan perintah seperti diatas**

- **Running DAG Success**

    ![Gambar Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/18_running-dag-success.png?raw=true)

    **Terlihat bahwa running dag success dengan menampilkan graph task yang sukses.**

- **Penjadwalan eksekusi setiap senin 09.00**

    ![Gambar Penjadwalan eksekusi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/19_penjadwalan-9.png?raw=true)

    ![Gambar Penjadwalan eksekusi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/20_penjadwalan-9-1.png?raw=true)

- **Hasil Logs Task**

    ![Gambar Hasil Logs Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Eksplorasi/21_logs-task-extract-books.png?raw=true)

    **Terlihat marking task a success, dengan menampilkan info pengambilan data dari API seperti judul, pengarang, tahun_terbit, genre. Dengan pengambilan data sesuai schedule setiap senin 09.00**