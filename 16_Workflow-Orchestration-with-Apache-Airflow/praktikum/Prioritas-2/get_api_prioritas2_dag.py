from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import csv
import os

def get_data_from_api():
    # Placeholder for actual API call
    return [
        {'id': 1, 'title': 'Product 1', 'description': 'Description 1', 'category': 'Category 1', 'image': 'image1.jpg', 'rating': 4.5, 'count': 10},
        {'id': 2, 'title': 'Product 2', 'description': 'Description 2', 'category': 'Category 2', 'image': 'image2.jpg', 'rating': 3.8, 'count': 20}
    ]

def write_to_csv(response):
    response_dict = eval(response)  # Ubah string menjadi dictionary
    with open('/home/sapphire/data/api_data.csv', 'w', newline='') as csvfile:
        fieldnames = response_dict[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in response_dict:
            writer.writerow(item)

def write_to_txt(response):
    response_dict = eval(response)  # Ubah string menjadi dictionary
    with open('/home/sapphire/data/api_data.txt', 'w') as txtfile:
        for item in response_dict:
            txtfile.write(f"ID: {item['id']}, Title: {item['title']}, Description: {item['description']}, Category: {item['category']}, Image: {item['image']}, Rating: {item['rating']}")
            if 'count' in item:  # Periksa keberadaan kunci 'count'
                txtfile.write(f", Count: {item['count']}")
            txtfile.write("\n")


def print_done():
    print("done!")

default_args = {
    "owner":"rayhan",
    "retries":2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="api_data_prioritas2_dags",
    default_args=default_args,
    description="DAG to retrieve data from API and write to CSV and TXT files",
    start_date=datetime(2024, 1, 4, 2),
    schedule_interval="@daily",
) as dag:

    get_api_data = SimpleHttpOperator(
        task_id='get_api_data',
        method='GET',
        http_conn_id='fakestore_api_conn',  # Sesuaikan dengan koneksi HTTP yang telah Anda konfigurasi
        endpoint='/products',
        response_filter=lambda response: response.json()
    )

    write_to_csv_task = PythonOperator(
        task_id='write_to_csv',
        python_callable=write_to_csv,
        op_kwargs={'response': '{{ task_instance.xcom_pull(task_ids="get_api_data") }}'}
    )

    write_to_txt_task = PythonOperator(
        task_id='write_to_txt',
        python_callable=write_to_txt,
        op_kwargs={'response': '{{ task_instance.xcom_pull(task_ids="get_api_data") }}'}
    )

    print_done_task = BashOperator(
        task_id='print_done',
        bash_command='echo done!'
    )

    # Define task dependencies
    get_api_data >> [write_to_csv_task, write_to_txt_task] >> print_done_task
