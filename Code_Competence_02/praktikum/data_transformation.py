import pandas as pd
from google.cloud import storage
import os

class DataWarehouseLoader:
    def load_data(self, file_path):
        # Metode untuk membaca data dari Data Lake (format Parquet).
        return pd.read_parquet(file_path)

    def transform_data(self, events_df, customers_df, tickets_df, transactions_df, feedback_df):

        # Menggabungkan tabel transactions dengan tickets berdasarkan ticket_id
        merged_df = pd.merge(transactions_df, tickets_df, on='ticket_id')

        # Menggabungkan hasilnya dengan DataFrame feedback_df menggunakan kolom 'transaction_id'
        feedback_analysis = pd.merge(feedback_df, merged_df, on='transaction_id')

        # Kemudian gabungkan dengan events berdasarkan event_id
        feedback_analysis = pd.merge(feedback_analysis, events_df, on='event_id')

        # Analisis rating rata-rata per acara
        avg_rating_per_event = feedback_analysis.groupby('event_id').agg({'rating': 'mean'}).reset_index()

        # Menghitung jumlah tiket yang terjual per acara
        tickets_sold_per_event = merged_df.groupby('event_id').agg({'quantity': 'sum'}).reset_index()

        # Menghitung total pendapatan dari setiap acara
        revenue_per_event = merged_df.groupby('event_id').agg({'total_amount': 'sum'}).reset_index()

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event
    
    def save_to_warehouse(self, df, table_name, date_folder):
        # Metode untuk menyimpan data ke Data Warehouse.
        # Path untuk menyimpan file dalam folder berdasarkan tanggal
        folder_path = os.path.join('data_warehouse', date_folder)
        os.makedirs(folder_path, exist_ok=True)

        # Path lengkap untuk menyimpan file dalam format Parquet
        file_path = os.path.join(folder_path, f"{table_name}.parquet")

        # Simpan DataFrame ke format Parquet
        df.to_parquet(file_path, index=False)

    def upload_to_gcs(self, bucket_name, file_path, destination_blob_name, service_account_key_path):
        # Metode untuk mengunggah file ke Google Cloud Storage.
        # Inisialisasi client Google Cloud Storage dengan menggunakan kunci JSON
        storage_client = storage.Client.from_service_account_json(service_account_key_path)

        # Mengunggah file ke Google Cloud Storage
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(file_path)
        print(f"File '{destination_blob_name}' berhasil diunggah ke Google Cloud Storage.")

# Path ke folder data_lake
data_lake_folder = "data_lake"

# Membuat instance dari DataWarehouseLoader
loader = DataWarehouseLoader()

# Memuat data dari Data Lake
events_df = loader.load_data(os.path.join(data_lake_folder, "events.parquet"))
customers_df = loader.load_data(os.path.join(data_lake_folder, "customers.parquet"))
tickets_df = loader.load_data(os.path.join(data_lake_folder, "tickets.parquet"))
transactions_df = loader.load_data(os.path.join(data_lake_folder, "transactions.parquet"))
feedback_df = loader.load_data(os.path.join(data_lake_folder, "customer_feedback.parquet"))

# Melakukan transformasi data
tickets_sold_per_event, revenue_per_event, avg_rating_per_event = loader.transform_data(events_df, customers_df, tickets_df, transactions_df, feedback_df)

# Simpan hasil transformasi ke Data Warehouse dengan struktur folder berdasarkan tanggal
today_date_folder = pd.to_datetime('today').strftime('%Y-%m-%d')
loader.save_to_warehouse(tickets_sold_per_event, "Tickets_sold_per_event", today_date_folder)
loader.save_to_warehouse(revenue_per_event, "Revenue_per_event", today_date_folder)
loader.save_to_warehouse(avg_rating_per_event, "Feedback_analysis", today_date_folder)

# Upload file ke Google Cloud Storage
bucket_name = 'data-warehouse-rayhan'
service_account_key_path = 'C:/code/de_rayhan-qalby-r/Code_Competence_02/praktikum/project-data-engineer1-account.json'
loader.upload_to_gcs(bucket_name, os.path.join('data_warehouse', today_date_folder, 'Tickets_sold_per_event.parquet'), 'Tickets_sold_per_event.parquet', service_account_key_path)
loader.upload_to_gcs(bucket_name, os.path.join('data_warehouse', today_date_folder, 'Revenue_per_event.parquet'), 'Revenue_per_event.parquet', service_account_key_path)
loader.upload_to_gcs(bucket_name, os.path.join('data_warehouse', today_date_folder, 'Feedback_analysis.parquet'), 'Feedback_analysis.parquet', service_account_key_path)