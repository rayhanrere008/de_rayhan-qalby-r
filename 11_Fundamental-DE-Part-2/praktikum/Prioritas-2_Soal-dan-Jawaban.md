## Soal Prioritas 2 - Fundamental DE Part 2

Anda diberi tugas untuk merancang sistem basis data untuk sebuah perusahaan e-commerce. Perusahaan ini memiliki data yang sangat beragam, mulai dari data transaksi pelanggan hingga log interaksi pengguna di website. Diskusikan pendekatan yang akan Anda gunakan untuk mengelola data ini, termasuk pemilihan antara basis data relasional dan NoSQL, serta strategi untuk mengintegrasikan data terstruktur dan tidak terstruktur.

**Jawaban :**

Dalam merancang sistem basis data untuk perusahaan e-commerce dengan data yang beragam, ada beberapa pertimbangan penting yang perlu dipertimbangkan. Berikut adalah pendekatan dan strategi yang dapat saya gunakan:

1. **Pemilihan Antara Basis Data Relasional dan NoSQL**:
    - **Basis Data Relasional**:
        - Cocok untuk data yang terstruktur, memiliki skema yang tetap, dan memerlukan integritas data yang tinggi.
        - Digunakan untuk mengelola data pelanggan, produk, pesanan, dan transaksi.
        - Memiliki keuntungan dalam konsistensi data dan kemampuan untuk melakukan transaksi kompleks.
    - **Basis Data NoSQL**:
        - Cocok untuk data yang tidak terstruktur, memiliki skema yang fleksibel, dan memerlukan skalabilitas dan performa yang tinggi.
        - Digunakan untuk mengelola data seperti log interaksi pengguna, data sensor, dan data media sosial.
        - Memiliki keuntungan dalam fleksibilitas skema, skalabilitas, dan performa.

2. **Strategi Integrasi Data Terstruktur dan Tidak Terstruktur**:
    - **Data Terstruktur**:
        - Representasikan dalam skema yang jelas (tabel dengan baris dan kolom).
        - Cocok untuk data kuantitatif seperti operasi keuangan dan angka penjualan.
    - **Data Tidak Terstruktur**:
        - Tidak mengikuti skema yang telah ditentukan sebelumnya.
        - Representasikan dalam berbagai bentuk (misalnya, teks, audio, video).
        - Cocok untuk data kualitatif seperti log interaksi pengguna, media sosial, dan data sensor.
    - **Penyimpanan Data**: 
        - Gunakan basis data relasional untuk data terstruktur dan basis data NoSQL untuk data tidak terstruktur.

3. **Pemodelan Data dan Normalisasi**:
    - Desain skema basis data dengan baik untuk menghindari redundansi dan memastikan integritas data.
    - Normalisasi basis data relasional untuk mengurangi duplikasi dan memperbaiki struktur tabel.

4. **Keamanan dan Performa**:
    - Pertimbangkan keamanan data dan performa kueri saat memilih basis data.

5. **Pemantauan dan Pemeliharaan**:
    - Lakukan pemantauan secara berkala untuk memastikan kinerja dan keamanan basis data.
    - Cadangkan data secara teratur untuk menghindari kehilangan informasi.

**Referensi**
- https://appmaster.io/id/blog/merancang-database-e-niaga
- https://www.academia.edu/25694895/Integrasi_Data_Terstruktur_dan_Tidak_Terstruktur_dalam_Sistem_Inteligensi_Bisnis
