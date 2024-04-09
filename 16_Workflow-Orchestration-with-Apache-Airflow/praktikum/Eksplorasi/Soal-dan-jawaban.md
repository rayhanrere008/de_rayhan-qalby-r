## Soal Eksplorasi dan Jawaban - Workflow Orchestration with Apache Airflow

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

    ![Gambar Soal Workflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/01_alur_workflow.png?raw=true)


Kriteria yang harus dipenuhi:

- Task pertama bertujuan untuk membuat tabel dengan nama fruits untuk menyimpan data buah-buahan.
- Task kedua bertujuan untuk mendapatkan data dari API. Endpoint API yang digunakan adalah sebagai berikut: https://www.fruityvice.com/api/fruit/family/Rosaceae 
- Task ketiga bertujuan untuk memasukkan data buah-buahan ke dalam tabel fruits yang sudah dibuat.
- Gunakan Operator berdasarkan jenis task yang dijalankan.

**Jawaban :**

- **Install Library yang diperlukan (requests):**

    ![Gambar Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/02_Install-library.png?raw=true)

- **Code Import Library:**

    ![Gambar Code Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/03_Code-import-library.png?raw=true)

    **Sebelumnya lakukan juga penginstalan package: pip install apache-airflow-providers-postgres**

- **Code Function create_fruit_table():**

    ![Gambar Code Function create_fruit_table()](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/04_Code-function-create_fruit_table.png?raw=true)

    **Jadi, keseluruhan fungsi ini bertujuan untuk memudahkan pembuatan tabel "fruits" dengan skema yang telah ditentukan di dalam database. Seperti id: Kolom ini bertipe BIGSERIAL, name: Kolom ini bertipe VARCHAR(255), calories, fat, sugar, carbohydrates, protein: Kelima kolom ini bertipe DECIMAL**

- **Code Function get_fruit_data_from_api():**

    ![Gambar Code Function get_fruit_data_from_api()](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/05_Code-function-get_fruit_data_from_api.png?raw=true)

    **Jadi, keseluruhan fungsi ini bertujuan untuk mengambil data buah dari API yang diberikan**

- **Code Function insert_into_fruit_table():**

    ![Gambar Code Function insert_into_fruit_table()](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/06_Code-function-insert_into_fruit_table.png?raw=true)

    **Fungsi insert_into_fruit_table(* *kwargs) bertujuan untuk menyisipkan data buah yang diperoleh dari sebuah API ke dalam tabel "fruits" di dalam database PostgreSQL. Pertama, fungsi ini mengambil data buah dari XCom menggunakan ti.xcom_pull(task_ids='get_data_from_api'). Selanjutnya, fungsi ini membuat koneksi ke database PostgreSQL menggunakan PostgresHook(postgres_conn_id='postgres_db'). Fungsi ini melakukan iterasi melalui setiap buah dalam fruit_data. Fungsi memeriksa apakah data buah tersebut sudah ada di dalam tabel "fruits" dengan menjalankan perintah SQL SELECT 1 FROM fruits WHERE name = %s dengan menggunakan nama buah sebagai parameter. Jika tidak ada data yang ditemukan, existing_data akan bernilai None. Jika data buah tersebut belum ada di dalam tabel, maka fungsi akan menyisipkan data tersebut ke dalam tabel "fruits" menggunakan perintah SQL INSERT INTO ... VALUES ....Setelah semua data buah ditambahkan ke dalam database, transaksi akan di-commit dengan conn.commit().**

- **Code Inisialisasi DAG:**

    ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/07_Code-inisialisasi-DAG.png?raw=true)

    **Dengan definisi ini, DAG bernama "fruit_data_dag" akan dijalankan setiap hari dan akan mencoba menjalankan tugas-tugas yang telah didefinisikan di dalamnya menggunakan argumen default yang telah ditentukan.**

- **Code Eksekusi Task:**

    ![Gambar Code Eksekusi Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/08_Code-eksekusi-task.png?raw=true)

    **create_table_task: Ini adalah sebuah PostgresOperator yang bertujuan untuk membuat tabel "fruits" di dalam database PostgreSQL. get_data_task: Ini adalah sebuah PythonOperator yang bertujuan untuk mengambil data buah dari sebuah API. insert_task: Ini adalah sebuah PythonOperator yang bertujuan untuk menyisipkan data buah ke dalam tabel "fruits" di dalam database PostgreSQL.**

- **Code Urutan Eksekusi Task:**

    ![Gambar Code  Urutan Eksekusi Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/09_Code-urutan-eksekusi-task.png?raw=true)

    **Dengan urutan dependency ini, DAG akan memastikan bahwa langkah-langkah dijalankan sesuai dengan urutan yang diinginkan, yaitu membuat tabel terlebih dahulu, kemudian mengambil data dari API, dan akhirnya menyisipkan data tersebut ke dalam tabel yang baru dibuat.**

- **Membuat koneksi postgre di Airflow:**

    ![Gambar Membuat koneksi postgre](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/10_membuat-koneksi-postgre-di-airflow.png?raw=true)

    **Disini saya membuat koneksi baru bernama postgre_db dengan tipe koneksi Postgre. selain itu memiliki keterangan host : localhost, database : postgres, login(username) : postgres, password : mypassword, dan port 5500.**

- **Jalankan Airflow:**

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/11_jalankan_airflow.png?raw=true)

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/12_jalankan_airflow2.png?raw=true)

- **Running DAG Success:**

    ![Gambar Running DAG Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/13_running-dag-success.png?raw=true)

    **Terlihat bahwa DAG berhasil dijalankan dengan sesuai alur workflow nya dan setiap task berhasil dieksekusi dengan sukses.**

- **Hasil Logs Task 1 create_fruit_table:**

    ![Gambar Logs Task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/14_logs-task1-create_fruit_table.png?raw=true)

    **Terlihat pada logs bahwa marking task success dengan mengembalikan pembuatan table fruits dengan kolom yang sudah ditentukan.**

- **Hasil Logs Task 2 get_dat_from_api:**

    ![Gambar Logs Task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/15_logs-task2-get_dat_from_api.png?raw=true)

    **Terlihat pada logs bahwa marking task a success dengan mengembalikan nilai done dengan keterangan mengambil data yang ada di dalam API.**

- **Hasil Logs Task 3 insert_into_fruit_table:**

    ![Gambar Logs Task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/16_logs-task3-insert_into_fruit_table.png?raw=true)

    **Terlihat pada logs bahwa marking task a success dengan mengembalikan nilai done.**

- **Table fruits created:**

    ![Gambar Table fruits created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/17_table_fruits_created.png?raw=true)

    ![Gambar Deskripsi Table](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/18_desc_table_fruits.png?raw=true)

- **Isi table fruits setelah proses insert**

    ![Gambar Isi table fruits](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/19_isi_table_fruits.png?raw=true)

    ![Gambar Isi table fruits](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Eksplorasi/20_isi_table_fruits2.png?raw=true)

    **Terlihat bahwa data dari API berhasil diinsert ke dalam table fruits dengan total 11 data yang masuk sesuai dengan data yang ada dalam API**