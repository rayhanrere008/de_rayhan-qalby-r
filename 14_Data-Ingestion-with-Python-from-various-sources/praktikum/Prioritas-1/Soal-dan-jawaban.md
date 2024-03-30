## Soal Prioritas 1 - Data Ingestion with Python from various sources

1. Ekstrak data transaksi e-commerce dari file CSV dan data produk dari file Excel.
2. Gunakan pymysql untuk mengimpor data pelanggan dari database MySQL.
3. Ambil data pengiriman dari API berikut: https://fakestoreapi.com/products menggunakan requests.
4. Simpan semua data yang diingest ke dalam Pandas DataFrame dan ekspor ke file Parquet.

**Catatan**:

- Untuk soal nomor 1 gunakan dataset berikut dengan nama products dan transactions.csv: https://drive.google.com/drive/folders/1oGNIJGEgX_pzk2juBKRrY9R4cYAQZDH_?usp=sharing 
- Untuk soal nomor 2, jalankan kode SQL yang telah disediakan dengan nama customers.sql untuk menambahkan data pelanggan ke dalam database MySQL.

**Jawaban :**

1. Install Library yang diperlukan seperti pandas, pymysql, requests, openpyxl, pyarrow, fastparquet

    ![Gambar Install Library pandas](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/01_Install-library-pandas.png?raw=true)

    ![Gambar Install Library pymysql](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/02_Install-library-pymysql.png?raw=true)

    ![Gambar Install Library requests](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/03_Install-library-requests.png?raw=true)

    ![Gambar Install Library openpyxl](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/04_Install-library-openpyxl.png?raw=true)

    ![Gambar Install Library pyarrow dan fastparquet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/05_Install-library-pyarrow-fastparquet.png?raw=true)

2. **Mengimpor library yang diperlukan**

    ![Gambar Code Impor Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/06_impor-library.png?raw=true)

3. **Membaca data produk dari file Excel dan data transaksi dari file CSV**

    ![Gambar Code membaca file excel dan csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/07_membaca-dataproduk-datatransaksi.png?raw=true)

4. **Impor file sql**

    ![Gambar Impor file sql di phpmyadmin](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/08_Impor-file-sql-customers.png?raw=true)

    ![Gambar impor berhasil](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/09_File-berhasil-diimpor.png?raw=true)

5. **Mengimpor data pelanggan dari database MySQL menggunakan pymysql**

    ![Gambar impor data pelanggan dari database mysql](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/10_Code-impor-dataPelanggan-dari-databaseMySQL.png?raw=true)

6. **Mengambil data pengiriman dari API menggunakan requests:**

    ![Gambar Code Mengambil data Pengiriman di API](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/11_Code-ambil-data-pengiriman-di-API.png?raw=true)

7. **Menggabungkan semua DataFrame menjadi satu DataFrame tunggal:**

    ![Gambar Code Menggabungkan semua DataFrame](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/12_Menggabungkan-semua-dataframe.png?raw=true)

8. **Menyimpan DataFrame ke dalam file Parquet:**

    ![Gambar Menyimpan dataframe di file parquet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/13_Menyimpan-data-di-file-Parquet.png?raw=true)

    ![Gambar File Berhasil disimpan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/14_output-disimpan-di-file-parquet.png?raw=true)

9. **Code berhasil dijalankan**

    ![Gambar Code Berhasil dijalankan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/15_code-berhasil-dijalankan.png?raw=true)

10. **Hasil Output jika ditampilkan**

    ![Gambar Code Berhasil dijalankan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/15_code-berhasil-dijalankan.png?raw=true)

11. **Output Jika Ditampilkan**

    ![Gambar Ouput Jika Ditampilkan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/16_Output-1.png?raw=true)

    ![Gambar Ouput Jika Ditampilkan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/16_Output-2.png?raw=true)

    ![Gambar Ouput Jika Ditampilkan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-1/16_Output-3.png?raw=true)