## Soal Prioritas 2 dan Jawaban - Workflow Orchestration with Apache Airflow

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

    ![Gambar Soal Workflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/01_workflow_soal.png?raw=true)

Kriteria yang harus dipenuhi:

- Task pertama bertujuan untuk mendapatkan data dari API. Berikut adalah endpoint API yang digunakan: https://fakestoreapi.com/products 
- Task kedua bertujuan untuk menulis hasil dari response API ke dalam file CSV
- Task ketiga bertujuan untuk menulis hasil dari response API ke dalam file txt.
- Task terakhir bertujuan untuk menampilkan pesan “done!” untuk menyatakan tugas telah selesai.
- Gunakan Operator berdasarkan jenis task yang dijalankan.

**Jawaban :**

- **Persiapkan filenya terlebih dahulu (Import Library)**

    ![Gambar Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/02_import-library.png?raw=true)

- **Code function task get_data_from_api():**

    ![Gambar Code Function get data api](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/03_Code-function-task-get-api-data.png?raw=true)

    **Fungsi ini mensimulasikan pengambilan data dari sebuah API, walaupun pada kenyataannya, ia hanya mengembalikan daftar yang telah ditentukan sebelumnya dalam bentuk dictionary. Setiap dictionary dalam daftar tersebut merepresentasikan informasi tentang sebuah produk, termasuk id, title, description, category, image, rating, dan count.**
 
 - **Code function task write_to_csv:**

    ![Gambar Code Function write_to_csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/04_Code-function-task-write_to_csv.png?raw=true)

    **Fungsi ini pada dasarnya akan mengonversi respons API yang diberikan dalam format string menjadi dictionary, kemudian menulisnya ke dalam file CSV dengan menggunakan modul csv bawaan dari Python.**

 - **Code function task write_to_txt:**

    ![Gambar Code Function write_to_txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/05_Code-function-task-write_to_txt.png?raw=true)

    **Fungsi ini menghasilkan file teks yang berisi informasi produk dari respons API dengan format yang sesuai dengan keterangan yang dijelaskan dalam kode.**

 - **Code function task print_done:**

    ![Gambar Code Function print_done](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/06_Code-function-task-print_done.png?raw=true)

    **Fungsi print_done() sederhana, ia hanya mencetak pesan "done!" ke konsol saat dipanggil. Ini berguna untuk memberi tahu bahwa suatu tugas atau proses telah selesai.**

 - **Code Inisialisasi DAG:**

    ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/07_Code-inisialisasi-dag.png?raw=true)

    **Ini adalah kerangka dasar yang biasa digunakan dalam Airflow untuk mendefinisikan DAG.**

 - **Code Eksekusi Setiap Task:**

    ![Gambar Code Eksekusi Setiap Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/08_Code-eksekusi-setiap-task.png?raw=true)

    **get_api_data: Ini adalah sebuah task yang menggunakan SimpleHttpOperator untuk melakukan permintaan HTTP GET ke endpoint '/products' pada koneksi HTTP yang telah dikonfigurasi sebelumnya. write_to_csv_task: Task ini menggunakan PythonOperator untuk menjalankan fungsi write_to_csv yang telah definisikan sebelumnya. write_to_txt_task: Task ini juga menggunakan PythonOperator untuk menjalankan fungsi write_to_txt yang telah definisikan. print_done_task: Task ini adalah BashOperator yang cukup sederhana. Ia hanya mencetak pesan "done!" ke konsol saat dieksekusi.**

 - **Code Urutan Eksekusi Task:**

    ![Gambar Code Urutan Eksekusi Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/09_Code-urutan-eksekusi-task.png?raw=true)

    **Ini menunjukkan bahwa get_api_data harus selesai sebelum write_to_csv_task dan write_to_txt_task dimulai, dan kedua task tersebut harus selesai sebelum print_done_task dimulai.**

 - **Membuat koneksi konfigurasi API**

    ![Gambar koneksi konfigurasi API](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/10_membuat_koneksi_API.png?raw=true)

 - **Jalankan Airflow**

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/11_jalankan_airflow.png?raw=true)

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/12_jalankan_airflow2.png?raw=true)

 - **Running DAG Sukses**

    ![Gambar Running DAG Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/13_running-dag-success.png?raw=true)

    **Terlihat bahwa alur grahpnya sesuai, semua task berhasil dieksekusi**

 - **Hasil logs task 1 get_api_data**

    ![Gambar Hasil logs task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/14_logs-task1-get_api_data.png?raw=true)

 - **Hasil logs task 2 write_to_txt**

    ![Gambar Hasil logs task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/15_logs-task2-write_to_txt.png?raw=true)

- **Hasil logs task 3 write_to_csv**

    ![Gambar Hasil logs task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/16_logs-task3-write_to_csv.png?raw=true)

- **Hasil logs task 4 print_done**

    ![Gambar Hasil logs task 4](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/17_logs-task4-print_done.png?raw=true)

    **Terlihat marking task success dengan menghasilkan output : done!**

- **Isi File api_data.csv**

    ![Gambar Isi File api_data.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/18_isi-file-api_data.csv.png?raw=true)

- **Isi File api_data.txt**

    ![Gambar Isi File api_data.txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-2/19_isi-file-api_data.txt.png?raw=true)