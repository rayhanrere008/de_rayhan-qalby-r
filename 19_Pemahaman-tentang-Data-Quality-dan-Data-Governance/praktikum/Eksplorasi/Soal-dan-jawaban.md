## Soal dan Jawaban Eksplorasi - Data Quality dan Data Governance

1. Lakukan proses data cleaning pada sebuah workflow yang diilustrasikan sebagai berikut:

    ![Workflow Soal](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/01_workflow-soal.png?raw=true)

    Kriteria yang harus dipenuhi:

    - Menggunakan Apache Airflow dalam menyusun DAG berdasarkan workflow diatas.
    - Menggunakan API [endpoint](https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json) berikut.
    - Jenis Operator yang digunakan bebas / bisa disesuaikan.
    - Mengubah format nomor telepon dengan awalan +62 di depan. Contohnya seperti ini: +6281234567891
    - Mengubah nilai transaksi (transaction_amount) dengan format seperti berikut: Rp 12.000
    - Pastikan data yang diambil adalah data transaksi dengan status sama dengan success.
    - Proses data cleaning dapat menggunakan library Pandas.
    - Hasil akhir data cleaning disimpan di dalam DataFrame.

**Jawaban :**

- **Install dan Import Library yang diperlukan (airflow, pandas, requests):**

    ![Install dan Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/02_Install-dan-import-library.png?raw=true)

- **Code function get_data_from_api:**

    ![Code function get_data_from_api](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/03_Code-function-get_data_api.png?raw=true)

    **Fungsi get_data_from_api() tersebut bertujuan untuk mengambil data dari suatu API. Data yang diambil adalah data transaksi.**

- **Code function clean_data:**

    ![Code function clean_data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/04_Code-function-clean_data.png?raw=true)

    **Dengan langkah-langkah tersebut, fungsi ini membersihkan data transaksi yang telah diambil dari API, mengubah format nomor telepon dan nilai transaksi, serta memfilter hanya transaksi yang berhasil sebelum mencetaknya.**

- **Code Insialisasi DAG:**

    ![Code Insialisasi DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/05_Code-insialisasi-DAG.png?raw=true)

    **Code tersebut digunakan untuk menginisialisasi sebuah DAG yang akan dibuat seperti dag_id, default_args, deskripsi dag tersebut, dag akan dimulai, dan interval waktu eksekusi DAG.**

- **Code Eksekusi setiap Task:**

    ![Code Eksekusi setiap Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/06_Code-eksekusi-setiap-task.png?raw=true)

    **get_data_task: Ini adalah tugas yang menggunakan PythonOperator untuk menjalankan fungsi get_data_from_api(). Tugas ini bertujuan untuk mengambil data dari API. clean_data_task: Ini adalah tugas yang menggunakan PythonOperator untuk menjalankan fungsi clean_data(). Tugas ini bertujuan untuk membersihkan data yang telah diambil dari API. provide_context=True digunakan untuk memberikan akses ke konteks eksekusi (seperti informasi tentang tugas lainnya).**

- **Code Urutan eksekusi task:**

    ![Code Urutan eksekusi task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/07_Urutan-eksekusi-task.png?raw=true)

    **Dengan dependensi ini, Apache Airflow akan memastikan bahwa clean_data_task tidak akan dijalankan sampai get_data_task berhasil menyelesaikan eksekusinya. Ini membantu dalam memastikan bahwa data yang diperlukan untuk membersihkan data sudah tersedia sebelum proses pembersihan dimulai.**

- **Jalankan Airflow Scheduler dan Webserver:**

    ![Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/08_Jalankan-airflow.png?raw=true)

    ![Jalankan Airflow Webserver](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/09_Jalankan-airflow2.png?raw=true)

- **Running DAG Success:**

    ![Running DAG Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/10_Running-dag-success.png?raw=true)

    ![Running DAG Sukses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/11_Running-dag-success2.png?raw=true)

    **Terlihat bahwa DAG sukses dieksekusi dengan menampilkan graph setiap task berwarna hijau menandakan bahwa semua task berhasil dieksekusi dengan baik.**

- **Hasil Task 1 get_data_API:**

    ![Hasil Task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/12_Logs-task1-get_data_API.png?raw=true)

    **Terlihat pada logs bahwa marking task a success dengan mengembalikan nilai untuk memgambil data dari API nya.**

- **Hasil Task 2 clean_data:**

    ![Hasil Task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Eksplorasi/13_Logs-task2-clean_data.png?raw=true)

    **Terlihat pada logs bahwa marking task a success dengan mengembalikan nilai untuk menampilkan dataframe nya sesuai dengan hasil cleaningnya seperti Mengubah format nomor telepon dengan awalan +62 di depan, Mengubah nilai transaksi (transaction_amount) dengan format yang telah ditentukan, dan memfilter data dengan status success.**