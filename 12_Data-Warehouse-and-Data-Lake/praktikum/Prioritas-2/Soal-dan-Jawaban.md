## Soal Prioritas 2 - Data Warehouse dan Data Lake

1. Sebuah perusahaan yang bergerak di bidang jasa penyewaan kendaraan bermotor ingin menerapkan penggunaan data warehouse dalam operasional bisnis. Data warehouse nantinya digunakan untuk menganalisis penggunaan kendaraan bermotor, kepuasan konsumen serta menganalisis keuntungan yang diperoleh setiap bulannya. Berdasarkan skenario tersebut buatlah rancangan skema database dalam bentuk diagram ERD. Rancangan dapat dibuat dengan menggunakan aplikasi draw.io atau aplikasi lainnya yang sejenis.

2. Berdasarkan diagram ERD yang sudah dibuat pada nomor 1, buatlah berbagai tabel dengan kriteria sebagai berikut:
    1. Menggunakan Citus dalam pembuatan tabel.
    2. Menerapkan replication.
    3. Menerapkan sharding.

**Jawaban :**

1. **Rancangan ERD dibuat dengan draw.io** :

    ![Gambar Rancangan ERD](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/Rancangan_ERD-Perusahaan-Jasa-Sewa-Motor.png?raw=true)

    Diatas merupakan gambar rancangan ERD untuk penyewaan kendaraan bermotor terdapat beberapa tabel yaitu tabel pelanggan, motor, penyewaan, dan kepuasan pelanggan serta memiliki relationshipnya masing-masing.

2. **Pembuatan Tabel motor dengan citus menerapkan sharding**

    ![Gambar Create Tabel Motor](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/01_Create-table-motor(Sharding).png?raw=true)

    Diatas merupakan kueri untuk melakukan pembuatan tabel motor dengan beberapa atribut seperti id_motor (primary key), jenis_motor, merek, tahun_pembuatan, status_ketersediaan, created_at, updated_at sesuai dengan tipe data yang ditentukan dengan menerapkan **sharding** dalam pembuatannya.

3. **Pembuatan Tabel penyewaan dengan citus menerapkan sharding**

    ![Gambar Create Tabel Penyewaan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/03_Create-table-penyewaan(Sharding).png?raw=true)

    Diatas merupakan kueri untuk melakukan pembuatan tabel penyewaan dengan beberapa atribut seperti id_penyewaan (primary key), id_pelanggan, id_motor, tanggal_mulai_sewa, tanggal_selesai_sewa, total_biaya, created_at, updated_at sesuai dengan tipe data yang ditentukan dengan menerapkan **sharding** dalam pembuatannya.

4. **Pembuatan Tabel kepuasan_pelanggan dengan citus menerapkan replication**

    ![Gambar Create Tabel Kepuasan_pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/04_Create-table-kepuasan-pelanggan(Replication).png?raw=true)

    Diatas merupakan kueri untuk melakukan pembuatan tabel kepuasan_pelanggan dengan beberapa atribut seperti id_kepuasan (primary key), id_penyewaan, rating_kepuasan, komentar, created_at, updated_at sesuai dengan tipe data yang ditentukan dengan menerapkan **replication** dalam pembuatannya.

5. **Insert data ke dalam tabel motor, pelanggan, penyewaan, kepuasan_pelanggan**

    ![Gambar Insert data to Tabel Motor](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/05_insert-data-motor.png?raw=true)

    ![Gambar Insert data to Tabel Pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/06_insert-data-pelanggan.png?raw=true)

    ![Gambar Insert data to Tabel Penyewaan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/07_insert-data-penyewaan.png?raw=true)

    ![Gambar Insert data to Tabel Kepuasan_Pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/08_insert-data-kepuasan_pelanggan.png?raw=true)

6. **Kueri Menampilkan Data Penggunaan Motor**

    ![Gambar Menampilkan Data Penggunaan Motor](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/09_Kueri-menampilkan-penggunaan-motor.png?raw=true)

    Gambar diatas merupakan kueri untuk menampilkan data penggunaan motor berdasarkan jenis_motor yang disewa dan siapa yang menyewanya(pelanggan).

7. **Kueri Menampilkan Data Kepuasan Konsumen**

    ![Gambar Menampilkan Data Kepuasan Konsumen](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/10_Kueri-menampilkan-kepuasan-penyewaan.png?raw=true)

    Gambar diatas merupakan kueri untuk menampilkan data kepuasan konsumen dalam melakukan penyewaan motor berdasarkan nama penyewa, jenis motor yang disewanya, rating, serta komentarnya.

8. **Kueri Menampilkan Data Keuntungan Setiap Bulannya**

    ![Gambar Menampilkan Data Keuntungan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-2/11_Kueri-menampilkan-keuntungan-setiap-bulannya.png?raw=true)

    Gambar diatas merupakan kueri untuk menampilkan data keuntungan setiap bulannya khususnya bulan maret berdasarkan tanggal_mulai_sewa dan perhitungan SUM(total_biaya).