from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd

def get_data_from_api():
    # Get data from API
    api_url = "https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json"
    response = requests.get(api_url)
    data = response.json()
    return data

def clean_data(**kwargs):
    # Ekstrak data dari instance task
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='get_data_from_api')

    # Konversi data ke DataFrame
    df = pd.DataFrame(data)

    # Ubah format nomor telepon dengan awalan +62
    df['phone_number'] = '+62' + df['phone_number'].astype(str).str[1:]

    # Ubah format nilai transaksi menjadi "Rp 12.000" dengan tanda titik sebagai pemisah ribuan
    df['transaction_amount'] = df['transaction_amount'].map(lambda x: 'Rp {:,.0f}'.format(x).replace(',', '.'))

    # Filter data berdasarkan status transaksi success
    df = df[df['transaction_status'] == 'success']

    # Print data yang telah dibersihkan
    print(df)

default_args = {
    "owner":"rayhan",
    "retries":2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
        dag_id="data_cleaning_workflow",
        default_args=default_args,
        description="A DAG to perform data cleaning from API",
        start_date=datetime(2024, 4, 19),
        schedule_interval="@daily",
) as dag:

    # Define tasks
    get_data_task = PythonOperator(
        task_id='get_data_from_api',
        python_callable=get_data_from_api,
        dag=dag,
    )

    clean_data_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
        provide_context=True,
        dag=dag,
    )

# Set task dependencies
get_data_task >> clean_data_task
