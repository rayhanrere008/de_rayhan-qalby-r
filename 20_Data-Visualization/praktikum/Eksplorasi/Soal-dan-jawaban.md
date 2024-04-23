## Soal dan Jawaban Eksplorasi - Data Visualization

1. Sebuah data transaksi saham telah dikumpulkan dan disimpan pada file berikut. Buatlah data visualization untuk mendapatkan informasi berikut:
    - Harga beli saham yang tertinggi dalam rupiah (IDR). Pastikan semua nilai transaksi sudah dikonversi dalam satuan rupiah.
    - Perkembangan transaksi pembelian saham TSLA.
    - Persentase jenis saham yang dilakukan proses jual-beli. Jenis saham dapat dilihat pada bagian stock_symbol.
    - Jenis transaksi yang banyak dilakukan (buy / sell).
    - Persentase jenis transaksi yang dilakukan.
    - Rata-rata nilai transaksi jual pada setiap tahun untuk semua jenis saham.

**Jawaban :**

- **Import Library yang dibutuhkan:**

    ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/01_Import-library.png?raw=true)

- **Muat dataset form json:**

    ![Muat dataset form json](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/02_Muat-dataset-from-json.png?raw=true)

- **Create dataframe from data JSON:**

    ![Create dataframe](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/03_Create-dataframe-from-json.png?raw=true)

- **Konversi harga transaksi ke rupiah:**

    ![Konversi harga transaksi](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/04_Konversi-harga-transaksi-ke-rupiah.png?raw=true)

    **Code tersebut melakukan pengalihan nilai dari kolom 'trade_price' dalam dataframe df ke mata uang Rupiah (IDR) dengan mengalikannya dengan kurs konversi 1 USD = 17,000 IDR. Hasil konversi kemudian disimpan dalam kolom baru dengan nama 'trade_price_idr' di dalam dataframe df.**

- **Code Harga beli saham tertinggi dalam rupiah (IDR) dan Visualisasi:**

    ![Harga beli saham tertinggi dalam rupiah](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/05_Code-dan-visualisasi-harga-beli-saham-tertinggi-dalam-rupiah.png?raw=true)

    **Dengan demikian, hasil dari code ini adalah mencetak harga beli saham tertinggi dalam IDR dan menampilkan visualisasi dalam bentuk diagram batang.**

- **Output Visualisasi Harga beli saham tertinggi dalam rupiah (IDR):**

    ![Output Visualisasi Harga beli saham tertinggi dalam rupiah](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/06_Output-visualisasi-harga-beli-saham-tertinggi-dalam-rupiah.png?raw=true)

- **Code Perkembangan transaksi pembelian saham TSLA dan Visualisasi:**

    ![Perkembangan transaksi pembelian saham TSLA](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/07_Code-dan-visualisasi-perkembangan-transaksi-beli-saham-TSLA.png?raw=true)

    **Hasilnya adalah visualisasi perkembangan transaksi pembelian saham TSLA dalam bentuk scatter plot dengan tanggal transaksi pada sumbu x dan harga saham dalam IDR pada sumbu y.**

- **Output Visualisasi Perkembangan transaksi pembelian saham TSLA:**

    ![Output Visualisasi Perkembangan transaksi pembelian saham TSLA](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/08_Output-visualisasi-perkembangan-transaksi-beli-saham-TSLA.png?raw=true)

- **Code Persentase jenis saham yang dilakukan proses jual-beli dan Visualisasi:**

    ![Persentase jenis saham yang dilakukan proses jual-beli](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/09_Code-dan-visualisasi-persentase-saham-proses-jual-beli.png?raw=true)

    **Code ini bertujuan untuk menghitung persentase masing-masing jenis saham yang mengalami proses jual-beli dari dataframe df dan kemudian memvisualisasikannya dalam bentuk strip plot. Hasilnya adalah visualisasi persentase jenis saham yang mengalami proses jual-beli dalam bentuk strip plot dengan jenis saham pada sumbu x dan persentase pada sumbu y.**

- **Output Visualisasi Persentase jenis saham yang dilakukan proses jual-beli:**

    ![Output Visualisasi Persentase jenis saham yang dilakukan proses jual-beli](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/10_Output-visualisasi-persentase-saham-proses-jual-beli.png?raw=true)

- **Code Jenis transaksi yang banyak dilakukan (buy / sell):**

    ![Jenis transaksi yang banyak dilakukan (buy / sell)](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/11_Code-dan-visualisasi-jenis-transaksi-yang-banyak-dilakukan-buy-atau-sell.png?raw=true)

    **Code ini bertujuan untuk menghitung jumlah transaksi yang dilakukan untuk setiap jenis transaksi dari dataframe df dan kemudian memvisualisasikannya dalam bentuk plot garis. Hasilnya adalah visualisasi jumlah transaksi yang dilakukan untuk setiap jenis transaksi dalam bentuk plot garis dengan jenis transaksi pada sumbu x dan jumlah transaksi pada sumbu y.**

- **Output Visualisasi Jenis transaksi yang banyak dilakukan (buy / sell):**

    ![Output Visualisasi Jenis transaksi yang banyak dilakukan (buy / sell)](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/12_Output-visualisasi-jenis-transaksi-yang-banyak-dilakukan-buy-atau-sell.png?raw=true)

- **Code Persentase jenis transaksi yang dilakukan:**

    ![Persentase jenis transaksi yang dilakukan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/13_Code-dan-visualisasi-persentase-jenis-transaksi-yang-dilakukan.png?raw=true)

    **Code tersebut bertujuan untuk menghitung persentase dari setiap jenis transaksi yang dilakukan dalam dataframe df dan kemudian memvisualisasikannya dalam bentuk pie plot. Hasilnya adalah visualisasi persentase dari setiap jenis transaksi yang dilakukan dalam bentuk pie plot, di mana setiap bagian pie mewakili persentase dari jenis transaksi yang berbeda.**

- **Output Visualisasi Persentase jenis transaksi yang dilakukan:**

    ![Output Visualisasi Persentase jenis transaksi yang dilakukan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/14_Output-visualisasi-persentase-jenis-transaksi-yang-dilakukan.png?raw=true)

- **Code Rata-rata nilai transaksi jual pada setiap tahun untuk semua jenis saham:**

    ![Rata-rata nilai transaksi jual pada setiap tahun](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/15_Code-dan-visualisasi-rata-rata-nilai-transaksi-jual-setiap-tahun.png?raw=true)

    **Hasilnya adalah visualisasi rata-rata nilai transaksi jual per tahun untuk semua jenis saham dalam bentuk bar plot, di mana sumbu x adalah tahun dan sumbu y adalah rata-rata nilai transaksi jual dalam IDR.**

- **Output Visualisasi Rata-rata nilai transaksi jual pada setiap tahun untuk semua jenis saham:**

    ![Output Visualisasi Rata-rata nilai transaksi jual pada setiap tahun](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/20_Data-Visualization/screenshots/Eksplorasi/16_Output-visualisasi-rata-rata-nilai-transaksi-jual-setiap-tahun.png?raw=true)