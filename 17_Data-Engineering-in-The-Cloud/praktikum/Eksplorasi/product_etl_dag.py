from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import requests
import os
from firebase_admin import credentials, storage, initialize_app

# Inisialisasi Firebase Admin SDK
def initialize_firebase_app(service_account_path):
    cred = credentials.Certificate(service_account_path)
    initialize_app(cred)

# Fungsi untuk mengambil data dari API
def extract_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data_json = response.json()
    return data_json

# Fungsi untuk transformasi data
def transform_data(data):
    # Membuat DataFrame dari data JSON
    df = pd.DataFrame(data)

    # Memfilter produk dengan harga di atas 100
    df = df[df['price'] > 100]

    # Memilih kolom yang diperlukan
    df = df[['title', 'price', 'description', 'category']]

    return df

# Fungsi untuk memuat data ke Firebase Storage dalam format Parquet
def load_data_to_firebase_storage(**kwargs):
    bucket_name = kwargs.get('bucket_name')
    file_name = kwargs.get('file_name')
    df = kwargs.get('ti').xcom_pull(task_ids='transform_data')
    
    bucket = storage.bucket(bucket_name)
    df.to_parquet(file_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)


# Definisi default arguments
default_args = {
    "owner":"rayhan",
    "retries":1,
    "retry_delay": timedelta(minutes=1),
}

# Lokasi file service account Firebase
service_account_path = "/home/sapphire/airflow/accountKey.json"

# Inisialisasi Firebase App di awal skrip DAG
initialize_firebase_app(service_account_path)

# Inisialisasi DAG
with DAG(
    dag_id="product_pipeline_dag",
    default_args=default_args,
    description="A DAG to extract data, transform data, and load to firebase storage",
    start_date=datetime(2024, 1, 4, 2),
    schedule_interval="@daily",
) as dag:

    # Task untuk ekstrak data
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        dag=dag,
    )

    # Task untuk transformasi data
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_args=[extract_task.output],
        dag=dag,
    )

    # Task untuk memuat data ke Firebase Storage dalam format Parquet
    load_task = PythonOperator(
        task_id='load_data_to_storage',
        python_callable=load_data_to_firebase_storage,
        op_kwargs={'bucket_name': 'explore-de-rayhan.appspot.com', 'file_name': 'output_product.parquet'},
        provide_context=True,  # Memberikan akses ke informasi konteks
        dag=dag,
    )

# Definisi dependency antar task
extract_task >> transform_task >> load_task