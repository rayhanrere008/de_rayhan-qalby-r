**Hasil Prompting**

**Input :**
```
Buatkan kueri SQL untuk skema database media sosial
```

**Output :**
```
Tentu, berikut ini adalah contoh kueri SQL untuk membuat skema database sederhana untuk media sosial dengan tabel-tabel dasar seperti pengguna (users), posting (posts), dan komentar (comments):

-- Membuat tabel pengguna (users)
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    join_date DATE
);

-- Membuat tabel posting (posts)
CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    post_text TEXT,
    post_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Membuat tabel komentar (comments)
CREATE TABLE comments (
    comment_id INT PRIMARY KEY,
    post_id INT,
    user_id INT,
    comment_text TEXT,
    comment_date DATETIME,
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

Di sini:

- Tabel users menyimpan informasi tentang pengguna seperti ID, nama pengguna, email, kata sandi, dan tanggal bergabung.
- Tabel posts menyimpan posting pengguna, dengan kolom untuk ID posting, ID pengguna yang memposting, teks posting, dan tanggal posting.
- Tabel comments menyimpan komentar pada posting, dengan kolom untuk ID komentar, ID posting yang dikomentari, ID pengguna yang mengomentari, teks komentar, dan tanggal komentar.

Pastikan untuk menyesuaikan struktur skema database sesuai dengan kebutuhan Anda yang lebih spesifik.
```