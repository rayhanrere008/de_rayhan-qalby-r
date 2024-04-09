from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
import os

# Tentukan jalur direktori yang diinginkan
base_directory = '/home/sapphire/data'

# Tentukan jalur lengkap ke direktori dan file yang diinginkan
about_us_directory = os.path.join(base_directory, 'about_us')
our_works_directory = os.path.join(base_directory, 'our_works')

default_args = {
    "owner":"rayhan",
    "retries":3,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="prioritas1_hello_dag",
    default_args=default_args,
    description="dag for create file and write text",
    start_date=datetime(2024, 1, 4, 2),
    schedule_interval="@daily",
) as dag:
    t1 = BashOperator(
        task_id='create_about_us_directory_and_file',
        bash_command=f"mkdir -p {about_us_directory} && echo 'hello airflow' >> {about_us_directory}/about.txt",
    dag=dag,
)

    t2 = BashOperator(
        task_id='create_our_works_directory_and_file',
        bash_command=f"mkdir -p {our_works_directory} && echo 'hello airflow' >> {our_works_directory}/works.txt",
    dag=dag,
)

    t3 = BashOperator(
        task_id='print_done',
        bash_command="echo 'done!'",
    dag=dag,
)

t1 >> t2 >> t3