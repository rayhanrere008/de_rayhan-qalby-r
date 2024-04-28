**Hasil Prompting**

Input :
```
"Buatkan SQL query untuk menghitung total penjualan per kategori produk setiap bulan dari tabel yang terdiri dari kolom Tanggal_Transaksi, Jumlah_Penjualan, Harga, Kategori_Produk.",

"Buatkan SQL query untuk menampilkan tanggal transaksi dengan jumlah penjualan tertinggi dari tabel yang terdiri dari kolom Tanggal_Transaksi, Jumlah_Penjualan, Harga, Kategori_Produk.",

"Buatkan SQL query untuk menghitung total pendapatan per bulan dari tabel yang terdiri dari kolom Tanggal_Transaksi, Jumlah_Penjualan, Harga, Kategori_Produk."
```
Output :

```
Response 1: SELECT MONTH(Tanggal_Transaksi) AS Bulan, Kategori_Produk, SUM(Jumlah_Penjualan * Harga) AS Total_Penjualan
FROM nama_tabel
GROUP BY MONTH(Tanggal_Transaksi), Kategori_Produk;

Response 2: SELECT Tanggal_Transaksi, Jumlah_Penjualan
FROM nama_tabel
ORDER BY Jumlah_Penjualan DESC
LIMIT 1;

Response 3: Tentu, berikut adalah contoh SQL query untuk menghitung total pendapatan per bulan dari tabel yang memiliki kolom Tanggal_Transaksi, Jumlah_Penjualan, Harga, dan Kategori_Produk:

```sql
SELECT 
    YEAR(Tanggal_Transaksi) AS Tahun,
    MONTH(Tanggal_Transaksi) AS Bulan,
    SUM(Jumlah_Penjualan * Harga) AS Total_Pendapatan
FROM 
    nama_tabel
GROUP BY 
    YEAR(Tanggal_Transaksi), MONTH(Tanggal_Transaksi);

Pastikan untuk mengganti `nama_tabel` dengan nama tabel yang sesuai dengan struktur data Anda. Query ini akan mengelompokkan total pendapatan berdasarkan tahun dan bulan dari tanggal transaksi, dan kemudian menghitung jumlah penjualan dikalikan dengan harga untuk setiap baris data, lalu menjumlahkannya untuk mendapatkan total pendapatan per bulan.
```