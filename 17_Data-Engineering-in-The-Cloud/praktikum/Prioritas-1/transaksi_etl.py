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
    # Filter data berdasarkan metode pembayaran kartu kredit (credit card) dan status success
    transformed_data = data[(data['payment_method'] == 'credit card') & (data['status'] == 'success')]
    return transformed_data

# Fungsi untuk memuat data ke Firebase Storage dalam format CSV
def load_data_to_firebase_storage(data, bucket_name, file_name):
    # Konversi DataFrame ke string CSV
    csv_data = data.to_csv(index=False)

    # Inisialisasi bucket Firebase Storage
    bucket = storage.bucket(bucket_name)

    # Upload data ke Firebase Storage
    blob = bucket.blob(file_name)
    blob.upload_from_string(csv_data)

    print(f"Data has been successfully loaded to Firebase Storage with filename: {file_name}")

if __name__ == "__main__":
    # URL data transaksi
    url = "https://gist.githubusercontent.com/nadirbslmh/8fc9cc6cd5cbaaf5cbff63b090fb497e/raw/a7bf3e1edab88b04314a40a9de3ed744bc86d0e9/ecommerce.json"

    # Nama file untuk disimpan di Firebase Storage
    file_name = "output_transactions.csv"

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

    # Memuat data ke Firebase Storage
    load_data_to_firebase_storage(transformed_data, bucket_name, file_name)
