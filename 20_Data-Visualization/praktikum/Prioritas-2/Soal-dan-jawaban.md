## Soal dan Jawaban Prioritas 2 - Data Visualization

1. Sebuah platform e-commerce telah merekap data transaksi. Platform tersebut ingin mendapatkan informasi berikut:
    - Jumlah nilai transaksi per hari.
    - Kategori barang yang paling banyak dibeli.
    - Jumlah nilai transaksi dengan metode pembayaran e-wallet.
    - Nilai maksimal, nilai minimal dan nilai tengah dari jumlah nilai transaksi yang dilakukan.
    Berdasarkan poin-poin tersebut, buatlah data visualization untuk memperoleh informasi tersebut.

2. Sebuah survei mengenai pengembangan software telah dilakukan dan didapatkan data sebagai berikut. Buatlah data visualization untuk memperoleh berbagai informasi berikut:
    - Persentase responden berdasarkan umur.
    - Bahasa pemrograman / framework yang paling banyak digunakan dalam pengembangan front end.
    - Bahasa pemrograman / framework yang paling banyak digunakan dalam pengembangan back end.
    - Persentase bahasa pemrograman / framework yang dipilih dalam pengembangan front end.
    - Rentangan gaji per tahun yang paling banyak berdasarkan hasil survei.
    
    Catatan tambahan:
    Pastikan data survei sudah diproses untuk menghindari data duplikat dan data dengan atribut yang tidak lengkap.

**Jawaban :**

**Jawaban No.1 :**

- **Import Library yang dibutuhkan:**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/01_Import-library.png?raw=true)

- **Read dataset file JSON:**

    ![Read Dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/02_Read-dataset-json.png?raw=true)

- **Konversi data menjadi dataframe:**

    ![Konversi data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/03_Konversi-data-menjadi-dataframe.png?raw=true)

- **Code jumlah nilai transaksi per hari:**

    ![Code jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/04_Code-jumlah-nilai-transaksi.png?raw=true)

    **Code tersebut merupakan pengelompokan data berdasarkan tanggal transaksi pada suatu DataFrame (df). Sehingga, hasil dari code tersebut adalah sebuah Series yang berisi jumlah total transaksi untuk setiap tanggal yang unik dalam DataFrame df.**

- **Code kategori barang paling banyak dibeli:**

    ![Code kategori barang paling banyak dibeli](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/05_Code-kategori-barang-paling-banyak-dibeli.png?raw=true)

    **Sehingga, most_purchased_category akan berisi lima kategori barang yang paling sering dibeli, beserta jumlah kemunculannya dalam DataFrame df.**

- **Code jumlah nilai transaksi dengan payment method = e wallet:**

    ![Code jumlah nilai transaksi dengan payment method = e wallet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/06_Code-jumlah-nilai-transaksi-payment-ewallet.png?raw=true)

    **Sehingga, ewallet_transaction akan berisi total jumlah transaksi yang dilakukan dengan metode pembayaran menggunakan e-wallet dalam DataFrame df.**

- **Code nilai minimal, maksimal, tengah dari nilai jumlah transaksi:**

    ![Code nilai minimal, maksimal, tengah](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/07_Code-nilai-minimal-maksimal-tengah.png?raw=true)

    **Sehingga, max_transaction akan berisi nilai maksimum dari kolom 'transaction_amount', min_transaction akan berisi nilai minimum, dan median_transaction akan berisi nilai median dari DataFrame df pada kolom 'transaction_amount'.**

- **Code visualisasi jumlah nilai transaksi per hari:**

    ![Code visualisasi jumlah nilai transaksi per hari](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/08_Visualisasi-jumlah-nilai-transaksi.png?raw=true)

    **Ini adalah code untuk membuat plot yang menampilkan jumlah nilai transaksi harian dalam bentuk diagram batang dengan label yang sesuai dan judul yang relevan.**

- **Output visualisasi jumlah nilai transaksi per hari:**

    ![Output visualisasi jumlah nilai transaksi per hari](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/09_Ouput-visualisasi-jumlah-nilai-transaksi.png?raw=true)

- **Code visualisasi kategori barang paling banyak dibeli:**

    ![Code visualisasi kategori barang paling banyak dibeli](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/10_Visualisasi-kategori-barang-paling-banyak-dibeli.png?raw=true)

    **Ini adalah code untuk membuat plot yang menampilkan kategori barang yang paling banyak dibeli dalam bentuk diagram batang dengan label yang sesuai dan judul yang relevan.**

- **Output visualisasi kategori barang paling banyak dibeli:**

    ![Output visualisasi kategori barang paling banyak dibeli](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/11_Output_visualisasi-kategori-barang-paling-banyak-dibeli.png?raw=true)

- **Code visualisasi jumlah nilai transaksi payment e wallet:**

    ![Code visualisasi jumlah nilai transaksi payment e wallet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/12_Visualisasi-jumlah-nilai-transaksi-payment-ewallet.png?raw=true)

    **Ini adalah code untuk membuat plot yang menampilkan total nilai transaksi dengan menggunakan metode pembayaran e-wallet dan metode pembayaran lainnya dalam bentuk diagram batang dengan label yang sesuai dan judul yang relevan.**

- **Output visualisasi jumlah nilai transaksi payment e wallet:**

    ![Output visualisasi jumlah nilai transaksi payment e wallet](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/13_Output-visualisasi-jumlah-nilai-transaksi-payment-ewallet.png?raw=true)

- **Code visualisasi nilai minimal, maximal, dan tengah dari nilai jumlah transaksi:**

    ![Code visualisasi nilai minimal, maximal, dan tengah](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/14_Visualisasi-nilai-minimal-maksimal-tengah.png?raw=true)

    **Ini adalah code untuk membuat plot yang menampilkan distribusi nilai transaksi dalam bentuk diagram kotak (boxplot) dengan titik data untuk nilai maksimum, minimum, dan median, beserta label dan judul yang sesuai.**

- **Output visualisasi nilai minimal, maximal, dan tengah dari nilai jumlah transaksi:**

    ![Output visualisasi nilai minimal, maximal, dan tengah](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-1/15_Output-visualisasi-nilai-minimal-maksimal-tengah.png?raw=true)

**Jawaban No.2 :**

- **Import Library yang dibutuhkan:**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/01_Import-library.png?raw=true)

- **Read dataset CSV nya:**

    ![Read dataset CSV](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/02_Read-dataset-csv.png?raw=true)

- **Code hapus data duplikat dan atribut tidak lengkap:**

    ![Code hapus data duplikat dan atribut tidak lengkap](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/03_Code-hapus-data-duplikat-dan-atribut-tidak-lengkap.png?raw=true)

    **Code tersebut menggunakan metode dropna() dan drop_duplicates() untuk membersihkan DataFrame df dari nilai-nilai yang kosong (NaN) dan duplikat, secara berturut-turut.**

- **Code hapus baris yang memiliki "-" di kolomnya:**

    ![Code hapus baris yang memiliki "-" di kolomnya](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/04_Hapus-baris-yang-memiliki-'-'-pada-colomnya.png?raw=true)

    **Code tersebut menghilangkan baris-baris di DataFrame df di mana nilai kolom 'favorite_front_end' atau 'age' adalah '-'. Kemudian, kedua DataFrame yang baru dibuat digunakan untuk mengganti DataFrame df, sehingga DataFrame df akan berisi hanya baris-baris di mana kolom 'favorite_front_end' dan 'age' memiliki nilai yang valid, yaitu tidak sama dengan '-'.**

- **Code agregasi data:**

    ![Code agregasi data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/05_Code-agregasi-data.png?raw=true)

    **Pertama, code tersebut melakukan pengelompokkan DataFrame df berdasarkan dua kolom, yaitu 'name' dan 'age', dan menghitung jumlah baris dalam setiap kelompok. Hasilnya disimpan dalam DataFrame baru yang disebut aggregated_df. Selanjutnya, dilakukan pengelompokkan lagi berdasarkan dua kolom lain, yaitu 'name' dan 'salary_per_year_in_USD', dan menghitung jumlah baris dalam setiap kelompok. Hasilnya disimpan dalam DataFrame baru yang disebut aggregated_salary_df.**

- **Visualisasi persentase responden berdasarkan umur:**

    ![Visualisasi persentase responden berdasarkan umur](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/06_Visualisasi-persentase-responden-berdasarkan-umur.png?raw=true)

    **Code ini membuat histogram untuk menampilkan distribusi umur responden berdasarkan data yang telah diagregasi dalam DataFrame aggregated_df.**

- **Output Visualisasi persentase responden berdasarkan umur:**

    ![Output persentase responden berdasarkan umur](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/07_Output-Visualisasi-persentase-responden-berdasarkan-umur.png?raw=true)

- **Visualisasi Bahasa pemrograman/framework yang paling banyak digunakan dalam pengembangan front end:**

    ![Visualisasi pengembangan front end](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/08_Visualisasi-framework-pengembangan-front-end.png?raw=true)

    **Ini adalah code untuk membuat countplot yang menampilkan penggunaan front end framework atau bahasa pemrograman yang menjadi favorit responden, dengan label dan judul yang sesuai.**

- **Output Visualisasi Bahasa pemrograman/framework yang paling banyak digunakan dalam pengembangan front end:**

    ![Output Visualisasi pengembangan front end](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/09_Output-Visualisasi-framework-pengembangan-front-end.png?raw=true)

- **Visualisasi Bahasa pemrograman/framework yang paling banyak digunakan dalam pengembangan back end:**

    ![Visualisasi pengembangan back end](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/10_Visualisasi-framework-pengembangan-back-end.png?raw=true)

    **Ini adalah code untuk membuat countplot yang menampilkan penggunaan back end framework atau bahasa pemrograman yang menjadi favorit responden, dengan label dan judul yang sesuai.**

- **Output Visualisasi Bahasa pemrograman/framework yang paling banyak digunakan dalam pengembangan back end:**

    ![Output Visualisasi pengembangan back end](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/11_Output-Visualisasi-framework-pengembangan-back-end.png?raw=true)

- **Visualisasi Persentase bahasa pemrograman/framework yang dipilih dalam pengembangan front end:**

    ![Visualisasi persentase pengembangan front end](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/12_Visualisasi-persentase-framework-pengembangan-front-end.png?raw=true)

    **Ini adalah code untuk membuat diagram batang yang menampilkan persentase penggunaan setiap front end framework atau bahasa pemrograman favorit oleh responden.**

- **Output Visualisasi Persentase bahasa pemrograman/framework yang dipilih dalam pengembangan front end:**

    ![Output Visualisasi persentase pengembangan front end](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/13_Output-Visualisasi-persentase-framework-pengembangan-front-end.png?raw=true)

- **Visualisasi Rentangan gaji per tahun yang paling banyak berdasarkan hasil survei:**

    ![Visualisasi Rentangan gaji per tahun yang paling banyak berdasarkan hasil survei](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/14_Visualisasi-rentangan-gaji.png?raw=true)

    **Ini adalah code untuk membuat histogram yang menampilkan distribusi gaji per tahun responden berdasarkan data yang telah diagregasi, dengan label dan judul yang sesuai.**

- **Output Visualisasi Rentangan gaji per tahun yang paling banyak berdasarkan hasil survei:**

    ![Output Visualisasi Rentangan gaji per tahun yang paling banyak berdasarkan hasil survei](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-2/Soal-No-2/15_Output-Visualisasi-rentangan-gaji.png?raw=true)