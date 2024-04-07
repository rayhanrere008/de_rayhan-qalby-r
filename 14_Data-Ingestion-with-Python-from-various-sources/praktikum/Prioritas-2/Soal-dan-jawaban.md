## Soal Prioritas-2 - Data Ingestion with Python from various sources

1. Persiapan Lingkungan Pengembangan:
    - Pastikan Python sudah terinstal di sistem Anda.

        ![Gambar Python terinstall](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/01_python-terinstall.png?raw=true)

    - Install library yang diperlukan: requests untuk mengirim permintaan HTTP, dan beautifulsoup4 untuk parsing HTML.

        ![Gambar Library terinstall](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/01_install_library.png?raw=true)


2. Pemilihan Situs E-commerce dan Produk:
    - Pilih situs e-commerce yang akan di-scrape (misalnya, Amazon, Tokopedia, dll.).

        ![Gambar Situs E-commerce](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/02_Situs-e-commerce-bukalapak.png?raw=true)

    - Tentukan produk spesifik yang ulasannya ingin Anda kumpulkan.

        ![Gambar Produk Spesifik](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/02_produk-spesifik.png?raw=true)

3. Ekstraksi Data Ulasan:
    - Gunakan library requests untuk mengirim permintaan ke halaman produk.

        ![Gambar Mengirim Requests](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/03_mengirim-requests-ke-halaman-produk.png?raw=true)

    - Dengan BeautifulSoup, parse HTML yang diterima untuk mengekstrak informasi ulasan, seperti rating, teks ulasan, tanggal ulasan, dan nama pengguna.

        ![Gambar Mengekstrak Informasi Ulasan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/03_mengekstrak-informasi-ulasan.png?raw=true)

4. Penanganan Pagination:
    - Jika ulasan produk terdapat di beberapa halaman, implementasikan logika untuk menelusuri setiap halaman.
    - Ekstrak data ulasan dari setiap halaman tersebut.
5. Pembersihan dan Penyimpanan Data:
    - Bersihkan data yang telah diekstrak dari tag HTML dan format yang tidak diperlukan.
    - Simpan data ulasan ke dalam format yang diinginkan, seperti CSV atau database.

        ![Gambar Simpan data ke CSV](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/05_simpan-data-ke-csv.png?raw=true)
    
    - Isi File CSV:

        ![Gambar isi file CSV](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/14_Data-Ingestion-with-Python-from-various-sources/screenshots/Prioritas-2/05_isi-file-csv.png?raw=true)