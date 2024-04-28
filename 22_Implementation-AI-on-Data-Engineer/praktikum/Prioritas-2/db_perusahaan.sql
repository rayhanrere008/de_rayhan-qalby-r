-- Membuat database db_perusahaan
CREATE DATABASE IF NOT EXISTS db_perusahaan;

-- Menggunakan database db_perusahaan
USE db_perusahaan;

-- Membuat tabel Penjualan di dalam database db_perusahaan
CREATE TABLE IF NOT EXISTS Penjualan (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Tanggal_Transaksi DATE,
    Jumlah_Penjualan INT,
    Harga INT,
    Kategori_Produk VARCHAR(255)
);

-- Memasukkan data ke dalam tabel Penjualan
INSERT INTO Penjualan (Tanggal_Transaksi, Jumlah_Penjualan, Harga, Kategori_Produk) VALUES
('2024-01-01', 10, 100000, 'Elektronik'),
('2024-01-05', 15, 150000, 'Pakaian'),
('2024-01-10', 20, 200000, 'Makanan'),
('2024-02-02', 12, 120000, 'Elektronik'),
('2024-02-06', 18, 180000, 'Pakaian'),
('2024-02-12', 22, 220000, 'Makanan'),
('2024-03-03', 14, 140000, 'Elektronik'),
('2024-03-07', 21, 210000, 'Pakaian'),
('2024-03-14', 25, 250000, 'Makanan'),
('2024-04-04', 16, 160000, 'Elektronik'),
('2024-04-08', 24, 240000, 'Pakaian'),
('2024-04-15', 28, 280000, 'Makanan'),
('2024-05-05', 18, 180000, 'Elektronik'),
('2024-05-09', 27, 270000, 'Pakaian'),
('2024-05-16', 30, 300000, 'Makanan');