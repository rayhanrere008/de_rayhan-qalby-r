## Soal Eksplorasi - Data Warehouse and Data Lake

1. Gunakan dataset berikut untuk melakukan proses kueri dengan menggunakan Google BigQuery. Lakukan berbagai kueri berikut:
    - Tampilkan rata-rata dari kepuasan mentor (mentor_satisfaction_score) secara keseluruhan.
    - Tampilkan rata-rata dari kepuasan CS (cs_satisfaction_score) secara keseluruhan.
    - Tampilkan rata-rata dari kepuasan mentor untuk “Course A”.
    - Tampilkan nilai terendah dari kepuasan belajar (learning_satisfaction_score) untuk “Course C”.
    - Tampilkan nilai tertinggi dari kepuasan CS (cs_satisfaction_score) untuk “Course B”.
    - Tampilkan nama course dengan rata-rata kepuasan mentor tertinggi.
    - Tampilkan nama course dengan rata-rata kepuasan belajar tertinggi.

**Jawaban :**

1. **Tampilkan rata-rata dari kepuasan mentor (mentor_satisfaction_score) secara keseluruhan.**

    ![Gambar Kueri Rata-rata Kepuasan Mentor](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/01_rata-rata_kepuasan-mentor.png?raw=true)

    Terlihat bahwa rata-rata kepuasan mentor secara keseluruhan adalah 8,63999..

2. **Tampilkan rata-rata dari kepuasan CS (cs_satisfaction_score) secara keseluruhan.**

    ![Gambar Kueri Rata-rata Kepuasan CS](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/02_rata-rata_kepuasan-CS.png?raw=true)

    Terlihat bahwa rata-rata kepuasan CS secara keseluruhan adalah 6,94666..

3. **Tampilkan rata-rata dari kepuasan mentor untuk “Course A”**

    ![Gambar Kueri Rata-rata Kepuasan Mentor Course A](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/03_rata-rata_kepuasan-mentor-course-A.png?raw=true)

    Terlihat bahwa rata-rata kepuasan mentor untuk course A adalah 7,7999..

4. **Tampilkan nilai terendah dari kepuasan belajar (learning_satisfaction_score) untuk “Course C”**

    ![Gambar Kueri Nilai Terendah Kepuasan Belajar Course C](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/04_nilai-terendah-kepuasan-belajar-course-C.png?raw=true)

    Terlihat bahwa nilai terendah kepuasan belajar course C adalah 8

5. **Tampilkan nilai tertinggi dari kepuasan CS (cs_satisfaction_score) untuk “Course B”**

    ![Gambar Kueri Nilai Tertinggi Kepuasan CS Course B](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/05_nilai-tertinggi-kepuasan-CS-course-B.png?raw=true)

    Terlihat bahwa nilai tertinggi kepuasan CS course B adalah 8

6. **Tampilkan nama course dengan rata-rata kepuasan mentor tertinggi**

    ![Gambar Kueri Course dengan Kepuasan Mentor Tertinggi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/06_course-dengan-kepuasan-mentor-tertinggi.png?raw=true)

    Disini saya mengambil 3 data dengan Course yang memiliki Kepuasan Mentor tertinggi yaitu Course E, C, dan B.

7. **Tampilkan nama course dengan rata-rata kepuasan belajar tertinggi.**

    ![Gambar Kueri Course dengan Kepuasan Belajar Tertinggi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Eksplorasi/07_course-dengan-kepuasan-belajar-tertinggi.png?raw=true)

    Disini saya mengambil 3 data dengan Course yang memiliki Kepuasan Belajar tertinggi yaitu Course C, B, dan E.