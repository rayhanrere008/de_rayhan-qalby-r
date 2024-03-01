## Soal Prioritas 1 OOP

Sistem untuk mengelola aktivitas di sebuah pusat kebugaran, termasuk pelanggan, pelatih, dan berbagai kelas latihan.

1. Desain Kelas Pelanggan:
    - Buat kelas Pelanggan dengan atribut privat seperti nama, usia, dan ID pelanggan.
    - Implementasikan metode get dan set untuk setiap atribut (Encapsulation).
    - Tambahkan metode tampilkanInfo() untuk menampilkan informasi pelanggan (Data Abstraction).
2. Desain Kelas Pelatih:
    - Buat kelas Pelatih dengan atribut privat seperti nama, spesialisasi, dan tahun pengalaman.
    - Implementasikan metode get dan set serta tampilkanInfo() (Encapsulation dan Data Abstraction).
3. Desain Kelas KelasLatihan:
    - Buat kelas KelasLatihan yang mewarisi dari kelas Pelatih dan menambahkan atribut seperti jenis latihan dan jadwal (Inheritance).
    - Override metode tampilkanInfo() untuk menampilkan informasi tambahan (Polymorphism).
4. Demonstrasi:
    - Buat objek Pelanggan dan Pelatih, serta beberapa objek KelasLatihan.
    - Tampilkan informasi setiap objek menggunakan metode tampilkanInfo().

**Jawab :**

**Desain Kelas Pelanggan:**

**Code :**

![Gambar Code Desain Kelas Pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-1/Code_desain-kelas-pelanggan.png?raw=true)

Class pelanggan merepresentasikan objek pelanggan dengan atribut nama, usia, dan ID pelanggan. Class ini memiliki konstruktor (__init__) untuk inisialisasi objek, serta metode getter dan setter untuk mengakses dan mengubah nilai atribut. Pelanggan memiliki metode tampilkanInfo() untuk menampilkan informasi pelanggan.

**Desain Kelas Pelatih:**

**Code :**

![Gambar Code Desain Kelas Pelatih](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-1/Code_desain-kelas-pelatih.png?raw=true)

Class pelatih merepresentasikan objek pelatih dengan atribut nama, spesialisasi, dan tahun pengalaman. Class ini memiliki konstruktor (__init__) untuk inisialisasi objek, serta metode getter dan setter untuk mengakses dan mengubah nilai atribut. Pelatih juga memiliki metode serupa untuk menampilkan informasi pelatih.

**Desain Kelas KelasLatihan:**

**Code :**

![Gambar Code Desain Kelas KelasLatihan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-1/Code_desain-kelas-KelasLatihan.png?raw=true)

KelasLatihan: Mewarisi dari kelas Pelatih dan menambahkan atribut jenis latihan dan jadwal. Class ini memiliki konstruktor (__init__) untuk inisialisasi objek, serta metode getter dan setter untuk mengakses dan mengubah nilai atribut. KelasLatihan melakukan override pada metode tampilkanInfo() yang diwarisi dari kelas Pelatih, dan menambahkan informasi jenis latihan dan jadwal.

**Demonstrasi:**

**Code :**

![Gambar Code Demonstrasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-1/Code_demonstrasi.png?raw=true)

Di bagian bawah, dilakukan demonstrasi pembuatan objek dari setiap kelas dan pemanggilan metode tampilkanInfo() untuk menampilkan informasi masing-masing objek.

**Output :**

![Gambar Output 1](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-1/Output-1.png?raw=true)

![Gambar Output 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-1/Output-2.png?raw=true)

Ini merupakan hasil output yang menampilkan keseluruhan informasi mulai dari informasi pelanggan, pelatih, dan beberapa objek kelas latihan.