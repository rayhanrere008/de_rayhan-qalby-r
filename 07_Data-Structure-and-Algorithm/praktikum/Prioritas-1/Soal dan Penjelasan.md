## Soal Prioritas 1 dan Jawaban (Data Structure & Algorithm)

1. Buatlah sebuah program untuk mengelompokkan sekumpulan bilangan berdasarkan target kelipatan yang diinginkan:

    Test Case 1:

- Input:
    - Numbers: [1,2,3,4,5,6,7,8,9]
    - Target: 3
- Output: [[3, 6, 9], [1, 2, 4, 5, 7, 8]]

    Test Case 2:

- Input:
    - Numbers: [23,15,19,20,75,30,45]
    - Target: 5
- Output: [[15, 20, 75, 30, 45], [23, 19]]

**Jawab :**

**Code :**

![Gambar Code Pengelompokkan Bilangan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-1/Code_1-pengelompokkanBilangan.png?raw=true)

Fungsi **group_numbers** menerima dua parameter: **numbers** (sekumpulan bilangan yang akan dikelompokkan) dan **target** (nilai kelipatan yang diinginkan untuk pengelompokkan). Dua list kosong, **multiples** dan **non_multiples**, dibuat untuk menyimpan bilangan yang merupakan kelipatan dari **target** dan yang bukan. Selanjutnya, dilakukan iterasi melalui setiap bilangan dalam **numbers**. Untuk setiap bilangan, diperiksa apakah ia merupakan kelipatan dari **target** dengan menggunakan operator modulo (%). Jika hasil modulo dari bilangan tersebut terhadap **target** adalah 0, maka bilangan tersebut merupakan kelipatan, dan akan dimasukkan ke dalam list **multiples**. Jika tidak, maka bilangan tersebut dimasukkan ke dalam list **non_multiples**. List **multiples** dan **non_multiples** dikembalikan sebagai list yang berisi dua list tersebut.

**Output :**

![Output Pengelompokkan Bilangan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-1/Output-1.png?raw=true)

Output pertama menghasilkan pengelompokkan kelipatan 3 dan sisanya, untuk output kedua menghasilkan pengelompokkan kelipatan 5 dan sisanya.



2. Sebuah perusahaan roti ingin menentukan jenis roti yang dibuat berdasarkan jumlah tepung yang tersedia. Buatlah sebuah program untuk menentukan jenis roti yang dapat dibuat berdasarkan jumlah tepung yang tersedia.

    Test Case 1:

- Input:
    - Flour stock: 100
    - Breads: [{"name":"donut","flour":25},{"name":"mini puff","flour":15},{"name":"baguette","flour":75},{"name":"cupcake","flour":15}]
- Output: tampilkan jenis roti yang dapat dibuat
    - ['mini puff', 'cupcake', 'donut']

**Jawab :**

**Code :**

![Gambar Code Tentukan Jenis Roti](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-1/Code-2-tentukanJenisRoti.png?raw=true)

Fungsi **get_breads(breads, flour_stock)** didefinisikan untuk menerima dua parameter. **breads.sort(key=lambda x: x['flour'])**: Pertama-tama, daftar roti disortir menggunakan metode **sort()** dengan menggunakan lambda function sebagai kunci pengurutan. Lambda function ini akan mengambil setiap elemen dalam daftar dan mengembalikan nilai jumlah tepung yang dibutuhkan. Ini berarti daftar roti akan diurutkan berdasarkan jumlah tepung yang dibutuhkan untuk membuatnya, dari yang terkecil hingga yang terbesar. Kita inisialisasi sebuah variabel **result** sebagai daftar kosong yang akan menampung nama roti yang dapat dibuat. Kemudian, kita melakukan iterasi melalui setiap roti dalam daftar breads. Akhirnya, setelah iterasi selesai, daftar **result** yang berisi nama-nama roti yang dapat dibuat dikembalikan.

**Output :**

![Output Tentukan Jenis Roti](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/07_Data-Structure-and-Algorithm/screenshots/Prioritas-1/Output-2.png?raw=true)

Output diatas menghasilkan jenis roti yang dapat dibuat untuk tepung yang tersedia 100 dan 75.