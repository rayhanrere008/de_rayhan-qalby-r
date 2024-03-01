## Soal Eksplorasi OOP

1. Desain Sistem Pemesanan:
    - Tambahkan metode pesanKelas() dan batalkanKelas() di kelas KelasLatihan.
    - Override metode tersebut di kelas Yoga dan AngkatBeban dengan aturan pemesanan dan pembatalan khusus.
2. Implementasi dan Demonstrasi:
    - Buat sistem yang memungkinkan pelanggan untuk memesan dan membatalkan kelas.
    - Demonstrasi kasus pemesanan dan pembatalan untuk Yoga dan AngkatBeban, menunjukkan bagaimana polimorfisme digunakan dalam kasus ini.

**Jawab :**

**Desain Sistem Pemesanan :**

**Code :**

![Gambar Code Metode pesanKelas dan batalkanKelas](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Code_desain-sistem-pemesanan.png?raw=true)

![Gambar Code Metode pemesanan kelas Yoga](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Code_desain-sistem-pemesanan-yoga.png?raw=true)

![Gambar Code Metode pemesanan kelas Angkat Beban](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Code_desain-sistem-pemesanan-angkatBeban.png?raw=true)

Metode pesanKelas() digunakan untuk memesan kelas latihan. Jika kelas tersedia, statusnya diubah menjadi tidak tersedia. Metode batalkanKelas() digunakan untuk membatalkan pemesanan kelas latihan. Jika kelas tidak tersedia, statusnya diubah menjadi tersedia kembali. Metode pesanKelas() dioverride untuk memeriksa apakah tingkat kesulitan yang diminta cocok dengan tingkat kesulitan kelas. Jika cocok, pesanan berhasil; jika tidak, pesan kesalahan ditampilkan. Metode pesanKelas() dioverride untuk memeriksa apakah berat maksimum yang dimasukkan oleh pelanggan tidak melebihi berat maksimum kelas. Jika berat maksimum cocok, pesanan berhasil; jika tidak, pesan kesalahan ditampilkan.

**Implementasi dan Demonstrasi :**

**Code :**

![Gambar Code Implementasi Sistem Pemesanan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Code_implementasi-sistem-pemesanan.png?raw=true)

![Gambar Code Demonstrasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Code_demonstrasi.png?raw=true)

Fungsi tampilkanMenu(): Fungsi ini digunakan untuk menampilkan menu pilihan kepada pengguna. Di dalam blok ini, objek Yoga dan AngkatBeban dibuat. Dilakukan loop utama untuk menampilkan menu pilihan kepada pengguna. Pengguna diminta untuk memilih opsi, seperti memesan atau membatalkan kelas. Berdasarkan pilihan pengguna, metode yang sesuai dipanggil pada objek kelas yang dipilih.

**Output :**

![Gambar Code Implementasi Sistem Pemesanan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Output_pemesanan-kelas.png?raw=true)

![Gambar Code Demonstrasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Eksplorasi/Output_pembatalan-kelas.png?raw=true)

Output diatas yang pertama menampilkan cara melakukan pemesanan kelas, disitu saya pilih kelas yoga dan akan menampilkan tingkat kesulitan yang dipilih kemudian pilih tingkat kesulitas Intermediate sehingga kelas yoga bisa didaftarkan.

Output yang kedua menampilkan cara pembatalan kelas, tampilan akan kembali ke menu utama pilih pembatalan kelas lalu pilih kelas yang dipesan tadi untuk dibatalkan, kemudian akan muncul kelas yang dipilih berhasil dibatalkan.

Hal ini berlaku juga saat proses pemesanan kelas Angkat Beban bedanya kelas tersebut harus input beban maksimal.