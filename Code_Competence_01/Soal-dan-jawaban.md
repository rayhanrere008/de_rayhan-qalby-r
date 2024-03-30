## Soal dan Jawaban - Code Competence 01

Sistem untuk menganalisis sentimen dari tweets menggunakan dataset ChatGPT Sentiment Analysis dari Kaggle. Sistem akan memproses data dan mengkategorikan sentimen ke dalam tiga kategori: good, bad, danneutral. Data akan dipisahkan ke dalam tiga file CSV berdasarkan kategorinya dan jumlah data per kategori akan dihitung dan disimpan.

1. **Persiapan Lingkungan Pengembangan**
    - Buat virtual environment dengan Python dan namai sebagai venv_code untuk mengisolasi proyek.

        ![Gambar Create Venv venv_code](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/01_Buat-virtual-env-dan-aktifkan.png?raw=true)

    - Download dataset ChatGPT Sentiment Analysis dari tautan ini kemudian simpan kedalam folder data_source, yang terdiri dari atribut tweets sebagai teks tweet dan label yang merupakan penanda sentimen (good,bad,neutral).

        ![Gambar Download Dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/01_download-dataset-ChatGPT-Sentiment-Analysis.png?raw=true)

        ![Gambar Simpan Dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/01_simpan-di-folder-data_source.png?raw=true)

    - Install Library yang diperlukan (pandas, sqlalchemy, pymysql)

        ![Gambar Install Pandas](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/01_Install_library_pandas.png?raw=true)

        ![Gambar Install PymySQL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/01_Install_library_pymysql.png?raw=true)

        ![Gambar Install SQLAlchemy](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/01_Install_library_sqlalchemy.png?raw=true)

2. **Persiapan dan Pemrosesan Dataset dengan OOP**
    - Bangun class SentimentClassifier dalam Python didalam file sentiment_classifier.py yang memiliki metode untuk membaca dan memproses dataset.

        ![Gambar Code Create Class SentimentClassifier](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_Code-create-class-SentimentClassifier-1.png?raw=true)

    - Metode load_data() akan membaca dataset ke dalam struktur data yang sesuai.

        ![Gambar Code Metode Load data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_Code-metode-load_data-2.png?raw=true)

        **ketika metode load_data dipanggil pada sebuah objek dari kelas yang sesuai, ia akan mencetak pesan "Memuat dataset...", memuat dataset dari file CSV ke dalam atribut data objek tersebut, dan kemudian mencetak pesan "Dataset dimuat."**

    - Metode classify_sentiment() akan membagi tweets ke dalam kategori good, bad, atau neutral.

        ![Gambar Code Metode classify_sentiment()](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_Code-metode-classify_sentiment()-3.png?raw=true)

        **Metode classify_sentiment bertanggung jawab untuk mengklasifikasikan sentimen berdasarkan label yang ada dalam dataset. Metode classify_label adalah bagian dari proses klasifikasi yang sebenarnya, di mana label yang diberikan akan diklasifikasikan menjadi 'good', 'bad', atau 'neutral' berdasarkan kondisi yang ditetapkan.**

    - Metode save_to_csv() akan menyimpan tweets yang diklasifikasikan ke dalam file CSV terpisah: sentiment_good.csv, sentiment_bad.csv, dan sentiment_neutral.csv.

        ![Gambar Code Metode save_to_csv()](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_Code-metode-save_to_csv()-4.png?raw=true)

        **Metode save_to_csv dipanggil pada sebuah objek dari kelas yang sesuai, ia akan memisahkan data berdasarkan sentimen dan menyimpannya ke dalam tiga file CSV terpisah yaitu bad, good, dan neutral.**

        - Isi File sentiment_good.csv

            ![Gambar File sentiment_good.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_isi-file-sentiment_good.csv.png?raw=true)

        - Isi File sentiment_bad.csv

            ![Gambar File sentiment_bad.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_isi-file-sentiment_bad.csv.png?raw=true)

        - Isi File sentiment_neutral.csv

            ![Gambar File sentiment_neutral.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_isi-file-sentiment_neutral.csv.png?raw=true)

    - Hitung dan simpan jumlah tweets untuk masing-masing kategori sentimen ke dalam file sentiment_counts.csv menggunakan metode summarize_counts().

        ![Gambar Code Metode summarize_counts()](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_Code-metode-summarize_counts()-5.png?raw=true)

        **Metode summarize_counts dipanggil pada sebuah objek dari kelas yang sesuai, ia akan menghitung jumlah tweet untuk setiap kategori sentimen dalam dataset dan menyimpan hasil perhitungannya ke dalam file CSV.**

        - Isi File sentiment_counts.csv

            ![Gambar File sentiment_counts.csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_isi-file-sentiment_counts.csv.png?raw=true)
    
    - Code main sebelum dijalankan

        ![Gambar Code main](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_Code-main-6.png?raw=true)

        **Jika skrip ini dijalankan sebagai skrip utama (main script), langkah-langkah tersebut akan dieksekusi secara berurutan.**
        
    - Running code file sentiment_classifier.py sukses

        ![Gambar Running File](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/02_running-file-sentiment_classifier.py-success.png?raw=true)

3. **Penyimpanan Data**
    - Desain skema database dengan tabel yang saling berelasi:
        - tweets (id, text, sentiment_id)

            ![Gambar Code Skema table tweets](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_Code-skema-table-tweets-1.png?raw=true)

            **Dengan menggunakan definisi kelas ini, kita dapat membuat objek Tweet yang merepresentasikan entri dalam tabel 'tweets' dalam basis data, serta melakukan operasi CRUD (Create, Read, Update, Delete) pada entri tersebut menggunakan SQLAlchemy ORM.**

        - sentiments (sentiment_id, sentiment_label)

            ![Gambar Code Skema table sentiments](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_Code-skema-table-sentiments-2.png?raw=true)

            **Dengan menggunakan definisi kelas ini, kita dapat membuat objek Sentiment yang merepresentasikan entri dalam tabel 'sentiments' dalam basis data, serta melakukan operasi CRUD (Create, Read, Update, Delete) pada entri tersebut menggunakan SQLAlchemy ORM.**
        
        - Pastikan sentiment_id di tabel tweets merupakan foreign key yang merujuk ke sentiments.

            ![Gambar Struktur database](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_Struktur-database.png?raw=true)

    - Buat class Python DatabaseManager didalam file database_manager.py dengan library SQLAlchemy atau pymysql (jika menggunakan mysql) yang memiliki metode:
        - create_tables untuk mendefinisikan dan membuat tabel-tabel di atas jika belum ada.

            ![Gambar Code metode create_tables](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_Code-metode-create_tables-3.png?raw=true)

            **Kelas DatabaseManager menyediakan fungsionalitas untuk mengelola koneksi ke database, membuat tabel dalam database, serta membuat dan menggunakan sesi SQLAlchemy untuk berinteraksi dengan database.**

        - insert_from_csv untuk membaca data dari CSV dan menginsert-nya ke dalam database sesuai tabel yang relevan.

            ![Gambar Code metode insert_from_csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_Code-metode-insert_from_csv-4.png?raw=true)

            **Fungsi insert_from_csv ini secara efektif membaca data dari file CSV, mencari atau membuat entri baru untuk setiap sentimen yang ditemukan, dan kemudian memasukkan tweet beserta sentimennya ke dalam database.**

        - Dokumentasi masing-masing tabel hasil insert dalam bentuk screenshot
            - Isi tabel sentiments

                ![Gambar isi tabel sentiments](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_insert_table-sentiments.png?raw=true)

            - Isi tabel tweets

                ![Gambar isi tabel tweets](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_insert_table-tweets.png?raw=true)
    
    - Code main sebelum di running

        ![Gambar code main](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_Code-main.png?raw=true)

        **Jadi, jika skrip ini dijalankan, ia akan menginisialisasi koneksi ke database MySQL, membuat tabel-tabel yang diperlukan, dan kemudian memasukkan data dari file CSV ke dalam database untuk setiap kategori sentimen yang ada.**
    
    - Proses running code file database_manager.py sukses

        ![Gambar running file database_manager.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/03_running-file-database_manager.py-success.png?raw=true)

4. **Integrasi dengan Google Cloud Storage:**
    - Buat satu bucket di Google Cloud Storage, dengan nama sentiment_chatgpt_storage, untuk menyimpan semua file yang relevan:

        ![Gambar Create Bucket](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/04_create_bucket.png?raw=true)

        - sentiment_good.csv
        - sentiment_bad.csv
        - sentiment_neutral.csv
        - sentiment_counts.csv
        - Backup database sentiment_chatgpt.sql (kalau saya db_chatgpt.sql)

            ![Gambar Simpan file di bucket](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_01/screenshots/04_simpan-file-di-bucket.png?raw=true)