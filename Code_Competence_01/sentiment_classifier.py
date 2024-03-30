import pandas as pd
import os

class SentimentClassifier:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None

    def load_data(self):
        print("Memuat dataset...")
        self.data = pd.read_csv(self.dataset_path)
        print("Dataset dimuat.")

    def classify_sentiment(self):
        if self.data is None:
            raise ValueError("Data belum dimuat. Panggil metode load_data() terlebih dahulu.")
        
        print("Melakukan klasifikasi sentimen...")
        # Implementasi klasifikasi sentimen
        self.data['sentiment'] = self.data['labels'].apply(self.classify_label)
        print("Klasifikasi sentimen selesai.")

    def classify_label(self, label):
        if label == 'good':
            return 'good'
        elif label == 'bad':
            return 'bad'
        else:
            return 'neutral'

    def save_to_csv(self):
        if self.data is None:
            raise ValueError("Data belum dimuat. Panggil metode load_data() terlebih dahulu.")
        
        print("Menyimpan hasil ke dalam file CSV...")
        # Memisahkan data berdasarkan kategori sentimen
        good_tweets = self.data[self.data['sentiment'] == 'good']
        bad_tweets = self.data[self.data['sentiment'] == 'bad']
        neutral_tweets = self.data[self.data['sentiment'] == 'neutral']

        # Menyimpan data ke dalam file CSV terpisah
        good_tweets.to_csv('sentiment_good.csv', index=False)
        bad_tweets.to_csv('sentiment_bad.csv', index=False)
        neutral_tweets.to_csv('sentiment_neutral.csv', index=False)

        print("Hasil disimpan dalam file CSV.")

    def summarize_counts(self):
        if self.data is None:
            raise ValueError("Data belum dimuat. Panggil metode load_data() terlebih dahulu.")
        
        print("Menghitung jumlah tweet untuk masing-masing kategori sentimen...")
        # Hitung jumlah tweet untuk setiap kategori sentimen
        sentiment_counts = self.data['sentiment'].value_counts()

        # Simpan hasil perhitungan ke dalam file CSV
        sentiment_counts.to_csv('sentiment_counts.csv')
        print("Jumlah tweet untuk masing-masing kategori sentimen telah dihitung.")

# Jika file ini dijalankan sebagai skrip utama
if __name__ == "__main__":
    # Path dataset
    dataset_path = 'data_source/file.csv'

    # Inisialisasi objek SentimentClassifier
    classifier = SentimentClassifier(dataset_path)

    # Memuat data
    classifier.load_data()

    # Melakukan klasifikasi sentimen
    classifier.classify_sentiment()

    # Menyimpan hasil ke dalam file CSV
    classifier.save_to_csv()

    # Menghitung jumlah tweet untuk masing-masing kategori sentimen
    classifier.summarize_counts()
