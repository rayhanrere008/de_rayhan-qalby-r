## Soal dan Jawaban Prioritas-2 - Big Data Technologies

1. Buatlah sebuah program untuk menghitung rata-rata dari setiap sekumpulan nilai dengan kriteria sebagai berikut:
    - Menggunakan [dataset](https://gist.github.com/nadirbslmh/d8a202195ba2908e2c04ee2ab66166a3) berikut.
    - Menggunakan Apache Hadoop MapReduce.

**Jawaban :**

- **Jalankan Hadoop nya terlebih dahulu :**

    ![Jalankan Hadoop](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/01_jalankan-hadoop.png?raw=true)

- **Buat file mapper dan reducernya :**

    ![Buat file mapper dan reducer](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/02_buat-file-mapper-dan-reducer.png?raw=true)

- **Masukkan codenya ke dalam file mapper :**

    ![Code file mapper](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/03_masukkan-isi-file-mapper.png?raw=true)

    **Jadi, secara keseluruhan, script ini membaca baris-baris input, memisahkan setiap baris menjadi pasangan key dan value berdasarkan koma, dan kemudian mencetak kembali pasangan tersebut dengan pemisah tab ke standard output.**

- **Berikan hak akses eksekusi ke dalam file mapper :**

    ![Berikan hak akses eksekusi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/04_berikan-hak-eksekusi-mapper.png?raw=true)

- **Masukkan codenya ke dalam file reducer :**

    ![Code file reducer](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/05_masukkan-isi-file-reducer.png?raw=true)

    **Jadi, secara keseluruhan, script ini membaca baris-baris input yang berisi pasangan kunci-nilai yang dipisahkan oleh tab (\t), menghitung rata-rata nilai-nilai yang terkait dengan setiap kunci, dan mencetak kunci beserta rata-rata nilai yang terkait.**

- **Berikan hak akses eksekusi ke dalam file reducer :**

    ![Berikan hak akses eksekusi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/06_berikan-hak-eksekusi-reducer.png?raw=true)

- **Buat Folder score dan beberapa file seperti score1.txt, score2.txt, score3.txt :**

    ![Buat Folder score](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/07_buat-folder-score-dan-nama-filenya.png?raw=true)

- **Isi semua file txt yang telah dibuat tadi dengan dataset yang telah ditentukan. File nya saya modifikasi seperti itu agar bisa sesuai dengan code programnya :**

    ![Isi file txt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/08_isi-file-score.txt-nya-sesuai-dataset.png?raw=true)

- **Copy folder dan filenya ke hdsf(hadoop) :**

    ![Copy folder](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/09_copy-filenya-ke-hadoop.png?raw=true)

- **Cek folder score apakan sudah tercopy :**

    ![Cek folder score](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/10_cek-folder-score.png?raw=true)

- **Jalankan mapreduce dengan Hadoop Streaming Jar :**

    ![Jalankan mapreduce](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/11_jalankan-mapreduce.png?raw=true)

- **Mapreduce Success :**

    ![Mapreduce Success](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/12_mapreduce-success.png?raw=true)

- **Cek hasil output_score :**

    ![Cek hasil output_score](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/13_cek-hasilnya.png?raw=true)

- **Hasil rata-rata setiap sekumpulan score:**

    ![Hasil rata-rata](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/18_Big-Data-Technologies/screenshots/Prioritas-2/14_hasil-rata-rata.png?raw=true)

    **Terlihat bahwa rata-rata setiap sekumpulan nilai atau score. score 1 = 80,74 , score 2 = 77,51 , score 3 = 76,48**