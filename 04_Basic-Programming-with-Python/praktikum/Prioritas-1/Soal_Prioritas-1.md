1. Buatlah sebuah program untuk menghitung luas persegi panjang. Kemudian dari hasil perhitungan luas tersebut tampilkan tulisan **“even rectangle”** jika luas merupakan bilangan genap dan tampilkan tulisan **“odd rectangle”** jika luas merupakan bilangan ganjil. Rumus perhitungan luas persegi panjang adalah sebagai berikut:

    L = p \times l

    **Jawab :**

    **Code :**

    ![Gambar Code Menghitung Luas Persegi Panjang](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Prioritas-1/1_Code-hitungLuasPersegiPanjang.png?raw=true)

    **Disitu fungsi pertama 'hitung_luas_persegi_panjang(p, l)' adalah mengambil parameter p dan l untuk dihitung luasnya dan disimpan dalam parameter L lalu hasilnya akan dikembalikan dengan perintah return. Fungsi 'cek_kelipatan(L)' mengambil parameter L untuk menentukan apakah luas tersebut bilangan genap atau ganjil. Disitu pengguna harus menginput p dan l agar bisa menghasilkan output dari print memanggil function tadi.**

    **Output :** 

    ![Output Menghitung Luas Persegi Panjang](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Prioritas-1/1_Output-hitungLuasPersegiPanjang.png?raw=true)

    **Output yang dihasilkan adalah even rectangle karena luas nya merupakan bilangan genap.**


2. Buatlah sebuah program untuk menghitung volume bola. Volume tabung dapat dihitung dengan rumus berikut:

    V = \frac{4}{3}\pi r^3

    Catatan: gunakan nilai Phi  = 3.14

    **Jawab :**

    **Code :** 

    ![Gambar Code Menghitung Volume Bola](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Prioritas-1/2_Code-hitungVolumeBola.png?raw=true)

    **Dari gambar tersebut nilai phi diinisialisasikan terlebih dahulu. fungsi 'hitung_volume_bola(r)' mengambil parameter r untuk dilakukan perhitungan sehingga menghasil variabel V yang kemudian dikembalikan menggunakan perintah return. Disini pengguna melakukan input r yang akan dimasukkan ke dalam function tadi dan dilakukan print untuk menghasilkan volume bola (V).**

    **Output :**

    ![Output Menghitung Volume Bola](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Prioritas-1/2_Output-hitungVolumeBola.png?raw=true)

    **Disitu saya memasukkan r = 3, sehingga menghasilkan volume bola = 113,039**


3. Buatlah sebuah program yang mencetak angka dari 1 sampai 100 dengan kriteria sebagai berikut:
    - Jika bilangan merupakan kelipatan 3 maka tampilkan hasil kuadrat dari bilangan tersebut.
    - Jika bilangan merupakan kelipatan 5 maka tampilkan hasil perpangkatan 3 dari bilangan tersebut.
    - Jika bilangan merupakan kelipatan 3 dan 5 maka tampilkan tulisan “buzz”
    - Jika tiga kriteria diatas tidak terpenuhi maka tampilkan bilangan aslinya.

    **Jawab :**

    **Code :** 

    ![Gambar Code Cetak Angka](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Prioritas-1/3_Code-cetakAngka.png?raw=true)

    **Kode tersebut adalah sebuah loop for yang iterasi dari 1 hingga 100 (termasuk 1 dan 100). Di setiap iterasi, program memeriksa apakah nilai i habis dibagi oleh 3 dan/atau 5 dengan menggunakan operator modulus (%).**

    **Output :**

    ![Output Cetak Angka](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Prioritas-1/3_Output-cetakAngka.png?raw=true)
