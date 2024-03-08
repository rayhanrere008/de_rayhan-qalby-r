## Soal Eksploraasi dan Jawaban (Data Structure & Algorithm)

1. Buatlah sebuah program sederhana untuk mengelola data pengeluaran. Fitur program terdiri dari:
    - Menambahkan data pengeluaran.
    - Melihat semua data pengeluaran beserta total pengeluaran secara keseluruhan.
    - Mengubah data pengeluaran.
    - Menghapus data pengeluaran.
        
- Berikut adalah kriteria tambahan:
    - Menggunakan UUID sebagai identifier data pengeluaran.

**Jawab :**

**Menu utama**

**Code :**

![Gambar Code Menu Utama](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Code-menu-utama.png?raw=true)

**main()**: Fungsi utama dari program. Ini adalah tempat di mana menu utama ditampilkan dan input pengguna diproses. Selama program berjalan, pengguna akan terus diberikan menu untuk memilih aksi yang ingin dilakukan. Program akan berjalan terus sampai pengguna memilih untuk keluar (pilihan 5).
- Saat pengguna memilih pilihan 1-4, fungsi yang sesuai akan dipanggil.
- Jika pengguna memilih pilihan 5, program akan mencetak pesan "Bye..." dan keluar dari loop while, sehingga mengakhiri program.

**Output :**

![Output Menu Utama](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Menu-utama.png?raw=true)

Outputnya akan menampilkan menu utama dari program ada 5 pilihan.

**Menambah data pengeluaran**

**Code :**

![Gambar Code Menambah Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Code_menambah-data.png?raw=true)

Import **uuid**: Mengimpor modul uuid yang digunakan untuk menghasilkan UUID (Universal Unique Identifier) yang unik untuk setiap data pengeluaran yang dibuat. **create_expense()**: Fungsi ini meminta pengguna untuk memasukkan nama dan jumlah pengeluaran, kemudian membuat sebuah dictionary yang berisi ID pengeluaran (digenerate menggunakan UUID), nama, dan jumlah pengeluaran. Data ini kemudian ditambahkan ke dalam daftar **expenses**.

**Output :**

![Output Menambah Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Menambahkan-data-pengeluaran.png?raw=true)

![Output Menambah Data 2](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Menambahkan-data-pengeluaran2.png?raw=true)

Disini saya memilih angka 1 untuk melakukan penambahan data. Data pertama yaitu sarapan dengan amount = 15000 dan data kedua yaitu jajan dengan amount = 5000.

**Melihat data pengeluaran**

**Code :**

![Gambar Code Melihat Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Code_melihat-data.png?raw=true)

**view_expenses()**: Fungsi ini mencetak semua data pengeluaran beserta total pengeluaran keseluruhan dengan mengiterasi melalui setiap item dalam daftar **expenses**.

**Output :**

![Output Melihat Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Melihat-data-pengeluaran.png?raw=true)

Outputnya akan menampilkan 2 data yang telah ditambahkan tadi yaitu sarapan dan jajan serta akan menampilkan UUID dari masing-masing expenses. Di akhir akan menampilkan total dari keseluruhan daftar yang ada di expenses.

**Mengubah data pengeluaran**

**Code :**

![Gambar Code Mengubah Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Code_mengubah-data.png?raw=true)

**update_expense()**: Fungsi ini memungkinkan pengguna untuk memperbarui data pengeluaran berdasarkan ID yang diberikan. Pengguna diminta untuk memasukkan ID pengeluaran yang ingin diubah, lalu diminta untuk memasukkan nama dan/atau jumlah baru. Jika pengguna tidak memasukkan nilai baru, nilai yang ada akan tetap.

**Output :**

![Output Mengubah Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Mengubah-data-pengeluaran.png?raw=true)

Disini saya memasukkan id data yang ingin diubah dengan nama baru, Saya mengubah menjadi "Makan Siang" dengan amount = 30000.

![Output Lihat Data Setelah Diubah](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/After-mengubah-data.png?raw=true)

Kemudian saya mengecek apakah data berhasil diubah dengan memilih 2 (lihat data). Maka akan muncul perubahan yang awalnya data sarapan menjadi data "Makan Siang".

**Menghapus data pengeluaran**

**Code :**

![Gambar Code Menghapus Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Code_menghapus-data.png?raw=true)

**delete_expense()**: Fungsi ini memungkinkan pengguna untuk menghapus data pengeluaran berdasarkan ID yang diberikan. Pengguna diminta untuk memasukkan ID pengeluaran yang ingin dihapus, dan jika ID tersebut ditemukan dalam daftar **expenses**, item tersebut akan dihapus dari daftar.

**Output :**

![Output Menghapus Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Menghapus-data.png?raw=true)

Disini saya memilih pilihan 4 untuk melakukan penghapusan data. Kemudian memasukkan id dari daftar expenses yang ingin dihapus.

![Output Lihat Data Setelah Dihapus](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/After-menghapus-data.png?raw=true)

Kemudian saya mengecek apakah data berhasil dihapus dengan memilih 2 (lihat data). Maka data yang saya masukkan id nya tadi telah dihapus dan tersisa data "jajan".

**Keluar dari Aplikasi**

**Output :**

![Output Keluar Aplikasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Eksplorasi/Keluar-dari-aplikasi.png?raw=true)

Disini saya memilih pilihan 5 untuk keluar dari aplikasi. Maka akan menampilkan kalimat "Bye..."