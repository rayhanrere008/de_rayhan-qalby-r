## Soal Eksplorasi dan Jawaban - Big Data Technologies

1. Buatlah sebuah program untuk mengecek apakah sebuah kata termasuk palindrom atau bukan dengan kriteria sebagai berikut:
    - Menggunakan [dataset](https://gist.github.com/nadirbslmh/f82dc5240226b648db61dc431aeb22b4) berikut.
    - Menggunakan Apache Hadoop MapReduce.
    - Jika sebuah kata termasuk palindrom maka tampilkan nilai “True”. Jika tidak tampilkan “False”.

**Jawaban :**

- **Jalankan Hadoop nya terlebih dahulu :**

    ![Jalankan Hadoop](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/01_pastikan-hadoop-berjalan.png?raw=true)

- **Buat file mappernya :**

    ![Buat file mapper](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/02_buat-file-mapper.png?raw=true)

- **Masukkan code ke file mappernya :**

    ![Masukkan code](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/03_isi-file-mapper.png?raw=true)

    **Jadi, secara keseluruhan, script ini membaca baris-baris input, memeriksa apakah setiap kata merupakan palindrome, dan mencetak hasilnya dalam format "kata True/False"**

- **Berikan hak akses eksekusi ke file mapper :**

    ![Berikan hak akses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/04_berikan-akses-file-mapper.png?raw=true)

- **Buat folder word dan isi beberapa file seperti words_1.txt, words_2.txt, words_3.txt:**

    ![Buat folder word](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/05_buat-folder-dan-isi-filenya.png?raw=true)

- **Isi semua file txt sesuai dengan dataset yang telah ditentukan :**

    ![Isi semua file txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/06_isi-file-words.txt-nya.png?raw=true)

- **Copy direktori folder words dan isi filenya ke hdsf(hadoop) :**

    ![Copy direktori folder words](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/07_copy-direktori-words-dan-filenya.png?raw=true)

- **Jalankan mapreduce dengan Hadoop Streaming :**

    ![Jalankan mapreduce](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/08_jalankan-mapreduce.png?raw=true)

- **MapReduce Success :**

    ![MapReduce Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/09_mapreduce-success.png?raw=true)

- **Cek file output_words :**

    ![Cek file output_words](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/10_cek-file-output_words.png?raw=true)

- **Hasil output polindrom atau tidak :**

    ![Hasil output polindrom](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/11_hasil-polindrom-atau-tidak.png?raw=true)

    ![Hasil output polindrom](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/12_hasil-polindrom-atau-tidak2.png?raw=true)

    ![Hasil output polindrom](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Eksplorasi/13_hasil-polindrom-atau-tidak3.png?raw=true)

    **Terlihat bahwa kata yang menghasilkan "True" menandakan bahwa kata tersebut polindrom, jika "False" maka kata tersebut bukan polindrom.**