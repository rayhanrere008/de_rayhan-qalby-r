## Soal dan Jawaban Prioritas 2 - Data Quality dan Data Governance

1. Lakukan proses data cleaning dengan kriteria sebagai berikut:
    - Menggunakan [dataset](https://gist.github.com/nadirbslmh/070556b27c7949e73fa435be6b9a8081) transaksi berikut.
    - Mengubah format nomor telepon dengan awalan +62 di depan. Contohnya seperti ini: +6281234567891
    - Mengubah nilai transaksi (transaction_amount) dengan format seperti berikut: Rp 12.000
    - Pastikan data yang diambil adalah data transaksi dengan status sama dengan **success**.
    - Proses data cleaning dapat menggunakan library Pandas.
    - Hasil akhir data cleaning disimpan di dalam DataFrame.

**Jawaban :**

- **Install Library yang dibutuhkan (Pandas):**

    ![Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/01_Install-library-pandas.png?raw=true)

- **Import Library Pandas dan Locale:**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/02_Import-library.png?raw=true)

- **Set locale ke Indonesia untuk menggunakan format mata uang Rp:**

    ![Set locale ke Indonesia](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/03_Set-locale-ke-indonesia.png?raw=true)

    **Dengan menggunakan locale.setlocale(locale.LC_ALL, 'id_ID'), kita mengatur locale ke Indonesia yang menggunakan titik sebagai pemisah ribuan. Ini akan memastikan bahwa nilai transaksi diformat dengan "Rp" diikuti oleh angka yang dipisahkan dengan titik.**

- **Read Dataset pada file csv:**

    ![Read Dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/04_Read-dataset-file-csv.png?raw=true)

    **Code tersebut adalah penggunaan fungsi read_csv() dari pustaka Pandas dalam bahasa pemrograman Python. Ini digunakan untuk membaca file CSV (Comma Separated Values) dan menyimpannya ke dalam sebuah objek DataFrame, yang disingkat sebagai df.**

- **Ubah format nomor telepon dengan awalan +62:**

    ![Ubah format nomor telepon](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/05_Ubah-format-telepon-ke-+62.png?raw=true)

    **Baris kode tersebut menambahkan awalan internasional "+62" ke kolom "phone_number" dalam DataFrame df. Ini dilakukan dengan menggunakan metode .apply() bersama dengan fungsi lambda.**

- **Ubah format nilai transaksi menjadi "Rp 12.000":**

    ![Ubah format nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/06_Ubah-format-nilai-transaksi.png?raw=true)

    **Baris kode tersebut mengubah format kolom "transaction_amount" dalam DataFrame df. Ini dilakukan dengan menggunakan metode .map() bersama dengan fungsi lambda. Akibatnya, setiap nilai dalam kolom "transaction_amount" akan sekarang memiliki format mata uang Rupiah dengan tanda titik sebagai pemisah ribuan.**

- **Filter data berdasarkan status transaksi success:**

    ![Filter data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/07_Filter-data-success.png?raw=true)

    **Baris kode tersebut melakukan filtering pada DataFrame df untuk hanya menyertakan baris-baris di mana nilai kolom "transaction_status" adalah 'success'. Akibatnya, DataFrame df akan sekarang hanya berisi baris-baris di mana transaksi berhasil ('success') berdasarkan nilai kolom "transaction_status".**

- **Melakukan reset index agar berurutan:**

    ![Melakukan reset index](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/08_Lakukan-reset-index.png?raw=true)

    **Baris kode tersebut mengatur ulang indeks DataFrame df setelah proses filtering sebelumnya. Hal ini dilakukan dengan menggunakan metode .reset_index() dengan argumen drop=True. Akibatnya, DataFrame df akan sekarang memiliki indeks yang diatur ulang dan tidak menyertakan indeks lama sebagai kolom tambahan. Indeks baru akan dimulai dari 0 dan berurutan sesuai dengan jumlah baris DataFrame yang baru setelah proses filtering.**

- **Tampilkan 10 Data Pertama:**

    ![Tampilkan 10 Data Pertama](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/09_Tampilkan-10-data-pertama.png?raw=true)

    **Code tersebut akan menampilkan 10 data pertama dari hasil data cleaning pada dataframe.**

- **Tampilkan 10 Data Terakhir:**

    ![Tampilkan 10 Data Terakhir](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/10_Tampilkan-10-data-terakhir.png?raw=true)

    **Code tersebut akan menampilkan 10 data terakhir dari hasil data cleaning pada dataframe.**

- **Simpan hasil data cleaning ke file csv:**

    ![Simpan hasil data cleaning ke file csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/11_Simpan-hasil-data-cleaning-ke-csv.png?raw=true)

    ![Isi file csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/19_Pemahaman-tentang-Data-Quality-dan-Data-Governance/screenshots/Prioritas-2/12_Isi-file-cleaning-csv.png?raw=true)


