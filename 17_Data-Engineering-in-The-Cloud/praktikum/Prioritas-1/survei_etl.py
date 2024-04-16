import pandas as pd
import firebase_admin
from firebase_admin import credentials, storage

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate("C:/code/de_rayhan-qalby-r/17_Data-Engineering-in-The-Cloud/praktikum/Prioritas-1/accountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'explore-de-rayhan.appspot.com'
})

# Fungsi untuk ekstraksi data dari file CSV
def extract_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Fungsi untuk transformasi data (data cleaning)
def transform_data(data):
    # Hapus data duplikat
    data = data.drop_duplicates()
    # Hapus baris yang memiliki nilai NULL
    data = data.dropna()
    return data

# Fungsi untuk memuat data ke Firebase Storage dalam format CSV
def load_data_to_firebase_storage(data, file_name):
    # Referensi ke bucket Firebase Storage
    bucket = storage.bucket()
    # Mengonversi DataFrame ke string CSV
    csv_data = data.to_csv(index=False)
    # Membuat blob di Firebase Storage
    blob = bucket.blob(file_name)
    # Mengunggah data CSV ke Firebase Storage
    blob.upload_from_string(csv_data)

# Main function
def main():
    # Lokasi file CSV
    file_path = "C:/code/de_rayhan-qalby-r/17_Data-Engineering-in-The-Cloud/praktikum/Prioritas-1/survey.csv"
    # Nama file untuk disimpan di Firebase Storage
    file_name = "output_survey.csv"

    # Ekstraksi data
    data = extract_data(file_path)
    # Transformasi data
    transformed_data = transform_data(data)
    # Memuat data ke Firebase Storage
    load_data_to_firebase_storage(transformed_data, file_name)

    # Memberikan pesan bahwa proses telah berhasil
    print("Data has been successfully processed and uploaded to Firebase Storage.")
    
if __name__ == "__main__":
    main()