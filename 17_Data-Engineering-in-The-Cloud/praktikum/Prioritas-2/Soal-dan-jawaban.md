## Soal dan Jawaban Prioritas 2 - Data Engineering in The Cloud

1. Sebuah data transaksi saham telah dikumpulkan dan disimpan pada file berikut. Buatlah sebuah pipeline ETL dengan kriteria berikut:
    - Lakukan proses ekstrak data.
    - Lakukan proses transformasi data yaitu:
        - Ambil transaksi saham untuk GOOGL, AMZN, MSFT dan AAPL. Bisa mengacu pada atribut stock_symbol.
        - Dari transaksi tersebut. Ambil data transaksi saham dengan harga transaksi (trade_price) diatas 500.
    - Lakukan proses load data dalam format parquet ke dalam Google Storage.

**Keterangan :**
- Masih menggunakan storage bucket yang sama dengan prioritas 1.
- Library juga sama.
- Service Account juga sama.

**Jawaban :**

- **Import Library yang dibutuhkan (Pandas, Firebase admin, Requests):**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/01_import-library-yang-dibutuhkan.png?raw=true)

- **Code inisialisasi Firebase:**

    ![Gambar Code inisialisasi Firebase](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/02_Code-inisialisasi-firebase.png?raw=true)

    **Fungsi initialize_firebase_app(service_account_path) bertanggung jawab untuk menginisialisasi Firebase Admin SDK dengan menggunakan file kunci layanan yang disediakan.**

- **Code Function Ekstrak data:**

    ![Gambar Code Function Ekstrak data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/03_Code-function-ekstrak-data.png?raw=true)

    **Dengan cara ini, fungsi extract_data(url) memungkinkan untuk dengan mudah mengambil data dari sumber data JSON di url yang disediakan dan mengubahnya menjadi format yang dapat diolah lebih lanjut dalam Python menggunakan DataFrame.**

- **Code Function Transform data:**

    ![Gambar Code Function Transform data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/04_Code-function-transform-data.png?raw=true)

    **Dengan melakukan langkah-langkah transformasi ini, fungsi transform_data(data) memungkinkan untuk menyaring data dan hanya mempertahankan data yang sesuai dengan kriteria tertentu, dalam hal ini, hanya data transaksi saham dengan harga di atas 500 untuk saham-saham tertentu yang dipilih ['GOOGL', 'AMZN', 'MSFT', 'AAPL'].**

- **Code Function Load data:**

    ![Gambar Code Function Load data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/05_Code-function-load-data-ke-firebase.png?raw=true)

    **Fungsi load_data_to_firebase_storage(data, bucket_name, file_name) bertugas untuk memuat data ke Firebase Storage dalam format Parquet.**

- **Code Main:**

    ![Gambar Code Main](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/06_Code-main.png?raw=true)

    **Dengan demikian, ini adalah skrip yang akan mengekstraksi data dari URL, mentransformasikannya, dan menyimpan data hasil transformasi ke Firebase Storage dalam format Parquet saat dijalankan sebagai skrip utama.**

- **Running Code Success:**

    ![Gambar Running Code Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/07_running-code-success.png?raw=true)

    **Terlihat pesan "Data has been successfully loaded to Firebase Storage with filename: output_transactions_saham.parquet" menandakan bahwa berhasil di load ke firebase storage.**

- **Berhasil Load ke storage firebase:**

    ![Gambar Load ke storage firebase](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/08_file-parquet-berhasil-diload-ke-storage-firebase.png?raw=true)

    **Terlihat file output_transactions_saham.parquet berhasil di load ke storage.**

- **Isi file parquet yang telah diekstrak ke file csv:**

    ![Gambar Isi File Parquet to Csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/09_isi-file-output_transactions_saham.csv-(yang-telah-diubah-dari-file-parquet).png?raw=true)

    ![Gambar Isi File Parquet to Csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/17_Data-Engineering-in-The-Cloud/screenshots/Prioritas-2/10_isi-file-output_transactions_saham.csv-(yang-telah-diubah-dari-file-parquet)2.png?raw=true)

    **Terlihat isi file tersebut telah dilakukan transformasi dengan menampilkan data dengan stock_symbol = ['GOOGL', 'AMZN', 'MSFT', 'AAPL'] dengan harga saham diatas 500.**