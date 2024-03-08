## Soal Prioritas 2 dan Jawaban (Data Structure & Algorithm)

1. Buatlah sebuah program untuk memasukkan sekumpulan karakter dari sebuah kata berdasarkan ruangan yang tersedia. Mekanisme dapat dilihat pada gambar berikut:

    Test Case 1:

    - Input:
        - Word: alta
        - Rooms: 10
    - Output: altaaltaal

    Test Case 2:

    - Input:
        - Word: sepulsa
        - Rooms: 20
    - Output: sepulsasepulsasepuls

**Jawab :**

**Code :**

![Gambar Code Program Karakter](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-2/Code-1-programKarakter.png?raw=true)

Fungsi **collect_chars** ini mengambil dua parameter: **word** adalah kata yang ingin diulangi untuk memenuhi jumlah ruangan yang diberikan, dan **rooms** adalah jumlah ruangan yang tersedia. Ini menghitung berapa kali kata harus diulang **(repeat_count)** untuk mencapai jumlah ruangan yang diperlukan. Kemudian, string hasil dibuat dengan menggabungkan kata yang diulang sebanyak **repeat_count** kali. Sisa ruangan yang belum terpenuhi ditambahkan dengan mengambil sejumlah karakter dari awal kata.

**Output :**

![Output Program Karakter](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-2/Output-1.png?raw=true)

Output yang dihasilkan sesuai dengan output testcasenya.


2. Buatlah segiempat berukuran height x width yang berisikan bilangan bilangan prima setelah start, pada bagian akhir jumlahkan seluruh bilangan prima tersebut.

**Jawab :**

**Code :**

![Gambar Code segiempat Prima](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-2/Code-2-segiempatPrima.png?raw=true)

![Gambar Code segiempat Prima 2 ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-2/Code-2-segiempatPrima2.png?raw=true)

Fungsi **is_prime(num)** adalah fungsi bantuan yang memeriksa apakah suatu angka **num** adalah bilangan prima atau bukan. Fungsi ini mengembalikan **True** jika **num** adalah bilangan prima, dan **False** jika tidak. Fungsi **next_prime(num)** adalah fungsi bantuan yang mengembalikan bilangan prima berikutnya setelah **num**. Fungsi ini terus meningkatkan nilai **num** dan memeriksa apakah setiap nilai tersebut adalah bilangan prima dengan menggunakan fungsi **is_prime**. Ketika ditemukan bilangan prima, bilangan itu dikembalikan. Fungsi utama **prime_rectangle(height, width, start)** menciptakan matriks berukuran **height** kali **width** dan mengisinya dengan bilangan prima yang dihasilkan dengan menggunakan fungsi **next_prime**, dimulai dari bilangan **start**. Setiap baris dalam matriks adalah rangkaian bilangan prima yang dipisahkan oleh spasi. Setelah menciptakan matriks, total dari semua bilangan prima dihitung. Hasil matriks dan total dari semua bilangan prima dicetak sebagai output.

**Output :**

![Output segiempat Prima](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-2/Output-2.png?raw=true)

Output yang dihasilkan sama dengan testcase dengan memiliki jumlah keseluruhan bilangan yang sama pada output 1 dan 2.
