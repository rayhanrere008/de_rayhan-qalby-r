## Soal Prioritas 2 OOP

Memperluas sistem manajemen pusat kebugaran dengan menambahkan fitur khusus untuk berbagai jenis kelas latihan, seperti Yoga dan Angkat Beban, dengan fokus pada detail lanjutan dari inheritance dan polymorphism.

1. Desain Kelas Turunan Lanjutan:
    - Buat kelas Yoga dan AngkatBeban yang mewarisi dari KelasLatihan.
    - Tambahkan atribut dan metode khusus untuk setiap kelas. Misalnya, Yoga mungkin memiliki atribut seperti tingkatKesulitan dan AngkatBeban mungkin memiliki beratMaksimum.
2. Implementasi Polymorphism:
    - Modifikasi metode tampilkanInfo() di Yoga dan AngkatBeban untuk menampilkan informasi spesifik kelas tersebut.
    - Demonstrasi penggunaan polymorphism dengan membuat array KelasLatihan yang berisi objek Yoga dan AngkatBeban, dan menampilkan informasi mereka menggunakan metode tampilkanInfo() yang telah di-modifikasi.
3. Desain Metode Khusus:
    - Implementasikan metode khusus dalam Yoga dan AngkatBeban, seperti aturPosisiYoga() untuk Yoga dan aturBeratBeban() untuk AngkatBeban.
    - Demonstrasi bagaimana metode ini digunakan dalam konteks objek masing-masing.
4. Demonstrasi Polymorphism Lanjutan:
    - Buat fungsi yang menerima objek KelasLatihan dan memanggil metode khusus berdasarkan tipe kelasnya. Gunakan isinstance() untuk menentukan tipe kelas dan memanggil metode yang sesuai.

**Jawab :**

**1, 2, dan 3:**

**Code :**

![Gambar Code No 1, 2, dan 3](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-2/Code_desain-kelas-turunan-lanjutan.png?raw=true)

Class Yoga dan AngkatBeban mewarisi dari kelas KelasLatihan dan menambahkan atribut tingkat kesulitan yang spesifik untuk kelas yoga dan menambahkan atribut berat maksimum yang spesifik untuk kelas angkat beban.Memiliki metode aturPosisiYoga() yang khusus untuk mengatur posisi yoga. Memiliki metode aturBeratBeban() yang khusus untuk mengatur berat beban. Fungsi cekInfoKelasLatihan(): Ini adalah fungsi yang menerima objek KelasLatihan sebagai parameter. Fungsi ini menggunakan polymorphism untuk memeriksa tipe objek dan memanggil metode khusus berdasarkan tipe objeknya.

**Demonstrasi Polymorphism Lanjutan :**

**Code :**

![Gambar Code Demonstrasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-2/Code_demonstrasi.png?raw=true)

Dalam bagian ini, objek Yoga dan AngkatBeban dibuat, dan fungsi cekInfoKelasLatihan() dipanggil untuk menampilkan informasi kelas latihan dan memanggil metode khusus sesuai dengan jenis kelas latihan tersebut.

**Output :**

![Gambar Output](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/06_Object-Oriented-Programming/screenshots/Prioritas-2/Output.png?raw=true)

Outputnya akan menampilkan seluruh informasi kelas latihan dengan tambahan hasil dari metode khusus sesuai dengan jenis kelas latihan tersebut.