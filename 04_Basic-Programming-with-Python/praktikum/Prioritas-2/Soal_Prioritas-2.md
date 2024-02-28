1. Buatlah sebuah program untuk menentukan tarif pengiriman paket berdasarkan berat paket dan jarak yang ditempuh dengan spesifikasi berikut:

|  Berat   |  Tarif   |
|----------|----------|
| 1 - 20   |  10000   |
| 21 - 30  |  15000   |
| 31 - 60  |  20000   |
| > 60     |  45000   |

|  Jarak   |  Tarif   |
|----------|----------|
| 1 - 5    |  2000    |
| 6 - 15   |  5000    |
| 16 - 30  |  10000   |
| > 30     |  15000   |

Tarif keseluruhan = tarif berdasarkan berat + tarif berdasarkan jarak

Input:

- Berat: 24
- Jarak: 10

Output: 20000

**Jawab :**
Code :

![Gambar Code Menghitung Tarif Paket](/screenshots/Prioritas-2/1_Code-hitungTarifPaket.png)

**Kode tersebut terdapat function 'hitung_tarif(berat, jarak)' dengan mengambil 2 parameter dengan kondisi tertentu lalu dihitung untuk menghasilkan total tarif yang kemudian dikembalikan hasil fungsinya. Pengguna harus menginput berat dan jarak untuk menghasilkan output dari print tarif (hasil perhitungan).**

Output :

![Output Menghitung Tarif Paket](/screenshots/Prioritas-2/1_Output-hitungTarifPaket.png)

**Disitu saya menginput berat = 24, jarak = 10. Sehingga menghasilkan tarif pengiriman sebesar 20000.**

2. Buatlah sebuah program untuk menentukan prioritas dari sebuah proyek berdasarkan budget, waktu pengerjaan dan tingkat kesulitan. Kriteria dari penentuan proyek adalah menggunakan skor secara keseluruhan. Perhitungan skor dari setiap faktor tersebut dihitung dengan kriteria berikut:

|  Budget  |   Skor   |
|----------|----------|
| 0 - 50   |  4       |
| 51 - 80  |  3       |
| 81 - 100 |  2       |
| > 100    |  1       |

| Waktu Pengerjaan | Skor |
|------------------|------|
| 0 - 20           |  10  |
| 21 - 30          |  5   |
| 31 - 50          |  2   |
| > 50             |  1   |

| Tingkat Kesulitan | Skor |
|-------------------|------|
| 0 - 3             |  10  |
| 4 - 6             |  5   |
| 8 - 10            |  2   |
| > 10              |  1   |

Hasil prioritas proyek diambil dari skor yang sudah dihitung.

|  Skor    |    Hasil    |
|----------|-------------|
| 24 - 17  |  High       |
| 16 - 10  |  Medium     |
| 9 - 3    |  Low        |
| <= 2     |  Impossible |

Test case:

Input:

- Budget: 51
- Waktu pengerjaan: 10
- Tingkat kesulitan: 3
        
Output: High

**Jawab :**
Code :

![Gambar Code Menghitung Prioritas Proyek](/screenshots/Prioritas-2/2_Code-hitungPrioritasProyek1.png)
![Gambar Code Menghitung Prioritas Proyek](/screenshots/Prioritas-2/2_Code-hitungPrioritasProyek2.png)

**Code ini memungkinkan pengguna untuk menentukan prioritas proyek berdasarkan tiga faktor utama (budget, waktu, kesulitan) berdasarkan kondisi tertentu. Lalu memanggil function 'hitung_prioritas()' yang dari isi inputan pengguna untuk dijadikan sebagai argumen untuk mencetak prioritas proyek.**

Output :

![Output Menghitung Prioritas Proyek](/screenshots/Prioritas-2/2_Output-hitungPrioritasProyek.png)

**Disini saya memasukkan budget = 51, waktu = 10, kesulitan = 3. Sehingga menghasilkan prioritas proyek = High.** 