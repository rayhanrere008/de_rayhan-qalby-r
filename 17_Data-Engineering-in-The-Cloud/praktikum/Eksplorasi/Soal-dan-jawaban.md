## Soal dan Jawaban Eksplorasi - Data Engineering in The Cloud

1. Buatlah sebuah pipeline ETL berdasarkan skema berikut:

    ![Workflow Soal](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/01_workflow_soal.png?raw=true)

    Kriteria dari pipeline ETL yang dibuat adalah sebagai berikut:

    - Data sampel yang digunakan adalah sebuah API dengan endpoint: https://fakestoreapi.com/products 
    - Menggunakan Apache Airflow dalam membangun pipeline ETL.
    - Terdapat proses ekstrak data dari API.
    - Terdapat proses transformasi data yaitu:
        - Mengambil data produk dengan harga diatas 100.
        - Menyimpan data produk berupa nama (title), harga (price), deskripsi (description) dan kategori (category).
    - Terdapat proses load data yang sudah ditransform dalam format parquet ke dalam Google Storage.

**Keterangan :**
- Sudah menginstall Apache Airflow
- Masih menggunakan service account dan storage yang sama(firebase)

**Jawaban :**

- **Install library yang diperlukan (pandas, requests, firebase admin):**

    ![Install library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/02_install-library-firebase-admin.png?raw=true)

- **Code Inisialisasi Firebase:**

    ![Gambar Code Inisialisasi Firebase](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/03_Code-inisialisasi-firebase.png?raw=true)

    ![Gambar Code Inisialisasi Firebase](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/04_Code-inisialisasi-firebase2.png?raw=true)

    **Kode diatas adalah mencoba untuk menginisialisasi Firebase Admin SDK di dalam skrip Apache Airflow menggunakan fungsi initialize_firebase_app(service_account_path).**

- **Code Function Ekstrak data:**

    ![Gambar Code Function Ekstrak data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/05_Code-function-ekstrak_data.png?raw=true)

    **Fungsi extract_data() bertugas untuk mengambil data dari sebuah API menggunakan permintaan HTTP GET dan mengembalikan respons dalam format JSON.**

- **Code Function Transform data:**

    ![Gambar Code Function Ekstrak data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/06_Code-function-transform_data.png?raw=true)

    **Fungsi transform_data(data) bertugas untuk melakukan transformasi data pada data JSON yang diberikan. Dengan Memfilter Produk dengan Harga di Atas 100 dan hanya kolom-kolom 'title', 'price', 'description', dan 'category' yang dipertahankan.**

- **Code Function load_data_to_firebase_storage:**

    ![Gambar Code Function load_data_to_firebase_storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/07_Code-function-load-data-to-firebase-storage.png?raw=true)

    **Fungsi load_data_to_firebase_storage(kwargs) bertanggung jawab untuk memuat data ke Firebase Storage dalam format Parquet. Fungsi ini dirancang untuk digunakan dalam skrip Apache Airflow dan menerima argumen berupa bucket_name, file_name, dan hasil dari operasi transformasi data menggunakan XCom.**

- **Code Inisialisasi DAG:**

    ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/08_Code-inisialisasi-dag.png?raw=true)

    ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/09_Code-inisialisasi-dag2.png?raw=true)

    **Dengan pengaturan ini, DAG siap untuk digunakan dalam skrip Apache Airflow dan akan berjalan setiap hari, mengeksekusi langkah-langkah yang didefinisikan di dalamnya.**

- **Code Eksekusi Semua Task:**

    ![Gambar Code Eksekusi Semua Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/10_Code-eksekuksi-semua-task.png?raw=true)

    **extract_task: Tugas ini bertanggung jawab untuk mengekstrak data menggunakan fungsi extract_data. Ini menggunakan PythonOperator yang akan mengeksekusi fungsi extract_data. transform_task: Tugas ini melakukan transformasi data menggunakan fungsi transform_data. Ini juga menggunakan PythonOperator, tetapi dalam kasus ini, tugas ini memiliki dependensi pada tugas extract_task. Artinya, tugas ini akan menunggu sampai tugas extract_task selesai sebelum memulai eksekusi. load_task: Tugas ini bertugas memuat data ke Firebase Storage dalam format Parquet menggunakan fungsi load_data_to_firebase_storage. Ini juga menggunakan PythonOperator dan memiliki dependensi pada tugas transform_task. Selain itu, tugas ini menggunakan op_kwargs untuk menyediakan argumen tambahan ke fungsi yang akan dipanggil.**

- **Code Urutan Eksekusi Task:**

    ![Gambar Code Urutan Eksekusi Semua Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/11_Code-urutan-eksekusi-task.png?raw=true)

    **Dengan konfigurasi ini, tugas-tugas dalam DAG akan dieksekusi secara berurutan: pertama extract_task, kemudian transform_task, dan terakhir load_task, membentuk alur kerja yang jelas dan terstruktur untuk menjalankan operasi ekstraksi, transformasi, dan pemuatan data.**

- **Jalankan Airflow Scheduler dan Webserver:**

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/12_jalankan-airflow.png?raw=true)

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/13_jalankan-airflow2.png?raw=true)

- **Running DAG Success:**

    ![Gambar Running DAG Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/14_running-dag-success.png?raw=true)

    **Terlihat bahwa DAG berjalan dengan sukses dengan mengeksekusi seluruh task (warna hijau).**

- **Hasil Logs Task 1 extract_data:**

    ![Gambar Hasil Logs Task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/15_logs-task1-extract_data.png?raw=true)

    **Terlihat pada logs Marking task a success dengan mengembalikan nilai untuk mengambil data yang ada pada API.**

- **Hasil Logs Task 2 transform_data:**

    ![Gambar Hasil Logs Task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/16_logs-task2-transform_data.png?raw=true)

    **Terlihat pada logs Marking task a success dengan mengembalikan nilai untuk mengambil data dengan kriteria yang telah ditentukan (harga diatas 100 dan mengambil data pada kolom 'title', 'price', 'description', dan 'category') yang ada pada API.**

- **Hasil Logs Task 3 load_data_to_storage:**

    ![Gambar Hasil Logs Task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/17_logs-task3-load_data_to_storage.png?raw=true)

    **Terlihat pada logs Marking task a success menandakan bahwa output akan di load ke storage firebase.**

- **Load ke storage firebase berhasil:**

    ![Gambar Load ke storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/18_berhasil-load-ke-storage.png?raw=true)

    **Terlihat pada storage bucket firebase terdapat file output_product.parquet yang berhasil di load.**

- **Load ke storage firebase berhasil:**

    ![Gambar Load ke storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/18_berhasil-load-ke-storage.png?raw=true)

    **Terlihat pada storage bucket firebase terdapat file output_product.parquet yang berhasil di load.**

- **Isi file output_product.parquet yang telah diekstrak ke csv:**

    ![Gambar Isi file output_product.parquet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/19_isi-file-output_product.csv-(diekstrak-dari-file-parquet).png?raw=true)

    ![Gambar Isi file output_product.parquet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Eksplorasi/20_isi-file-output_product.csv-(diekstrak-dari-file-parquet)2.png?raw=true)

    **Terlihat pada isi file tersebut menampilkan data pada beberapa kolom yang telah ditentukan yaitu 'title', 'price', 'description', dan 'category' dengan ketentuan price > 100.**
