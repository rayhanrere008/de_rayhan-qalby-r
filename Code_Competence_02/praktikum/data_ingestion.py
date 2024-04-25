import pandas as pd
import os

class DataLakeBuilder:
    def read_csv_data(self, file_path):
        # Metode untuk membaca data dari file CSV
        return pd.read_csv(file_path)

    def handle_missing_values(self, df):
        # Metode untuk menangani missing values dalam DataFrame
        return df.fillna(method='ffill')

    def handle_outliers(self, df, column):
        # Menggunakan teknik IQR untuk menangani outliers
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df.loc[df[column] < lower_bound, column] = lower_bound
        df.loc[df[column] > upper_bound, column] = upper_bound
        return df

    def save_to_parquet(self, df, file_name):
        # Memastikan folder data_lake ada
        data_lake_folder = "data_lake"
        if not os.path.exists(data_lake_folder):
            os.makedirs(data_lake_folder)
        # Menyimpan DataFrame ke file Parquet di dalam folder data_lake
        file_path = os.path.join(data_lake_folder, file_name)
        df.to_parquet(file_path)
        print(f"Saved {file_name} to {file_path}")

    def read_parquet_data(self, file_path):
        # Metode untuk membaca data dari file Parquet
        return pd.read_parquet(file_path)

    def validate_data(self, file_path):
        # Metode untuk memvalidasi data dalam file Parquet
        df = self.read_parquet_data(file_path)
        
        # Menampilkan ringkasan statistik
        print("Summary Statistics:")
        print(df.describe())
        
        # Menampilkan beberapa baris awal data
        print("\nFirst few rows of data:")
        print(df.head())

# Persiapan Lingkungan Pengembangan
# Mendapatkan path ke folder data_source
folder_path = "data_source"

# Memastikan folder data_source ada
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Membuat instance dari DataLakeBuilder
builder = DataLakeBuilder()

# Memuat dataset dari file CSV ke dalam DataFrame
events_df = builder.read_csv_data(os.path.join(folder_path, "events.csv"))
customers_df = builder.read_csv_data(os.path.join(folder_path, "customers.csv"))
tickets_df = builder.read_csv_data(os.path.join(folder_path, "tickets.csv"))
transactions_df = builder.read_csv_data(os.path.join(folder_path, "transactions.csv"))
customer_feedback_df = builder.read_csv_data(os.path.join(folder_path, "customer_feedback.csv"))

# Menangani outliers dalam kolom 'price' dari file 'tickets.csv'
tickets_df = builder.handle_outliers(tickets_df, 'price')

# Menyimpan DataFrame ke format Parquet
builder.save_to_parquet(events_df, "events.parquet")
builder.save_to_parquet(customers_df, "customers.parquet")
builder.save_to_parquet(tickets_df, "tickets.parquet")
builder.save_to_parquet(transactions_df, "transactions.parquet")
builder.save_to_parquet(customer_feedback_df, "customer_feedback.parquet")

# Validasi Data
builder.validate_data("data_lake/events.parquet")
builder.validate_data("data_lake/customers.parquet")
builder.validate_data("data_lake/tickets.parquet")
builder.validate_data("data_lake/transactions.parquet")
builder.validate_data("data_lake/customer_feedback.parquet")