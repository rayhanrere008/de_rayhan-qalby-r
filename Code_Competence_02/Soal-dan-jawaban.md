## Data Engineer Code Competance 2

🎯 Objective

Peserta mampu mengembangkan alur kerja data untuk Sistem Penjualan Tiket Online, mengotomatisasi proses dari pengambilan data hingga analisis dengan Python dan Apache Airflow, dan membangun Data Warehouse serta Data Lake untuk mendukung pengambilan keputusan bisnis yang berdasarkan data.

📝 Task

![Gambar Alur Task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/0_Soal-alur-task.png?raw=true)

1. **Persiapan Lingkungan Pengembangan**
    - **Gunakan virtual environment venv_code yang telah ada. Modifikasi environment ini untuk memasukkan dependencies baru yang diperlukan, seperti library pandas, airflow, dan library lain yang diperlukan.**

        ![Gambar Buat Virtual Env](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/1-01_Buat-virtual-environtment.png?raw=true)

        **Membuat virtual env dengan nama venv_code, lalu mengaktifkannya.**

        ![Gambar Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/1-02_Install-library-yang-diperlukan.png?raw=true)
        
        ![Gambar Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/1-05_Install-library-yang-diperlukan.png?raw=true)

        **Install library yang diperlukan seperti pandas, apache-airflow, pyarrow.**

    - **Update requirements.txt untuk mencerminkan perubahan tersebut.**

        ![Gambar Update requirements.txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/1-03_Update-requirements.txt.png?raw=true)

        **Melakukan update pada file requirements.txt dengan library yang baru ditambahkan.**

    - **Download dataset dan kemudian simpan kedalam folder data_source**

        ![Gambar Download dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/1-04_Download-dataset-save-to-data_source.png?raw=true)

        **Download dataset pada link yang disediakan, lalu simpan ke dalam folder data_source isi dataset tersebut ada customer_feedback.csv, customers.csv, events.csv, tickets.csv, transactions.csv.**

    - **Struktur file csv**

        ![Gambar Struktur File CSV](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/0_Soal-struktur-file-csv.png?raw=true)
    
2. **Data Ingestion dan Persiapan Data Lake / Data Werehouse**
    - **Penyiapan Skrip Python**
        - Buat file Python dengan nama data_ingestion.py.

            ![Gambar Buat file Python data_ingestion.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-01_Buat-file-data_ingestion.py.png?raw=true)

        - Dalam file ini, buat kelas dengan nama DataLakeBuilder.

            ![Gambar kelas dengan nama DataLakeBuilder](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-02_Buat-class-DataLakeBuilder.png?raw=true)

        - Kelas DataLakeBuilder

            **Ada Class DataLakeBuilder.**

        - Kelas ini harus memiliki metode untuk membaca data dari file CSV, menangani missing values dan outliers, dan menyimpan data ke format yang sesuai untuk Data Lake.

            **Ada Class DataLakeBuilder ini memiliki metode seperti yang disebutkan.**

        - read_csv_data(self, file_path): Metode untuk membaca data dari file CSV.

            **Ada class ini memiliki metode read_csv_data untuk melakukan read data dari file csv.**

        - handle_missing_values(self, df): Metode untuk menangani missing values dalam DataFrame.

            **Ada class ini memiliki metode handle_missing_values untuk menangani missing values dalam DataFrame.**

        - handle_outliers(self, df, column): Metode untuk menangani outliers dalam kolom tertentu dari DataFrame.

            **Ada class ini memiliki metode handle_outliers untuk menangani outliers dalam kolom tertentu dari DataFrame.**

        - save_to_parquet(self, df, file_name): Metode untuk menyimpan DataFrame ke file Parquet.

            **Ada class ini memiliki metode save_to_parquet untuk menyimpan DataFrame ke file Parquet.**   

    - **Metode read_csv_data**
        - Gunakan pandas untuk membaca file CSV.
        - Contoh: pd.read_csv(file_path) di mana file_path adalah path ke file CSV.

            ![Gambar Code Metode read_csv_data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-03_Code-method-read_csv_data.png?raw=true)

            **Kode yang diberikan adalah bagian dari sebuah kelas Python yang disebut DataLakeBuilder. Kelas ini memiliki satu metode bernama read_csv_data yang bertujuan untuk membaca data dari sebuah file CSV.**

    - **Metode handle_missing_values**
        - Terapkan strategi untuk menangani missing values, seperti pengisian nilai (imputation) atau penghapusan baris/kolom.
        - Contoh: Menggunakan df.fillna() atau df.dropna() dari pandas.

            ![Gambar Code Metode handle_missing_values](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-04_Code-method-handle_missing_values.png?raw=true)

            **Kode yang  diberikan adalah metode baru dalam kelas DataLakeBuilder yang disebut handle_missing_values. Metode ini bertujuan untuk menangani nilai-nilai yang hilang (missing values) dalam sebuah DataFrame.**

    - **Metode handle_outliers**
        - Gunakan teknik statistik untuk mendeteksi dan menangani outliers.
        - Contoh: IQR (Interquartile Range) untuk mengidentifikasi outliers dan kemudian menggantinya atau menghapusnya.

            ![Gambar Code Metode handle_outliers](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-05_Code-method-handle_outliers.png?raw=true)

            **Kode ini mendefinisikan metode baru dalam kelas DataLakeBuilder yang disebut handle_outliers. Metode ini bertujuan untuk menangani outliers dalam satu kolom dari DataFrame menggunakan teknik IQR (Interquartile Range).**

    - **Metode save_to_parquet**
        - Simpan DataFrame yang telah diolah ke format Parquet, yang efisien untuk Data Lake.
        - Contoh: df.to_parquet(file_name).

            ![Gambar Code Metode save_to_parquet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-06_Code-method-save_to_parquet.png?raw=true)

            **Kode ini mendefinisikan metode save_to_parquet dalam kelas DataLakeBuilder. Metode ini bertujuan untuk menyimpan DataFrame ke dalam format file Parquet di dalam folder 'data_lake'.**

    - **Eksekusi Script**
        - Buat instance dari DataLakeBuilder dan panggil metode-metodenya untuk setiap file CSV (events.csv, customers.csv, tickets.csv, transactions.csv, dan customer_feedback.csv).
        - Pastikan semua file terbaca dan diolah dengan benar, lalu simpan dalam format Parquet.

            ![Gambar Code Eksekusi Script](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-07_Code-bagian-eksekusi-script.png?raw=true)

            **folder_path = "data_source": Variabel folder_path digunakan untuk menyimpan path ke folder yang berisi file-file CSV yang akan dibaca. Pengecekan keberadaan folder tersebut. builder = DataLakeBuilder(). Kode ini membuat instance dari kelas DataLakeBuilder, yang kemudian digunakan untuk memanggil metode-metode dalam kelas tersebut. Lalu membaca file-file CSV dari folder yang ditentukan dan memuatnya ke dalam DataFrame menggunakan metode read_csv_data dari objek builder. Kemudian Kode ini menggunakan metode handle_outliers dari objek builder untuk menangani outliers dalam kolom 'price' dari DataFrame tickets_df. Dan menyimpan setiap DataFrame ke dalam format file Parquet di dalam folder 'data_lake' menggunakan metode save_to_parquet dari objek builder.**

    - **Validasi Data**
        - Setelah semua data disimpan dalam format Parquet, buat metode untuk memvalidasi atau menampilkan ringkasan data.
        - Contoh: Metode validate_data(self, file_path) yang membaca file Parquet dan menampilkan ringkasan statistik atau beberapa baris awal data.

            ![Gambar Code Validasi Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-08_Code-method-validate_data.png?raw=true)

            **def read_parquet_data(self, file_path):: Metode ini bertujuan untuk membaca data dari file Parquet. def validate_data(self, file_path):: Metode ini bertujuan untuk memvalidasi data dalam file Parquet.**

            ![Gambar Code Validasi Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-09_Code-validasi-data.png?raw=true)

            **Setiap kali metode validate_data dipanggil, itu membaca data dari file Parquet yang ditentukan, menampilkan ringkasan statistik tentang data (dengan menggunakan describe()) dan beberapa baris awal dari data (dengan menggunakan head()). Hal ini membantu untuk memastikan bahwa data yang disimpan dalam format Parquet telah berhasil dibaca dan memiliki format yang sesuai untuk proses selanjutnya.**

    - **Hasil Validasi data dengan menunjukkan ringkasan statistik dan beberapa baris awal data jika script di running.**

        ![Gambar Hasil Statistik customer_feedback](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-10_Hasil-statistik-customer_feedback.png?raw=true)

        ![Gambar Hasil Statistik customers](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-11_Hasil-statistik-customers.png?raw=true)

        ![Gambar Hasil Statistik events](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-12_Hasil-statistik-events.png?raw=true)

        ![Gambar Hasil Statistik tickets](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-13_Hasil-statistik-tickets.png?raw=true)

        ![Gambar Hasil Statistik transactions](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-14_Hasil-statistik-transaction.png?raw=true)
    
    - **Running file data_ingestion.py**

        ![Gambar Running file data_ingestion.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/2-15-Running-file-data-ingestion.py.png?raw=true)

        **Output yang dihasilkan setelah melakukan eksekusi pada script tersebut adalah melakukan penyimpanan file parquet hasil ingestion tadi ke dalam folder data lake.**

3. **Transformasi Data dan Pemuatan ke Data Warehouse**
    - **Penyiapan Skrip Python untuk Transformasi Data**

        ![Gambar Install Library Google Cloud Storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-01_Install-library-google-cloud-storage.png?raw=true)

        **Jangan lupa untuk melakukan Install Library Google Cloud Storage**

        - Buat file Python baru dengan nama data_transformation.py.

            ![Gambar Buat file Python data_transformation.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-02_Buat-file-data_transformation.py.png?raw=true)

        - Dalam file ini, buat kelas dengan nama DataWarehouseLoader.

            ![Gambar buat kelas dengan nama DataWarehouseLoader](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-03_Buat-class-DataWarehouseLoader.png?raw=true)

    - **Kelas DataWarehouseLoader**
        - Kelas ini harus memiliki metode untuk membaca data dari Data Lake, melakukan transformasi data, dan menyimpan data yang telah ditransformasi ke Data Warehouse.

            **Ada Class ini memiliki metode yang sudah ditentukan.**

        - load_data(self, file_path): Metode untuk membaca data dari Data Lake (format Parquet).

            **Class ini ada metode load_data untuk membaca data dari Data Lake (format Parquet)**
        - transform_data(self, df): Metode umum untuk melakukan transformasi data.

            **Class ini ada metode transform_data untuk melakukan transformasi data**

        - save_to_warehouse(self, df, table_name): Metode untuk menyimpan data ke Data Warehouse.

            **Class ini ada metode save_to_warehouse untuk menyimpan data ke Data Warehouse.**

    - **Metode load_data**
        - Gunakan pandas untuk membaca file Parquet dari Data Lake.
        - Load data dari file Parquet untuk tabel events, customers, tickets, transactions, dan customer_feedback.
        - Contoh: pd.read_parquet(file_path).

            ![Gambar Metode load_data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-04_Code-method-load_data.png?raw=true)

            **Dengan demikian, dengan menggunakan objek dari kelas DataWarehouseLoader dan memanggil metode load_data dengan memberikan path ke file Parquet sebagai argumen, maka dapat membaca data dari Data Lake yang disimpan dalam format Parquet ke dalam DataFrame.**

    - **Metode Transform Data**
        - **Menggabungkan Data untuk Analisis**
            - Gabungkan tabel transactions dengan tickets berdasarkan ticket_id, dan kemudian dengan events berdasarkan event_id.

                ![Gambar Code Menggabungkan Data untuk Analisis](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-05_Code-gabungkan-data-untuk-analisis.png?raw=true)

                **Metode transform_data dalam kelas DataWarehouseLoader memiliki tujuan untuk mentransformasi data dengan cara menggabungkan beberapa DataFrames. Di sini, menggunakan fungsi pd.merge, DataFrame transactions_df dan tickets_df digabungkan berdasarkan kolom 'ticket_id'. Hasil gabungan disimpan dalam DataFrame merged_df. DataFrame feedback_df digabungkan dengan merged_df berdasarkan kolom 'transaction_id'. Hasil gabungan disimpan dalam DataFrame feedback_analysis. DataFrame feedback_analysis yang sudah digabungkan sebelumnya, sekarang digabungkan dengan DataFrame events_df berdasarkan kolom 'event_id'. Hasil akhir dari proses transformasi ini akan tersimpan kembali dalam feedback_analysis.**

        - Menghitung Jumlah Tiket yang Terjual per Acara
            - Gunakan groupby pada kolom event_id atau name dari tabel events.
            - Hitung jumlah tiket yang terjual dengan mengagregasi kolom quantity menggunakan fungsi sum.

                ![Gambar Code Menghitung Jumlah Tiket yang Terjual per Acara](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-06_Code-menghitung-jumlah-tiket-yang-terjual.png?raw=true)

                **Di sini, DataFrame merged_df diambil dan di-grup berdasarkan kolom 'event_id' menggunakan metode groupby. Kemudian, menggunakan metode agg, jumlah tiket terjual per acara dihitung dengan menjumlahkan nilai di kolom 'quantity' untuk setiap kelompok. reset_index() digunakan untuk mengatur ulang indeks DataFrame sehingga 'event_id' menjadi kolom biasa. Hasilnya disimpan dalam DataFrame tickets_sold_per_event.**

        - Menghitung Total Pendapatan dari Setiap Acara
            - Dari DataFrame yang digabungkan sebelumnya, gunakan groupby pada kolom event_id atau name.
            - Hitung total pendapatan dengan mengagregasi total_amount menggunakan fungsi sum.

                ![Gambar Code Menghitung Total Pendapatan dari Setiap Acara](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-07_Code-menghitung-total-pendapatan-setiap-acara.png?raw=true)

                **Di sini, DataFrame merged_df di-grup berdasarkan kolom 'event_id' menggunakan metode groupby. Kemudian, menggunakan metode agg, total pendapatan dari setiap acara dihitung dengan menjumlahkan nilai di kolom 'total_amount' untuk setiap kelompok. reset_index() digunakan untuk mengatur ulang indeks DataFrame sehingga 'event_id' menjadi kolom biasa. Hasilnya disimpan dalam DataFrame revenue_per_event**

        - Analisis Feedback Pelanggan
            - Gabungkan tabel customer_feedback dengan transactions berdasarkan transaction_id untuk mengaitkan feedback dengan transaksi.
            - Analisis rating rata-rata per acara.

                ![Gambar Code Analisis Feedback Pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-08_Code-analisis-rata-rata-per-acara.png?raw=true)

                **Di sini, DataFrame feedback_analysis di-grup berdasarkan kolom 'event_id' menggunakan metode groupby. Kemudian, menggunakan metode agg, rating rata-rata dari setiap acara dihitung dengan mengambil nilai rata-rata dari kolom 'rating' untuk setiap kelompok. reset_index() digunakan untuk mengatur ulang indeks DataFrame sehingga 'event_id' menjadi kolom biasa. Hasilnya disimpan dalam DataFrame avg_rating_per_event.**

    - Metode Save to Werehouse

        ![Gambar Code Metode Save to Werehouse](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-09_Code-save-to-warehouse.png?raw=true)

        **Metode save_to_warehouse dalam kelas DataWarehouseLoader bertujuan untuk menyimpan DataFrame ke dalam Data Warehouse dalam format file Parquet. Dengan langkah-langkah ini, DataFrame akan disimpan dalam format Parquet di Data Warehouse, di dalam folder yang sesuai dengan tanggal, dengan nama tabel yang ditentukan.**

        ![Gambar Code Metode Save to Werehouse](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-10_Code-save-to-folder-data_warehouse.png?raw=true)

        **Variabel data_lake_folder menyimpan path ke folder data_lake di mana file-file Parquet disimpan. Kode ini membuat instance dari kelas DataWarehouseLoader yang akan digunakan untuk memuat dan menyimpan data. DataFrame yang berisi data dari file Parquet di Data Lake dimuat menggunakan metode load_data dari objek loader. Metode transform_data dipanggil untuk melakukan transformasi data pada DataFrame yang telah dimuat sebelumnya. Hasil transformasi disimpan dalam variabel. Metode save_to_warehouse dipanggil untuk menyimpan hasil transformasi ke dalam Data Warehouse dengan struktur folder yang berdasarkan tanggal (hari ini). Data disimpan dalam format Parquet dengan nama tabel yang sesuai.**

        - Penamaan File Hasil Transformasi
            - Tickets_sold_per_event.parquet
            - Revenue_per_event.parquet
            - Feedback_analysis.parquet

                ![Gambar Penamaan File Hasil Transformasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-14_Isi-folder-data_warehouse-berdasarkan-datetime.png?raw=true)

        - Setup Google Cloud Storage
            - Pastikan Anda memiliki akses ke Google Cloud Storage.

                ![Gambar Setup Google Cloud Storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-15_setup-bucket-gcp.png?raw=true)

            - Buat bucket yang akan digunakan sebagai Data Warehouse, jika belum ada.

                ![Gambar Setup Google Cloud Storage](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-16_bucket-created.png?raw=true)
            
            - Code Upload hasil data warehouse ke Google Cloud Storage

                ![Gambar Code Upload hasil data warehouse ke GCS](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-11_Code-upload-to-gcs.png?raw=true)

                **Metode upload_to_gcs dalam kelas DataWarehouseLoader bertujuan untuk mengunggah file ke Google Cloud Storage (GCS). Di sini, menggunakan kelas storage.Client, client GCS diinisialisasi dari file kunci JSON yang diberikan oleh service_account_key_path. Setelah inisialisasi client, bucket GCS diakses dengan nama yang diberikan oleh bucket_name. Kemudian, sebuah objek blob dibuat dengan nama yang diberikan oleh destination_blob_name. Akhirnya, menggunakan metode upload_from_filename, file yang ada di file_path diunggah ke dalam blob tersebut. Setelah proses pengunggahan selesai, pesan konfirmasi akan dicetak untuk memberitahu pengguna bahwa file telah berhasil diunggah ke GCS dengan nama yang sesuai.**
                
                ![Gambar Code Upload hasil data warehouse ke GCS](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-12_Code-upload-to-gcs2.png?raw=true)

                **Kode yang diberikan melakukan proses upload file ke Google Cloud Storage (GCS) menggunakan metode upload_to_gcs dari objek loader. Di sini, bucket_name adalah nama bucket di GCS tempat Anda ingin mengunggah file. service_account_key_path adalah path ke file kunci JSON yang diperlukan untuk otentikasi saat menggunakan layanan GCS. Dalam setiap baris, metode upload_to_gcs dipanggil untuk mengunggah file ke GCS. Argumen yang diberikan adalah nama bucket, path file lokal, nama blob di GCS, dan path ke kunci JSON untuk otentikasi. Tiga file Parquet, masing-masing Tickets_sold_per_event.parquet, Revenue_per_event.parquet, dan Feedback_analysis.parquet, diunggah ke dalam bucket yang ditentukan.**

        - Struktur Folder Berdasarkan DateTime
            - Untuk mengorganisir data, gunakan struktur folder berdasarkan tanggal. Format yang umum adalah YYYY/MM/DD atau YYYY-MM-DD.
                
                ![Gambar Code Struktur Folder Berdasarkan DateTime](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-13_Code-struktur-folder-berdasarkan-datetime.png?raw=true)

                **Dalam kode yang diberikan, hasil transformasi dari data disimpan ke dalam Data Warehouse dengan struktur folder yang berdasarkan tanggal saat ini. Di sini, variabel today_date_folder diinisialisasi dengan tanggal saat ini dalam format 'YYYY-MM-DD'. Tiga metode save_to_warehouse dipanggil untuk menyimpan hasil transformasi ke dalam Data Warehouse. Setiap metode menerima tiga argumen: DataFrame yang berisi hasil transformasi, nama tabel yang sesuai, dan struktur folder berdasarkan tanggal yang telah diinisialisasi sebelumnya. Dengan demikian, setiap hasil transformasi disimpan ke dalam Data Warehouse dengan nama tabel yang sesuai, di dalam folder yang sesuai dengan tanggal saat ini.**

            - Contoh: Untuk data yang diproses pada tanggal 20 November 2023, folder bisa bernama 2023/11/20 atau 2023-11-20.

                ![Gambar Isi folder data warehouse](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-14_Isi-folder-data_warehouse-berdasarkan-datetime.png?raw=true)

    - **Running file data_transformation.py**

        ![Gambar Running file data_transformation.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-17_running-data_transformation.py.png?raw=true)

        **Terlihat 3 file parquet hasil transformasi diunggah ke bucket pada cloud storage.**

    - **File parquet success to load in GCS**

        ![Gambar Running file data_transformation.py](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-18_load-file-parquet-to-google-cloud-storage.png?raw=true)
    
    - **Hasil Transformasi dalam bentuk file CSV (Optional)**

        ![Gambar Hasil Transformasi revenue_per_event](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-19_Hasil-transform-revenue_per_event-csv.png?raw=true)

        ![Gambar Hasil Transformasi tickets_sold_per_event](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-20_Hasil-transform-tickets_sold_per_event-csv.png?raw=true)

        ![Gambar Hasil Transformasi Feedback_analysis](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/3-21_Hasil-transform-Feedback_analysis-csv.png?raw=true)

4. **Orkestrasi Workflow dengan Apache Airflow**
    - **Buatlah DAG (Directed Acyclic Graph) di Apache Airflow untuk mengotomatisasi proses pengambilan data, transformasi, dan pemuatan ke Data Warehouse.**

        ![Gambar Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-01_Import-library-yang-dibutuhkan.png?raw=true)

        **Import Library yang dibutuhkan. Persiapkan file data_ingestion.py dan data_transformation.py dengan memasukkan ke direktori yang sama dengan file DAG.**

        ![Gambar Persiapkan direktori data_source](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-02_Persiapkan-direktori-folder-data_source.png?raw=true)

        **Persiapkan dataset pada direktori di data_source. Serta jangan lupa untuk persiapkan file service account dalam bentuk JSON.**

    - **DAG harus mencakup task untuk data ingestion, data transformation, dan loading data ke warehouse.**

        - Code Function untuk task data ingestion

            ![Gambar Code Function untuk task data ingestion](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-03_Code-function-perform_data_ingestion.png?raw=true)

            **Pertama-tama, fungsi membuat instance dari kelas DataLakeBuilder. Instance ini akan digunakan untuk memanggil metode-metode yang dibutuhkan untuk membaca dan menyimpan data. Fungsi membaca setiap file CSV dari folder yang ditentukan (data_source_folder) menggunakan metode read_csv_data dari objek builder. Setelah data dibaca, fungsi menyimpannya ke dalam Data Lake dalam format Parquet menggunakan metode save_to_parquet dari objek builder. Dengan cara ini, fungsi perform_data_ingestion akan melakukan proses data ingestion untuk setiap file CSV yang diberikan ke dalam Data Lake dalam format Parquet.**

        - Code Function untuk task data transformation

            ![Gambar Code Function untuk task data transformation](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-04_Code-function-perform_data_transformation.png?raw=true)

            **Pertama-tama, fungsi membuat instance dari kelas DataWarehouseLoader. Instance ini akan digunakan untuk memuat dan mentransformasi data dari Data Lake. Fungsi memuat setiap file Parquet dari Data Lake menggunakan metode load_data dari objek loader. Data yang dimuat kemudian disimpan dalam DataFrame masing-masing, yaitu events_df, customers_df, tickets_df, transactions_df, dan feedback_df. Setelah data dimuat, fungsi melakukan transformasi data menggunakan metode transform_data dari objek loader. Hasil transformasi, yaitu tickets_sold_per_event, revenue_per_event, dan avg_rating_per_event, disimpan untuk digunakan atau diambil oleh bagian lain dari kode. Fungsi mengembalikan hasil transformasi dalam bentuk tiga DataFrame: tickets_sold_per_event, revenue_per_event, dan avg_rating_per_event.**

        - Code Function untuk task loading data ke warehouse

            ![Gambar Code Function untuk task loading data ke warehouse](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-05_Code-function-perform_loading_data_to_warehouse.png?raw=true)

            **Fungsi mengambil hasil transformasi, yaitu tickets_sold_per_event, revenue_per_event, dan avg_rating_per_event, dari XCom menggunakan xcom_pull. Hasil transformasi ini diambil dari task dengan task_ids 'data_transformation'. Variabel today_date_folder diinisialisasi dengan tanggal hari ini dalam format 'YYYY-MM-DD'. Fungsi menggunakan metode save_to_warehouse dari objek loader untuk menyimpan hasil transformasi ke dalam Data Warehouse. Hasil transformasi disimpan dalam folder yang sesuai dengan tanggal hari ini. Fungsi menggunakan metode upload_to_gcs dari objek loader untuk mengunggah hasil transformasi ke GCS. Hasil transformasi yang disimpan dalam format Parquet di Data Warehouse diunggah ke dalam bucket GCS yang ditentukan.**

        - Code Eksekusi setiap task

            ![Gambar Code Function untuk task loading data ke warehouse](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-06_Code-eksekusi-setiap-task.png?raw=true)

            **Task untuk data ingestion (data_ingestion_task): Task ini akan menjalankan fungsi perform_data_ingestion yang bertanggung jawab untuk melakukan proses data ingestion dari file CSV ke dalam Data Lake dalam format Parquet. Task untuk data transformation (data_transformation_task): Task ini akan menjalankan fungsi perform_data_transformation yang bertanggung jawab untuk melakukan proses transformasi data pada Data Lake. Task untuk loading data ke Data Warehouse(loading_data_to_warehouse_task): Task ini akan menjalankan fungsi perform_loading_data_to_warehouse yang bertanggung jawab untuk melakukan proses loading data hasil transformasi ke dalam Data Warehouse dan juga mengunggah data ke Google Cloud Storage (GCS). provide_context=True digunakan untuk memberikan akses ke context Airflow seperti XCom, yang diperlukan untuk mengambil hasil transformasi dari task sebelumnya.**

    - **Jelaskan bagaimana Anda akan menjadwalkan DAG ini dan mengatur dependencies antar tasks.**

        ![Gambar Code menjadwalkan DAG](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-07_Code-inisialisasi-DAG.png?raw=true)

        **schedule_interval=timedelta(days=1): DAG akan dieksekusi sekali sehari.start_date=datetime(2024, 4, 24): Waktu mulai eksekusi DAG.**

        ![Gambar Code dependencies antar task](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-08_Code-dependencies-antar-task.png?raw=true)

        **Dengan menetapkan dependencies ini, Airflow akan mengeksekusi task-task tersebut sesuai dengan urutan yang ditentukan: data_ingestion_task dijalankan terlebih dahulu, kemudian data_transformation_task, dan terakhir loading_data_to_warehouse_task.**
    
    - **Jalankan Airflow Scheduler dan Webserver:**

        ![Gambar Jalankan Airflow Scheduler](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-09_Jalankan-airflow-scheduler.png?raw=true)

        ![Gambar Jalankan Airflow Webserver](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-10_Jalankan-airflow-webserver.png?raw=true)
    
    - **Running DAG Success:**

        ![Gambar Running DAG Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-11_Running-DAG-success.png?raw=true)

        ![Gambar Running DAG Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-12_Running-DAG-success2.png?raw=true)

        **Terlihat pada graph bahwa dag berhasil dieksekusi dengan semua task berwarna hijau.**

    - **Aturan Schedule:**

        ![Gambar Running DAG Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-13_Schedule-interval.png?raw=true)

        **Terlihat bahwa dag tersebut akan dieksekusi 1 hari sekali**

    - **Hasil Logs Task 1 data_ingestion :**

        ![Gambar Hasil Logs Task 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-14_Logs-task1-data_ingestion.png?raw=true)

        **Terlihat bahwa marking task a success dengan mengembalikan nilai bahwa data file parquet disimpan ke folder data_lake**

        ![Gambar Isi folder data_lake](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-15_Isi-folder-data_lake.png?raw=true)

    - **Hasil Logs Task 2 data_transformation :**

        ![Gambar Hasil Logs Task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-16_Logs-task2-data_transformation.png?raw=true)

        ![Gambar Hasil Logs Task 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-17_Logs-task2-data_transformation2.png?raw=true)

        **Terlihat bahwa marking task a success dengan mengembalikan nilai yaitu hasil dari transformasi data tersimpan ke folder data_warehouse.**

        ![Gambar Menghasilkan 2 folder](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-18_Menghasilkan-2-folder.png?raw=true)

        ![Gambar Isi folder data warehouse](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-19_Isi-folder-data_warehouse.png?raw=true)

    - **Hasil Logs Task 3 loading_data_to_warehouse :**

        ![Gambar Hasil Logs Task 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-20_Logs-task3-loading_data_to_warehouse.png?raw=true)

        **Terlihat bahwa marking task a success dengan mengembalikan nilai yaitu menampilkan informasi hasil dari transformasi yaitu berupa file parquet berhasil diunggah ke Google Cloud Storage.**

        ![Gambar Load to Data warehouse GCS](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/Code_Competence_02/screenshots/4-21-load-file-parquet-to-google-cloud-storage.png?raw=true)