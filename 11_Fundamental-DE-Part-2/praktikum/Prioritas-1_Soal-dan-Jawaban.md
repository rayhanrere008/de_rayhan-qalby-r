## Soal Prioritas 1 - Fundamental DE Part 2

1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.
2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.
3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.

**Jawaban :**

1. Data terstruktur dan data tidak terstruktur adalah dua jenis data yang berbeda berdasarkan cara mereka diorganisasi, disimpan, dan diproses/pengelolaan.
- **Data Struktur** 
    - **Definisi** : Data terstruktur adalah data yang memiliki format standar dan diatur dengan jelas. Setiap entitas atau elemen dalam data memiliki atribut yang konsisten dan berulang. Misalnya memiliki atribut name, address, zip code yang sudah ditentukan.
    - **Contoh** : Database Pelanggan: Dalam bisnis ritel, Database pelanggan yang terstruktur berisi informasi seperti nama, alamat, nomor telepon, dan riwayat pembelian.
    - **Penyimpanan** : Data terstruktur biasanya disimpan dalam bentuk tabel yang berelasi pada Database relasional (seperti MySQL, PostgreSQL) atau Database spasial (seperti PostGIS).
    - **Pengelolaan** : Pengolahan data terstruktur menggunakan bahasa kueri terstruktur (SQL) untuk mengambil, memperbarui, dan menganalisis data. Pengolahan data terstruktur lebih mudah karena formatnya yang terorganisir dengan baik.

- **Data Tidak Terstruktur**
    - **Definisi** : Data tidak terstruktur adalah jenis data yang tidak memiliki format atau struktur yang terdefinisi sebelumnya. Ini seringkali berarti data tersebut tidak mudah diorganisasi dalam tabel atau skema yang sama dengan data terstruktur.
    - **Contoh** : Data tidak terstruktur dapat berupa teks bebas, gambar, audio, video, atau bahkan dokumen HTML. Contoh termasuk posting media sosial, email, transkripsi percakapan, atau rekaman video.
    - **Penyimpanan** : Data tidak terstruktur dapat disimpan dalam sistem file, basis data NoSQL (seperti MongoDB), atau dalam bentuk data lake.
    - **Pengelolaan** : Pengolahan data tidak terstruktur sering memerlukan algoritma pemrosesan bahasa alami, analisis gambar, atau pengenalan pola untuk mengekstrak informasi yang bermanfaat. Biasanya menggunakan Apache Spark dan teknik pemrosesan teks (NLP).

- **Referensi**
    - https://aws.amazon.com/id/compare/the-difference-between-structured-data-and-unstructured-data/
    - https://www.divasoft.net/blog/mengenal-data-tidak-terstruktur-contoh-alat-dan-strateginya
    - https://www.gonel.id/contoh-data-tidak-terstruktur/

2. **Basis data relasional** adalah tipe basis data yang menggunakan model data relasional untuk menyimpan dan mengelola data. Model data relasional ini didasarkan pada teori himpunan matematika dan terdiri dari tabel-tabel yang terkait satu sama lain melalui kunci asing **(foreign keys)**.

    **Cara kerjanya** berbasis pada hubungan relasional yang ditentukan antara data, yang disusun dalam baris dan kolom. Data disusun dalam tabel, dan setiap tabel memiliki hubungan yang ditentukan, yang disebut hubungan relasional. Hubungan relasional ini digunakan untuk mengatur kesesuaian data dan mempermudah proses pengelolaan data. Untuk melakukan proses pengelolaan data diperlukan bahasa kueri terstruktur seperti SQL (Structured Query Language), yang digunakan untuk mengambil, menyisipkan, memperbarui, dan menghapus data dari basis data.

    **Contoh Penggunaan dalam dunia nyata**
    - **Sistem Manajemen Sekolah**: Sekolah atau perguruan tinggi menggunakan basis data relasional untuk menyimpan informasi tentang siswa, guru, dan jadwal. Data seperti informasi pendaftaran siswa, jadwal kelas, dan nilai ujian dapat disimpan dan diakses dengan mudah melalui sistem basis data.
    - **Sistem Perbankan dan Perdagangan**: Basis data relasional digunakan untuk mengelola akun pelanggan, transaksi, dan laporan keuangan.

    **Referensi**
    - https://id.bitdegree.org/tutorial/apa-itu-basis-data-relasional/
    - https://appmaster.io/id/blog/contoh-nyata-database-relasional
    - https://blog.myskill.id/tips-karir/relational-database-definisi-fungsi-dan-contohnya/

3. **Normalisasi basis data** adalah proses desain yang bertujuan untuk mengorganisasi struktur basis data dengan cara membagi tabel menjadi entitas yang lebih kecil dan terkait erat, sehingga mengurangi duplikasi dan kompleksitas. Normalisasi adalah konsep penting dalam desain database relasional. Hal ini memungkinkan pengorganisasian data secara konsisten dan efisien, memastikan integritas data, dan meminimalkan redundansi.

    **Alasan mengapa normalisasi penting dalam konteks basis data relasional:**
    - **Integritas data** : Dengan menghilangkan redundansi dan inkonsistensi data, integritas data dapat dijaga.
    - **Peningkatan Efisiensi Pemeliharaan dan Pembaruan**: Normalisasi menyederhanakan proses pembaruan dan mengurangi risiko kesalahan.
    - **Kinerja Kueri yang Lebih Baik**: Skema yang lebih sederhana memungkinkan pemrosesan dan pengoptimalan kueri yang lebih efisien.

    **Referensi**
    - https://appmaster.io/id/blog/normalisasi-dalam-database-relasional
    - https://medium.com/@fikrijane311/apa-itu-normalisasi-pada-entity-relationship-diagram-erd-bfbbc5fc6256
    - https://medium.com/@fazrianbaryf/normalisasi-dalam-erd-f7434bf146fd
