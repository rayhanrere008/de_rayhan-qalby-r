## Soal Prioritas 1 dan Jawaban - Data Transformation

![Gambar Konsep Soal](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/Gambar_soal.png?raw=true)

1. Analisis dan Transformasi Data Listing Rumah:
    - Import Library yang dibutuhkan seperti sklearn, pandas, re

        ![Gambar Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/01_Install-library-sklearn.png?raw=true)
    
    - Menerapkan function: 

        ![Gambar Code Function](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/02_terapkan_function.png?raw=true)

        **Fungsi ini digunakan untuk membersihkan string dari karakter yang tidak diinginkan dan mengonversinya menjadi nilai float, dengan memperlakukan nilai NaN pada string kosong.**
    
    - Load data dari file csv:

        ![Gambar Load data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/03_load_data_file_csv.png?raw=true)

    - Normalisasi Data: Normalisasi harga rumah dan harga per meter persegi menggunakan teknik Min-Max.

        ![Gambar Code Bersihkan dan konversi kolom](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/04_Code-bersihkan-dan-konversi-kolom.png?raw=true)

        **Keseluruhan kode ini membersihkan dan mengonversi nilai dalam kolom 'Price' dan 'Price_1m2' menjadi nilai float, serta mengganti nilai NaN dengan nilai yang diinginkan, dalam hal ini adalah 0**

        ![Gambar Code Lakukan Normalisasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/05_Code-lakukan-normalisasi.png?raw=true)

        **keseluruhan code tersebut adalah untuk memilih kolom-kolom yang akan dinormalisasi, kemudian melakukan normalisasi pada kolom-kolom tersebut menggunakan metode Min-Max Scaler, dan akhirnya mencetak nama-nama kolom yang telah dinormalisasi.**

    - Encoding Data Kategorikal: Terapkan one-hot encoding pada kolom 'Category', 'title_deed', 'repair', dan 'mortgage'.

        ![Gambar Code Lakukan Enconding](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/06_Code-lakukan-enconding.png?raw=true)

        **Jadi, keseluruhan code ini adalah untuk melakukan one-hot encoding pada kolom-kolom tertentu dalam DataFrame 'df' yaitu kolom 'category', 'title_deed', 'repair', dan 'mortgage'**

    - Aggregasi Data: Hitung rata-rata, median, dan modus dari harga rumah berdasarkan jumlah kamar dan tipe bangunan.

        ![Gambar Code Lakukan Agregasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/07_Code-lakukan-agregasi.png?raw=true)

        **Jadi, keseluruhan code tersebut adalah untuk menambahkan kolom baru 'building_type' berdasarkan kondisi dari kolom boolean 'category_Köhnə tikili' dan 'category_Yeni tikili', lalu melakukan aggregasi data berdasarkan kolom 'room_number' dan 'building_type', dan terakhir mencetak data hasil aggregasi.**
    
    - Hasil Output Agregasi :

        ![Gambar Output Agregasi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-1/08_Output-hasil-agregasi.png?raw=true)

        **terlihat hasil rata-rata, median, dan modus dari harga rumah berdasarkan jumlah kamar(room_number) dan tipe bangunan(building_type).**