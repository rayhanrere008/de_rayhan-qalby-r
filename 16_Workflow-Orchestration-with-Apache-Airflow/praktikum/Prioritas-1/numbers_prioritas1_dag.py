from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import random

from datetime import datetime, timedelta

def generate_random_numbers():
    random_numbers = [random.randint(1, 50) for _ in range(25)]
    return random_numbers

def calculate_sum(**context):
    numbers = context['ti'].xcom_pull(task_ids='generate_numbers')
    return sum(numbers)

def check_even_sum(**context):
    sum_result = context['ti'].xcom_pull(task_ids='calculate_sum')
    if sum_result % 2 == 0:
        return "Even Sum"
    else:
        return "Odd Sum"

default_args = {
    "owner":"rayhan",
    "retries":1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="random_number_dag",
    default_args=default_args,
    description="A DAG to generate random numbers, calculate their sum, and check if the sum is even",
    start_date=datetime(2024, 1, 4, 2),
    schedule_interval="@daily",
) as dag:

    generate_numbers_task = PythonOperator(
        task_id='generate_numbers',
        python_callable=generate_random_numbers,
    )

    calculate_sum_task = PythonOperator(
        task_id='calculate_sum',
        python_callable=calculate_sum,
    )

    check_even_task = PythonOperator(
        task_id='check_even',
        python_callable=check_even_sum,
    )

generate_numbers_task >> calculate_sum_task >> check_even_task
