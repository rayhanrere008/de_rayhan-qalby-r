## Soal Prioritas 1 - Workflow Orchestration with Apache Airflow

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

    ![Gambar Soal Workflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/01_Workflow-Soal.png?raw=true)

Catatan:
- Satu task menggambarkan perintah bash yang harus dijalankan.
- Gunakan BashOperator dalam membuat DAG.

**Jawaban :**

- **Persiapkan file dags code nya terlebih dahulu (import library)**

    ![Gambar Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/02_Code-import-library.png?raw=true)

- **Code untuk menentukan tempat penyimpanan direktori about_us dan our_works**

    ![Gambar Tempat Direktori](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/03_Code-tentukan-direktori-penyimpanan.png?raw=true)

    **Di dalam code tersebut, terdapat dua variabel yang digunakan untuk menyimpan jalur direktori. Jalur direktori tersebut dibangun menggunakan fungsi os.path.join(), yang menggabungkan jalur-jalur yang diberikan menjadi satu jalur yang lengkap. Dengan menggunakan os.path.join(), code tersebut dapat bekerja secara platform-independent, artinya dapat berjalan dengan baik di berbagai sistem operasi tanpa perlu khawatir tentang tanda pemisah direktori yang berbeda (seperti / di Linux dan \ di Windows).**

- **Code untuk inisialisasi DAG**

    ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/04_Code-inisialisasi-dag.png?raw=true)

    **Seluruh code tersebut adalah kerangka awal (Pendefinisian Default Arguments dan Pendefinisian DAG) untuk membuat sebuah DAG dengan Apache Airflow, dimana selanjutnya akan didefinisikan task-task yang akan dieksekusi dalam DAG tersebut.**

- **Code untuk Eksekusi Setiap Task**

    ![Gambar Code Eksekusi TASK](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/05_Code-eksekusi-setiap-task.png?raw=true)

    **Task 1 - create_about_us_directory_and_file: Task ini merupakan BashOperator yang bertugas untuk membuat sebuah direktori dengan nama about_us dan sebuah file about.txt di dalamnya. Task 2 - create_our_works_directory_and_file: Task ini juga merupakan BashOperator yang bertugas untuk membuat sebuah direktori dengan nama our_works dan sebuah file works.txt di dalamnya. Task 3 - print_done: Task ini sederhana, bertugas untuk mencetak teks 'done!'**

- **Code untuk urutan eksekusi task**

    ![Gambar Code Urutan Eksekusi TASK](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/06_Urutan-eksekusi-task.png?raw=true)

    **Eksekusi task dilakukan dari task 1 > task 2 > task 3**

- **Jalankan Airflow**

    ![Gambar Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/07_Jalankan-airflow.png?raw=true)

    ![Gambar Jalankan Airflow Webserver](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/08_Jalankan-airflow2.png?raw=true)

- **Running DAG Success**

    ![Gambar Running Dag Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/12_running_dag_success.png?raw=true)

    **Terlihat di GRAPHnya setiap task dieksekusi semua dan sukses**

- **Hasil Logs Semua Task**

    ![Gambar Logs Task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/09_logs_task1_about_us.png?raw=true)

    ![Gambar Logs Task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/10_logs-task2-our_works.png?raw=true)

    ![Gambar Logs Task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/11_logs-task3-print_done.png?raw=true)

    **Terlihat pesan mencetak 'done!'**

- **Direktori About_us dan Our_works telah dibuat**

    ![Gambar Direktori Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/13_direktori-telah-dibuat.png?raw=true)

- **File about.txt created**

    ![Gambar About.txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/14_isi-file-about.png?raw=true)

    **Terlihat pesan untuk mencetak tulisan hello airflow**

- **File works.txt created**

    ![Gambar works.txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_1/15_isi-file-works.png?raw=true)

    **Terlihat pesan untuk mencetak tulisan hello airflow**