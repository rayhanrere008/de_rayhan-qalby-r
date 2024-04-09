from datetime import datetime, timedelta
import requests

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# URL koneksi PostgreSQL
connection_url = "postgresql://postgres:mypassword@localhost:5500/postgres"

def create_fruit_table():
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS fruits (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(255),
            calories DECIMAL,
            fat DECIMAL,
            sugar DECIMAL,
            carbohydrates DECIMAL,
            protein DECIMAL
        );
    """
    return create_table_sql


def get_fruit_data_from_api():
    endpoint = "https://www.fruityvice.com/api/fruit/family/Rosaceae"
    response = requests.get(endpoint)
    return response.json()


def insert_into_fruit_table(**kwargs):
    ti = kwargs['ti']
    fruit_data = ti.xcom_pull(task_ids='get_data_from_api')
    pg_hook = PostgresHook(postgres_conn_id='postgres_db')
    with pg_hook.get_conn() as conn:
        with conn.cursor() as cur:
            for fruit in fruit_data:
                fruit_values = (
                    fruit['name'],
                    fruit['nutritions']['calories'],
                    fruit['nutritions']['fat'],
                    fruit['nutritions']['sugar'],
                    fruit['nutritions']['carbohydrates'],
                    fruit['nutritions']['protein']
                )
                # Check if the fruit already exists in the table
                cur.execute("SELECT 1 FROM fruits WHERE name = %s", (fruit['name'],))
                existing_data = cur.fetchone()
                if not existing_data:
                    # Insert the fruit data if it doesn't already exist
                    insert_sql = """
                        INSERT INTO fruits (name, calories, fat, sugar, carbohydrates, protein)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cur.execute(insert_sql, fruit_values)
        conn.commit()

default_args = {
    "owner": "rayhan",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
        dag_id="fruit_data_dag",
        default_args=default_args,
        description="A DAG to fetch fruit data from API and insert into PostgreSQL",
        start_date=datetime(2024, 1, 4, 2),
        schedule_interval="@daily",
) as dag:
    create_table_task = PostgresOperator(
        task_id='create_fruit_table',
        postgres_conn_id='postgres_db',
        sql=create_fruit_table(),
        dag=dag,
    )

    get_data_task = PythonOperator(
        task_id='get_data_from_api',
        python_callable=get_fruit_data_from_api,
        dag=dag,
    )

    insert_task = PythonOperator(
        task_id='insert_into_fruit_table',
        python_callable=insert_into_fruit_table,
        provide_context=True,
        dag=dag,
    )

    create_table_task >> get_data_task >> insert_task
