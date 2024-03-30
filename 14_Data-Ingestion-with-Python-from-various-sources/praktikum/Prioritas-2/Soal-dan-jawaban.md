## Soal Prioritas-2 - Data Ingestion with Python from various sources

1. Persiapan Lingkungan Pengembangan:
    - Pastikan Python sudah terinstal di sistem Anda.
    - Install library yang diperlukan: requests untuk mengirim permintaan HTTP, dan beautifulsoup4 untuk parsing HTML.
2. Pemilihan Situs E-commerce dan Produk:
    - Pilih situs e-commerce yang akan di-scrape (misalnya, Amazon, Tokopedia, dll.).
    - Tentukan produk spesifik yang ulasannya ingin Anda kumpulkan.
3. Ekstraksi Data Ulasan:
    - Gunakan library requests untuk mengirim permintaan ke halaman produk.
    - Dengan BeautifulSoup, parse HTML yang diterima untuk mengekstrak informasi ulasan, seperti rating, teks ulasan, tanggal ulasan, dan nama pengguna.
4. Penanganan Pagination:
    - Jika ulasan produk terdapat di beberapa halaman, implementasikan logika untuk menelusuri setiap halaman.
    - Ekstrak data ulasan dari setiap halaman tersebut.
5. Pembersihan dan Penyimpanan Data:
    - Bersihkan data yang telah diekstrak dari tag HTML dan format yang tidak diperlukan.
    - Simpan data ulasan ke dalam format yang diinginkan, seperti CSV atau database.