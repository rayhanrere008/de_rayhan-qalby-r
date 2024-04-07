## Soal Prioritas 2 dan Jawaban - Data Transformation

1. Mengatasi Tantangan Transformasi Data:
    - Install Library dna Import seperti pandas dan numpy

        ![Gambar Install Library dan Import](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/01_install_library_panda-numpy.png?raw=true)
    
    - Load data file house_listings.csv

        ![Gambar Load data csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/02_load_data_csv.png?raw=true)

    - Mengelola Nilai yang Hilang: Identifikasi dan imputasi nilai yang hilang pada kolom 'area' dan 'floor'. 

        ![Gambar imputasi nilai](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/03_Code-imputasi-nilai.png?raw=true)

        **Kedua kolom tersebut telah diubah, dan setiap nilai yang hilang telah diisi dengan nilai rata-rata. Penting untuk dicatat bahwa inplace=True tidak digunakan, yang berarti DataFrame tidak diubah secara langsung, melainkan membuat DataFrame baru yang dimodifikasi. Jadi, keseluruhan code tersebut adalah untuk mengelola nilai yang hilang pada kolom 'area' dan 'floor' dalam DataFrame df.**

    - Mengatasi Outlier: Gunakan metode IQR untuk mengidentifikasi dan menangani outlier pada harga rumah.

        ![Gambar Atasi Outlier](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/04_Code-mengatasi-outlier.png?raw=true)

        **Keseluruhan code tersebut bertujuan untuk membersihkan, mengonversi, dan mengatasi outlier pada kolom 'price' dalam DataFrame df.**

    - Menjaga Integritas Data: Verifikasi dan validasi keakuratan data pada kolom 'address' dan 'url'.

        ![Gambar Integritas data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/05_Code-integritas-data.png?raw=true)

        **Keseluruhan code tersebut bertujuan untuk memeriksa keberadaan nilai yang hilang dalam kolom 'address' dan 'url', serta melakukan validasi terhadap format URL.**
    
    - Simpan hasil proses ke .csv

        ![Gambar Simpan hasil proses](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/06_Simpan-df-ke-csv.png?raw=true)
    
    - Output hasil dari proses dalam bentuk .csv

        ![Gambar Output](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/15_Data-Transformation/screenshots/Prioritas-2/07_Output-csv-setelah-proses.png?raw=true)

