## Soal Prioritas 1 - Workflow Orchestration with Apache Airflow

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

    ![Gambar Soal Workflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/01_worfkflow_soal.png?raw=true)


Kriteria yang harus dipenuhi:

- Task pertama adalah membuat sekumpulan bilangan acak dari 1 sampai 50 dengan jumlah bilangan adalah 25 bilangan.
- Task kedua adalah menghitung jumlah dari semua bilangan yang didapatkan dari task pertama.
- Task terakhir adalah menentukan apakah jumlah dari semua bilangan merupakan bilangan genap atau bukan. Jika merupakan bilangan genap tampilkan tulisan “Even Sum”. Jika tidak maka tampilkan tulisan “Odd Sum”.
- Gunakan X-COM dalam proses pertukaran data antar task.
- Gunakan PythonOperator dalam membuat DAG.

**Jawaban :**

- **Persiapkan file terlebih dahulu (Import Library)**

    ![Gambar Code Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/02_import-library.png?raw=true)

- **Code function setiap task**

    ![Gambar Code Function Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/03_Code-function-task.png?raw=true)

    **generate_random_numbers(): Fungsi ini digunakan untuk menghasilkan 25 angka acak antara 1 dan 50, dan kemudian mengembalikan daftar angka tersebut. calculate_sum(* *context): Fungsi ini bertanggung jawab untuk mengambil hasil dari task generate_numbers, yang menghasilkan daftar angka acak, dan kemudian menjumlahkannya. Fungsi ini menggunakan XCom untuk mengambil data yang dihasilkan oleh task sebelumnya. check_even_sum ( * *context): Fungsi ini menerima konteks dan menggunakan XCom untuk mengambil hasil dari task sebelumnya, yaitu hasil penjumlahan yang dihasilkan oleh task calculate_sum.**

- **Code inisialisasi DAG**

    ![Gambar Code Inisialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/04_Code-inisialisasi-DAG.png?raw=true)

    **default_args: Ini adalah sebuah dictionary yang digunakan untuk menentukan default arguments untuk seluruh task dalam DAG. with DAG(): Ini adalah blok penutup (with) yang digunakan untuk mendefinisikan DAG.**

- **Code Eksekusi setiap task**

    ![Gambar Code Eksekusi task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/05_Code-eksekusi-task.png?raw=true)

    **generate_numbers_task: Ini adalah task yang bertanggung jawab untuk menjalankan fungsi generate_random_numbers(). calculate_sum_task: Ini adalah task yang bertanggung jawab untuk menjalankan fungsi calculate_sum(). check_even_task: Ini adalah task yang bertanggung jawab untuk menjalankan fungsi check_even_sum(). Setiap task menggunakan PythonOperator, yang memungkinkan untuk menjalankan fungsi Python yang telah definisikan sebelumnya sebagai bagian dari DAG.**

- **Code Urutan Eksekusi Task**

    ![Gambar Code Urutan Eksekusi task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/06_urutan-eksekusi-task.png?raw=true)

    **Ini akan memastikan bahwa calculate_sum_task akan dieksekusi setelah generate_numbers_task selesai, dan check_even_task akan dieksekusi setelah calculate_sum_task selesai.**

- **Jalankan Airflow**

    ![Gambar Jalankan Airflow](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/07_jalankan_airflow.png?raw=true)

- **Running DAG sukses**

    ![Gambar Running Dag Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/08_Running_dag_success.png?raw=true)

    **Terlihat running sukses dengan 3 task selesai dieksekusi**

- **Hasil logs task 1 generate_numbers**

    ![Gambar logs task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/09_logs_task1_generate_numbers.png?raw=true)

    **Terlihat pada logs marking task a sukses dengan menghasilkan angka [42, 33, 40, 2, 20, 44, 2, 31, 16, 29, 20, 16, 11, 35, 12, 39, 34, 28, 45, 9, 45, 43, 17, 26, 23]**

- **Hasil logs task 2 calculate_sum**

    ![Gambar logs task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/10_logs_task2_calculate_sum.png?raw=true)

    **Terlihat pada logs marking task a sukses menjumlahkan seluruh angka random sebelumnya dengan total = 662**

- **Hasil logs task 3 check_even**

    ![Gambar logs task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/16_Workflow-Orchestration-with-Apache-Airflow/screenshots/Prioritas-1/Soal_2/11_logs_task3_check_even.png?raw=true)

    **Terlihat pada logs marking task a sukses dengan mengklasifikasikan nilai 662 sebagai Even sum yaitu bilangan genap**
