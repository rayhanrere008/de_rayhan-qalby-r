## Soal Eksplorasi dan Jawaban - Data Transformation

![Gambar Ilustrasi Workflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_workflow.png?raw=true)

1. Implementasi Airflow untuk Automasi Workflow:
    - Pengaturan Airflow:
        - Instalasi dan konfigurasi Apache Airflow.

            ![Gambar Install Apache Airflow with Terminal](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_install-airflow-apache-with-terminal.png?raw=true)

            ![Gambar Inisialiasi Database Konfigurasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_inisialisasi-database.png?raw=true)

            ![Gambar Login to Localhost](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_login-to-airflow.png?raw=true)

        - Buat DAG (Directed Acyclic Graph) untuk mengatur workflow analisis data.

            ![Gambar Workflow DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_workflow-DAG.png?raw=true)
    
    - Install Library pandas, matplotlib, kaggle, seaborn, openpyxl, pyarrow  di terminal:

        ![Gambar Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_install_library.png?raw=true)

    - Inisialisasi DAG:

        ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_code_inisialisasi_DAG.png?raw=true)

        **Jadi, keseluruhan code tersebut adalah untuk mendefinisikan default arguments dan menginisialisasi sebuah DAG dengan menggunakan Apache Airflow. DAG ini dapat digunakan untuk membangun workflow untuk analisis data**
    
    - Import Library:

        ![Gambar Code Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_code_import_library.png?raw=true)

    - Task 1 - Ekstraksi Data:
        - Gunakan Python operator di Airflow untuk mengimpor dataset bebas dari repository seperti kaggle atau lainnya

            ![Gambar Dataset yang digunakan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_dataset_yang_diimpor.png?raw=true)

            ![Gambar Code Ekstraksi Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_code_task1_ekstrak_data.png?raw=true)

            **Fungsi download_dataset() yang diberikan bertujuan untuk mengunduh dataset dari Kaggle. Untuk menggunakan kode ini, pastikan telah menginstal pustaka Kaggle Python API dan memiliki akun Kaggle yang terdaftar. Dan juga harus memiliki file konfigurasi Kaggle API (biasanya berupa file JSON) yang berisi kunci API Anda. Selain itu, pastikan juga bahwa telah mengatur jalur yang valid untuk menyimpan dataset di lokasi yang ditentukan.**
        
        - Hasil logs task 1 - ekstraksi data:

            ![Gambar Logs Task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_logs_task1_ekstrak_data.png?raw=true)

    - Task 2 - Transformasi Data dengan Pandas:
        - Lakukan transformasi data (normalisasi, encoding, handling missing values, dll.) menggunakan Pandas.

            ![Gambar Code Transformasi data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_code_task2_transform_data.png?raw=true)

            **Fungsi ini menghasilkan DataFrame yang telah ditransformasi sesuai dengan kriteria yang ditetapkan, yaitu data yang memiliki nilai 'lunch' yang sama dengan 'standard'.**
        
        - Hasil logs task 2 - tranformasi data

            ![Gambar Logs task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/01_logs_task2_transform_data.png?raw=true)

2. Ekspor Data ke Excel:
    - Task 3 - Ekspor Hasil Analisis:

        ![Gambar Code Ekspor data ke excel](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/02_code_task3_export_to_excel.png?raw=true)

        **Fungsi ini akan menghasilkan file Excel baru yang berisi data yang telah ditransformasi sesuai dengan proses yang didefinisikan dalam fungsi transform_data(). Pastikan direktori /home/sapphire/data/ telah tersedia dan memiliki izin untuk menulis ke dalamnya..**

        - Gunakan Pandas untuk mengekspor hasil analisis ke file Excel.

            ![Gambar Hasil Analisis](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/02_hasil-transformasi-export-to-excel.png?raw=true)

        - Atur task ini di Airflow untuk otomatisasi proses ekspor (logs).

            ![Gambar logs task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/02_logs_task3_export_to_excel.png?raw=true)

3. Visualisasi Data:
    - Task 4 - Visualisasi Data:

        ![Gambar Code Visualisasi Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/03_code_task4_visualize_data.png?raw=true)

        **Fungsi visualize_data() yang diberikan bertujuan untuk membuat visualisasi data dari DataFrame yang sudah ditransformasi. Fungsi ini akan menghasilkan histogram dari kolom 'lunch' dan menyimpannya sebagai file gambar PNG di lokasi yang ditentukan. Pastikan direktori /home/sapphire/data/ telah tersedia dan memiliki izin untuk menulis ke dalamnya.**

        - Buat visualisasi data menggunakan library seperti Matplotlib atau Seaborn.
            - Menggunakan library tersebut dalam proses pembuatannya
        - Integrasikan pembuatan visualisasi ini dalam workflow Airflow(logs).

            ![Gambar logs task 4](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/03_logs_task4_visualize_data.png?raw=true)
        
        - Hasil Output Visualisasi:

            ![Gambar Output Visualisasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/03_visualization.png?raw=true)

4. Proses Eksekusi dan Menjalankan DAG di Airflow
    - Code eksekusi setiap task:

        ![Gambar Code Eksekusi setiap Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/04_code_eksekusi_task.png?raw=true)

        **Dengan mendefinisikan task-task ini, maka telah membuat alur kerja (workflow) yang berisi langkah-langkah untuk ekstraksi, transformasi, ekspor, dan visualisasi data, yang akan dieksekusi secara otomatis sesuai dengan jadwal yang telah ditetapkan (dalam hal ini, setiap hari).**
    
    - Jalankan Airflow:

        ![Gambar Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/04_jalankan_airflow_scheduler.png?raw=true)

        ![Gambar Jalankan Airflow Webserver](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/04_jalankan_airflow_webserver.png?raw=true)
    
    - Running DAG Success:

        ![Gambar Running DAG Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/04_running_dags_success.png?raw=true)

        ![Gambar Running DAG Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Eksplorasi/04_running_dags_success2.png?raw=true)
    