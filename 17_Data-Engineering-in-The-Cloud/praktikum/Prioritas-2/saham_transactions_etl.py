import pandas as pd
import firebase_admin
from firebase_admin import credentials, storage
import requests

# Inisialisasi Firebase Admin SDK
def initialize_firebase_app(service_account_path):
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

# Fungsi untuk ekstrak data dari sumber data
def extract_data(url):
    # Unduh data JSON dari URL
    response = requests.get(url)
    data_json = response.json()
    # Konversi data JSON menjadi DataFrame
    data = pd.DataFrame(data_json)
    return data

# Fungsi untuk transformasi data
def transform_data(data):
    # Filter data berdasarkan stock_symbol (GOOGL, AMZN, MSFT, dan AAPL)
    filtered_data = data[data['stock_symbol'].isin(['GOOGL', 'AMZN', 'MSFT', 'AAPL'])]
    # Ambil data transaksi saham dengan harga transaksi di atas 500
    transformed_data = filtered_data[filtered_data['trade_price'] > 500]
    return transformed_data

# Fungsi untuk memuat data ke Firebase Storage dalam format Parquet
def load_data_to_firebase_storage(data, bucket_name, file_name):
    # Inisialisasi bucket Firebase Storage
    bucket = storage.bucket(bucket_name)

    # Menyimpan data ke file Parquet
    data.to_parquet(file_name)

    # Upload file Parquet ke Firebase Storage
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)

    print(f"Data has been successfully loaded to Firebase Storage with filename: {file_name}")

if __name__ == "__main__":
    # URL data transaksi saham
    url = "https://gist.githubusercontent.com/nadirbslmh/93b62fdcfa694d4ec07bed9b3c94e401/raw/c07971341361e23fd4f3a880437c4d8e4ebcfafc/stock_trades.json"

    # Nama file untuk disimpan di Firebase Storage
    file_name = "output_transactions_saham.parquet"

    # Nama bucket Firebase Storage
    bucket_name = "explore-de-rayhan.appspot.com"

    # Lokasi file service account
    service_account_path = "C:/code/de_rayhan-qalby-r/17_Data-Engineering-in-The-Cloud/praktikum/Prioritas-1/accountKey.json"

    # Inisialisasi Firebase App
    initialize_firebase_app(service_account_path)

    # Ekstraksi data dari sumber data
    data = extract_data(url)

    # Transformasi data
    transformed_data = transform_data(data)

    # Memuat data ke Firebase Storage dalam format Parquet
    load_data_to_firebase_storage(transformed_data, bucket_name, file_name)
