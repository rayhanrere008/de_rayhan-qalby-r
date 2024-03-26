-- Tabel Motor
CREATE TABLE motor (
    id_motor BIGSERIAL PRIMARY KEY,
    jenis_motor VARCHAR(100) NOT NULL,
    merek VARCHAR(100) NOT NULL,
    tahun_pembuatan INTEGER NOT NULL,
    status_ketersediaan BOOLEAN,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);
SELECT create_distributed_table('motor', 'id_motor');

-- Tabel Pelanggan
CREATE TABLE pelanggan (
    id_pelanggan BIGSERIAL PRIMARY KEY,
    nama VARCHAR(100),
    alamat TEXT,
    no_telepon VARCHAR(20),
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);
SELECT create_distributed_table('pelanggan', 'id_pelanggan');

-- Tabel Penyewaan
CREATE TABLE penyewaan (
    id_penyewaan BIGSERIAL PRIMARY KEY,
    id_motor BIGINT,
    id_pelanggan BIGINT,
    tanggal_mulai_sewa DATE NOT NULL,
    tanggal_selesai_sewa DATE NOT NULL,
    total_biaya NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);
SELECT create_distributed_table('penyewaan', 'id_penyewaan');

-- Tabel Kepuasan Pelanggan
CREATE TABLE kepuasan_pelanggan (
    id_kepuasan BIGSERIAL PRIMARY KEY,
    id_penyewaan BIGINT,
    rating_kepuasan INTEGER NOT NULL,
    komentar TEXT NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);
SELECT create_reference_table('kepuasan_pelanggan');

-- Add Data Motor
INSERT INTO motor(jenis_motor, merek, tahun_pembuatan, status_ketersediaan) 
VALUES ('Sport', 'Honda', 2022, true),
    ('Scooter', 'Yamaha', 2023, false),
    ('Cub', 'Suzuki', 2021, true);

-- Add Data Pelanggan
INSERT INTO pelanggan(nama, alamat, no_telepon) 
VALUES ('Ganesya', 'Wonokusumo', 082367),
    ('Sopyan', 'Kedinding', 0876554);

-- Add Data Penyewaan
INSERT INTO penyewaan(id_motor, id_pelanggan, tanggal_mulai_sewa, tanggal_selesai_sewa, total_biaya) 
VALUES (1, 1, '2024-03-25', '2024-03-26', 150000.00),
    (2, 2, '2024-03-26', '2024-03-29', 200000.00),
    (3, 2, '2024-03-27', '2024-03-28', 350000.00);

-- Add Data Kepuasan_Pelanggan
INSERT INTO kepuasan_pelanggan(id_penyewaan, rating_kepuasan, komentar) 
VALUES (1, 8, 'Motornya bagus kuat untuk tanjakan'),
    (2, 9, 'Bensinnya sangat hemat'),
    (3, 6, 'Knalpot motornya sangat berisik');

-- Kueri Menampilkan Penggunaan Kendaraan Bermotor
SET citus.enable_repartition_joins= TRUE;
SELECT p.id_penyewaan, m.jenis_motor, p.id_pelanggan
FROM penyewaan p
JOIN motor m ON p.id_motor = m.id_motor;

-- Kueri Menampilkan Kepuasan Pelanggan
SET citus.enable_repartition_joins= TRUE;
SELECT k.id_kepuasan, k.id_penyewaan AS no_penyewaan, pe.nama AS nama_penyewa, m.jenis_motor AS motor_yg_disewa, k.rating_kepuasan AS rating_sewa, k.komentar
FROM kepuasan_pelanggan k
JOIN penyewaan p ON k.id_penyewaan = p.id_penyewaan
JOIN pelanggan pe ON p.id_pelanggan = pe.id_pelanggan
JOIN motor m ON p.id_motor = m.id_motor;

-- Kueri Menampilkan Keuntungan Setiap Bulannya
SELECT DATE_TRUNC('month', tanggal_mulai_sewa) AS bulan,
       SUM(total_biaya) AS keuntungan
FROM penyewaan
GROUP BY DATE_TRUNC('month', tanggal_mulai_sewa)
ORDER BY bulan;