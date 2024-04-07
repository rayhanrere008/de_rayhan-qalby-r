from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kaggle

# Fungsi untuk mengunduh dataset dari Kaggle
def download_dataset():
    kaggle.api.dataset_download_files("bhavikjikadara/student-study-performance", path="C:/code/de_rayhan-qalby-r/15_Data-Transformation/praktikum/Eksplorasi", unzip=True)

# Fungsi untuk melakukan transformasi data menggunakan Pandas
def transform_data():
    # Baca dataset
    df = pd.read_csv('C:/code/de_rayhan-qalby-r/15_Data-Transformation/praktikum/Eksplorasi/study_performance.csv')

    # Lakukan transformasi data
    # Filter data berdasarkan kolom 'lunch' yang memiliki keterangan 'standard'
    filtered_data = df[df['lunch'].isin(['standard'])]

    return filtered_data

# Fungsi untuk mengekspor data ke file Excel
def export_to_excel():
    # Panggil fungsi transform_data untuk mendapatkan dataframe yang sudah ditransformasi
    transformed_data = transform_data()

    # Ekspor data ke file Excel
    transformed_data.to_excel('/home/sapphire/data/transformed_data.xlsx', index=False)

# Fungsi untuk membuat visualisasi data
def visualize_data():
    # Panggil fungsi transform_data untuk mendapatkan dataframe yang sudah ditransformasi
    transformed_data = transform_data()

    # Buat visualisasi data menggunakan Matplotlib atau Seaborn
    plt.figure(figsize=(10, 6))
    sns.histplot(data=transformed_data, x='lunch', kde=True)
    plt.title('Histogram of Lunch Before Test')
    plt.xlabel('Lunch')
    plt.ylabel('Frequency')
    plt.savefig('/home/sapphire/data/visualization.png')
    plt.close()

# Definisikan default arguments
default_args = {
    'owner': 'rayhan',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Inisialisasi DAG
dag = DAG(
    'data_analysis_workflow',
    default_args=default_args,
    description='Workflow untuk analisis data',
    schedule_interval='@daily',
)

# Task 1 - Ekstraksi Data
extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=download_dataset,
    dag=dag,
)

# Task 2 - Transformasi Data
transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

# Task 3 - Ekspor Data ke Excel
export_to_excel_task = PythonOperator(
    task_id='export_to_excel',
    python_callable=export_to_excel,
    dag=dag,
)

# Task 4 - Visualisasi Data
visualize_data_task = PythonOperator(
    task_id='visualize_data',
    python_callable=visualize_data,
    dag=dag,
)

# Atur ketergantungan antar task
extract_data_task >> transform_data_task >> export_to_excel_task >> visualize_data_task