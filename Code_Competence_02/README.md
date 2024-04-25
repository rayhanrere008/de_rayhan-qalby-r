## Tahapan

1. Buat Virtual Environtment "venv_code"
2. Install beberapa library yang diperlukan (pandas, apache-airflow, pyarrow, google cloud storage)
3. Download dataset di link yang disediakan
4. Simpan dataset di folder data_source
5. Buat file data_ingestion.py
6. Running file data_ingestion.py
7. Maka akan muncul beberapa file parquet yang tersimpan di folder data_lake
8. Setup Bucket di Google Cloud Storage
9. Buat Service Account di project GCP dalam bentuk file JSON
10. Buat file data_transformation.py
11. Running file data_transformation.py
12. Maka hasil file parquet transformation akan disimpan di Bucket GCP dan Folder data_warehouse di lokal.

Otomatisasi Workflow DAG Airflow
1. Buat file tiket_online_dag.py
2. Masukkan file tersebut ke Dags direktori
3. Masukkan file data_ingestion.py dan data_transformation.py ke Dags direktori
4. Pastikan keberadaan folder data_source
5. Pastikan keberadaan direktori service account
6. Jalankan Airflow
7. Pantau pada Localhost:8080
8. Jika sukses maka akan menyimpan file parquet hasil transformasi ke Google Cloud Storage dan Direktori lokal (data_warehouse)