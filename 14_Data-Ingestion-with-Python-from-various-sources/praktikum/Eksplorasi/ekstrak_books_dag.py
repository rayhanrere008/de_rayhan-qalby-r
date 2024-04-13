from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def extract_books():
    import requests
    url = "https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json"
    response = requests.get(url)
    data = response.json()
    relevant_books = []
    for book in data['data']:
        relevant_books.append({
            'judul': book['title'],
            'pengarang': book['author'],
            'tahun_terbit': book['year'],
            'genre': book['genre']
        })
    print(relevant_books)

default_args = {
    "owner":"rayhan",
    "retries":2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
        dag_id="extract_books_dag",
        default_args=default_args,
        description="A DAG to extract relevant books data from an API",
        start_date=datetime(2024, 1, 4, 2),
        schedule_interval='0 9 * * 1',  # Run every Monday at 09:00
) as dag:

    extract_books_task = PythonOperator(
        task_id='extract_books_task',
        python_callable=extract_books,
        dag=dag,
    )

extract_books_task
