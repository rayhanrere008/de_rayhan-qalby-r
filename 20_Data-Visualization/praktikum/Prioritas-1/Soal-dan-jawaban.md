## Soal dan Jawaban Prioritas 1 - Data Visualization 

1. Buatlah sebuah data visualization dari dataset berikut dengan kriteria:
    - Membuat sebuah line plot untuk menggambarkan jumlah nilai dari transaksi per hari.
    - Membuat sebuah bar plot untuk menggambarkan jumlah customer per hari.
    - Membuat sebuah scatter plot untuk menggambarkan jumlah nilai dari transaksi per hari.
    - Untuk setiap poin di atas boleh menggunakan library yang berbeda / tidak harus sama.

2. Sebuah toko roti / bakery telah merekap data transaksi. Toko tersebut ingin mendapatkan informasi berikut:
    - Jumlah nilai transaksi per hari.
    - Jenis roti yang paling banyak dipesan.
    - Rata-rata kepuasan pelanggan (customer_rating) per hari.
    - Berdasarkan poin-poin tersebut, buatlah data visualization untuk memperoleh informasi tersebut.

**Jawaban :**

**Jawaban No 1:**

- **Install Library yang dibutuhkan (matplotlib, pandas, seaborn):**

    ![Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/01_Install-Library.png?raw=true)

- **Import Library yang dibutuhkan (matplotlib, pandas, seaborn):**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/02_Import-library.png?raw=true)

- **Read dataset file csv nya:**

    ![Read dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/03_Read-dataset-csvnya.png?raw=true)

- **Code visualisasi jumlah nilai transaksi per hari (menggunakan matplotlib):**

    ![Code visualisasi jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/04_Code-visual-jumlah-nilai-transaksi.png?raw=true)

    **Code tersebut menggambarkan visualisasi jumlah nilai transaksi per hari dari suatu DataFrame (df) yang telah di-grup berdasarkan tanggal transaksi.**

- **Output visualisasi jumlah nilai transaksi per hari (menggunakan matplotlib):**

    ![Output visualisasi jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/05_Output-jumlah-nilai-transaksi-matplotlib.png?raw=true)

- **Code visualisasi jumlah customer per hari (menggunakan pandas):**

    ![Code visualisasi jumlah customer](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/06_Code-jumlah-customer.png?raw=true)

    **Code tersebut menghasilkan visualisasi jumlah pelanggan yang berbeda pada setiap hari berdasarkan DataFrame df yang telah di-grup berdasarkan tanggal transaksi.**

- **Output visualisasi jumlah customer per hari:**

    ![Output visualisasi jumlah customer](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/07_Output-jumlah-customer-pandas.png?raw=true)

- **Code visualisasi jumlah nilai transaksi per hari (menggunakan seaborn):**

    ![Code visualisasi jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/08_Code-visual-jumlah-nilai-transaksi.png?raw=true)

    **Code tersebut menggunakan fungsi sns.scatterplot() dari library Seaborn untuk membuat scatter plot dari data transaksi yang sudah di-grupkan (transaction_date_result). Kemudian, plt.grid(True) digunakan untuk menampilkan grid pada plot.**

- **Output visualisasi jumlah nilai transaksi per hari:**

    ![Output visualisasi jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-1/09_Output-jumlah-nilai-transaksi-seaborn.png?raw=true)

**Jawaban No.2:**

- **Import Library yang dibutuhkan (matplotlib, pandas):**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/01_Import-library.png?raw=true)

- **Read Dataset file csvnya:**

    ![Read Dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/02_Read-dataset.png?raw=true)

- **Code visualisasi jumlah nilai transaksi per hari:**

    ![Code visualisasi jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/03_Code-visual-jumlah-nilai-transaksi.png?raw=true)

    **Code tersebut memvisualisasikan jumlah nilai transaksi per hari dari DataFrame df yang sudah di-grupkan berdasarkan tanggal transaksi. Serta menghasilkan plot yang menunjukkan jumlah nilai transaksi per hari dengan garis merah dan menggunakan grid hanya pada sumbu y.**

- **Output visualisasi jumlah nilai transaksi per hari:**

    ![Output visualisasi jumlah nilai transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/04_Output-jumlah-nilai-transaksi.png?raw=true)

- **Code visualisasi jumlah roti paling banyak dipesan:**

    ![Code visualisasi jumlah roti](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/05_Code-visual-jumlah-roti-paling-banyak-dipesan.png?raw=true)

    **Jadi, code tersebut menemukan dan mencetak jenis roti yang paling banyak dipesan, serta memvisualisasikan jumlah penjualan untuk setiap jenis roti tersebut dalam bentuk diagram batang.**

- **Output visualisasi jumlah roti paling banyak dipesan:**

    ![Output visualisasi jumlah roti](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/06_Output-jumlah-roti-dipesan.png?raw=true)

- **Code visualisasi rata-rata kepuasan pelanggan per hari:**

    ![Code visualisasi rata-rata kepuasan pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/07_Code-visual-rata-rata-kepuasan-pelanggan.png?raw=true)

    **Code tersebut bertujuan untuk memvisualisasikan rata-rata rating kepuasan pelanggan per hari dari DataFrame df yang telah di-grupkan berdasarkan tanggal transaksi. Code tersebut menghasilkan plot yang menunjukkan rata-rata rating kepuasan pelanggan per hari dalam bentuk diagram batang berwarna orange**

- **Output visualisasi rata-rata kepuasan pelanggan per hari:**

    ![Output visualisasi rata-rata kepuasan pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Prioritas-1/Soal-No-2/08_Output-rata-rata-kepuasan-pelanggan.png?raw=true)