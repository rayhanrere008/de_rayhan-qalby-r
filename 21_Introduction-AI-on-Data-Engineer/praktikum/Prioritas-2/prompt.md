**Hasil Prompting**

**Input :**
```
Implementasikan optimasi query SQL dari database media sosial tersebut seperti menerapkan indeksasi dan query tuning
```

**Output :**
```
Untuk mengoptimalkan kueri SQL pada skema database media sosial tersebut, kita dapat menerapkan indeksasi pada kolom-kolom yang sering digunakan dalam kueri dan melakukan tuning pada beberapa kueri agar lebih efisien. Berikut adalah contoh implementasi optimasi pada beberapa kueri:

Indeksasi:
- Kolom user_id pada tabel posts, comments, dan users akan sering digunakan dalam kueri JOIN, sehingga membuat indeks pada kolom ini akan meningkatkan performa.
- Kolom post_id pada tabel comments dan posts juga penting untuk diindeks, terutama jika sering digunakan dalam kueri JOIN atau WHERE.
- Kolom username dan email pada tabel users bisa diindeks jika sering digunakan dalam kueri pencarian berdasarkan nama pengguna atau email.

-- Membuat indeks
CREATE INDEX idx_user_id ON posts(user_id);
CREATE INDEX idx_user_id_comments ON comments(user_id);
CREATE INDEX idx_post_id_comments ON comments(post_id);
CREATE INDEX idx_post_id_posts ON posts(post_id);
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);

Tuning Kueri:
- Kueri yang membutuhkan JOIN antara tabel posts dan users atau antara comments dan users dapat dioptimalkan dengan memilih hanya kolom yang diperlukan dan menghindari penggunaan fungsi di dalam WHERE yang dapat memperlambat kueri.
- Contoh: Kueri untuk mendapatkan posting dan pengguna yang mempostingnya.

-- Tuning kueri
SELECT p.post_id, p.post_text, u.username
FROM posts p
JOIN users u ON p.user_id = u.user_id;

Dalam hal tuning kueri, selalu penting untuk melakukan pengujian dan analisis performa sebelum dan sesudah optimasi untuk memastikan bahwa perubahan yang diterapkan benar-benar meningkatkan kinerja kueri. Selain itu, perlu juga untuk mempertimbangkan ukuran data dan distribusi data yang sebenarnya untuk memastikan bahwa strategi indeksasi dan tuning kueri yang diterapkan relevan dengan lingkungan database yang spesifik.
```