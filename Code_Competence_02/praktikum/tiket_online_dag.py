from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from data_ingestion import DataLakeBuilder
from data_transformation import DataWarehouseLoader
import os

# Path ke folder data_source
data_source_folder = "/home/sapphire/data_source"

# Fungsi untuk menjalankan proses data ingestion
def perform_data_ingestion():
    builder = DataLakeBuilder()
    builder.save_to_parquet(builder.read_csv_data(os.path.join(data_source_folder, "events.csv")), "events.parquet")
    builder.save_to_parquet(builder.read_csv_data(os.path.join(data_source_folder, "customers.csv")), "customers.parquet")
    builder.save_to_parquet(builder.read_csv_data(os.path.join(data_source_folder, "tickets.csv")), "tickets.parquet")
    builder.save_to_parquet(builder.read_csv_data(os.path.join(data_source_folder, "transactions.csv")), "transactions.parquet")
    builder.save_to_parquet(builder.read_csv_data(os.path.join(data_source_folder, "customer_feedback.csv")), "customer_feedback.parquet")

# Fungsi untuk menjalankan proses data transformation
def perform_data_transformation():
    loader = DataWarehouseLoader()
    events_df = loader.load_data("data_lake/events.parquet")
    customers_df = loader.load_data("data_lake/customers.parquet")
    tickets_df = loader.load_data("data_lake/tickets.parquet")
    transactions_df = loader.load_data("data_lake/transactions.parquet")
    feedback_df = loader.load_data("data_lake/customer_feedback.parquet")
    tickets_sold_per_event, revenue_per_event, avg_rating_per_event = loader.transform_data(events_df, customers_df, tickets_df, transactions_df, feedback_df)
    return tickets_sold_per_event, revenue_per_event, avg_rating_per_event

# Fungsi untuk menjalankan proses loading data ke Data Warehouse
def perform_loading_data_to_warehouse(**kwargs):
    loader = DataWarehouseLoader()
    tickets_sold_per_event, revenue_per_event, avg_rating_per_event = kwargs['ti'].xcom_pull(task_ids='data_transformation')
    today_date_folder = datetime.now().strftime('%Y-%m-%d')
    loader.save_to_warehouse(tickets_sold_per_event, "Tickets_sold_per_event", today_date_folder)
    loader.save_to_warehouse(revenue_per_event, "Revenue_per_event", today_date_folder)
    loader.save_to_warehouse(avg_rating_per_event, "Feedback_analysis", today_date_folder)
    bucket_name = 'data-warehouse-rayhan'
    service_account_key_path = '/home/sapphire/airflow/project-data-engineer1-account.json'
    loader.upload_to_gcs(bucket_name, os.path.join('data_warehouse', today_date_folder, 'Tickets_sold_per_event.parquet'), 'Tickets_sold_per_event.parquet', service_account_key_path)
    loader.upload_to_gcs(bucket_name, os.path.join('data_warehouse', today_date_folder, 'Revenue_per_event.parquet'), 'Revenue_per_event.parquet', service_account_key_path)
    loader.upload_to_gcs(bucket_name, os.path.join('data_warehouse', today_date_folder, 'Feedback_analysis.parquet'), 'Feedback_analysis.parquet', service_account_key_path)

# Definisikan default argument
default_args = {
    "owner":"rayhan",
    "retries":1,
    "retry_delay": timedelta(minutes=1),
}

# Definisikan DAG
dag = DAG(
    'tiket_pipeline_dag',
    default_args=default_args,
    description='A DAG to automate data pipeline process',
    schedule_interval=timedelta(days=1), # Sekali sehari
    start_date=datetime(2024, 4, 24),
    catchup=False
)

# Definisikan task untuk data ingestion
data_ingestion_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=perform_data_ingestion,
    dag=dag
)

# Definisikan task untuk data transformation
data_transformation_task = PythonOperator(
    task_id='data_transformation',
    python_callable=perform_data_transformation,
    dag=dag
)

# Definisikan task untuk loading data ke Data Warehouse
loading_data_to_warehouse_task = PythonOperator(
    task_id='loading_data_to_warehouse',
    python_callable=perform_loading_data_to_warehouse,
    provide_context=True,  # Mengizinkan akses ke context Airflow seperti XCom
    dag=dag
)

# Atur dependencies antar task
data_ingestion_task >> data_transformation_task >> loading_data_to_warehouse_task
