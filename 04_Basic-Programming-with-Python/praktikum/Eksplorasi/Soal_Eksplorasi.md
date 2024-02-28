1. Buatlah sebuah program untuk memeriksa apakah sebuah kata adalah anagram dari suatu kata yang lain. Anagram merupakan sebuah kata yang memiliki frekuensi huruf yang sama dengan kata lain.

Contoh dari anagram adalah sebagai berikut:

- Kata **pulsa** merupakan anagram dari kata **palsu** karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.
- Kata **kasur** merupakan anagram dari kata **rusak** karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.
- Kata **donat bukan** merupakan anagram dari kata **donatello** karena jumlah frekuensi huruf pada dua kata tersebut beda.

**Test case**
Input:

- Kata pertama: kasur
- Kata kedua: rusak

Output:
Anagram

Pembahasan: kata kasur merupakan anagram dari kata rusak karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.

**Jawab :**
Code : 

![Gambar Code Cek Anagram](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/04_Basic-Programming-with-Python/screenshots/Eksplorasi/Code-cekAnagram1.png?raw=true)
![Gambar Code Cek Anagram](/screenshots/Eksplorasi/Code-cekAnagram2.png)

**Fungsi 'cek_anagram(kata1, kata2)' digunakan untuk mengambil parameter yaitu kata1, kata2. Kedua kata diubah menjadi lowercase dan no spasi agar menghasilkan perbadingan yang tepat. Selanjutnya, program menghitung frekuensi setiap huruf pada kata1 menggunakan kamus (dictionary) frekuensi. Kemudian, frekuensi huruf pada kata2 dibandingkan dengan frekuensi dari kata1. Jika ditemukan perbedaan, maka dikembalikan nilai False karena tidak mungkin merupakan anagram. Terakhir, program memastikan bahwa setiap huruf pada kata1 dan kata2 memiliki frekuensi yang sama, sehingga merupakan anagram.**

Output :

![Output Cek Anagram](/screenshots/Eksplorasi/Output-cekAnagram.png)

**Disitu saya memasukkan kata1 = kasur, kata2 = rusak. Sehingga input tersebut akan menghasilkan output "Anagram".**

