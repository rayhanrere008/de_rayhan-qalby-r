## Soal dan Jawaban Prioritas 2 - Implementation AI on Data Engineer

Sebuah perusahaan retail ingin mengoptimalkan proses analisis data penjualan mereka. Mereka memiliki dataset penjualan yang mencakup informasi seperti tanggal transaksi, jumlah penjualan, harga, kategori produk, dan lainnya. Tujuan utama adalah untuk menghasilkan SQL queries yang dapat membantu dalam analisis data yang lebih efisien dan efektif.

1. Membuat Database
    - Buatkan tabel dengan atribut kurang lebih memiliki tanggal transaksi, jumlah penjualan, harga, kategori produk, dan lainnya

        ![Buatkan tabel](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/01_Buat-database-dan-tabel.png?raw=true)

        ![Code Buat tabel](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/02_Code-buat-database-dan-tabel.png?raw=true)

2. Generate SQL dengan OpenAI API:

    ![Code Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/03_Import-library-yang-diperlukan.png?raw=true)

    **Import library yang dibutuhkan seperti os, load_dotenv, OpenAI**

    ![Persiapkan file env](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/04_Persiapkan-file-.env.png?raw=true)

    **Buat key api pada NAGA AI, lalu masukkan ke env.**

    ![Integrasikan ke OpenAI](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/05_Integrasikan-ke-OpenAI.png?raw=true)

    **Setelah mendapatkan key API nya integrasikan dengan OpenAI**

    - Gunakan OpenAI API untuk menghasilkan SQL queries. Misalnya, berikan prompt seperti "Buatkan SQL query untuk menghitung total penjualan per kategori produk setiap bulan."

        ![Code function prompt](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/06_Code-function-prompt.png?raw=true)

        **Fungsi generate(prompt, model="gpt-3.5-turbo") di atas adalah fungsi yang menggunakan objek client (yang diasumsikan sebagai objek yang sudah diinisialisasi sebelumnya untuk berinteraksi dengan API NAGA AI) untuk menghasilkan teks berdasarkan prompt yang diberikan.**

        ![Prompting](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/07_Prompting-dan-hasil-responses.png?raw=true)

        **Code tersebut adalah contoh penggunaan OpenAI API untuk menghasilkan respons dari Chat GPT berdasarkan daftar prompt yang diberikan. Di sini, kita memiliki sebuah daftar prompt yang berisi perintah SQL yang berbeda untuk diberikan sebagai input kepada Chat GPT. Kemudian, kode tersebut menggunakan loop untuk mengirim setiap prompt kepada OpenAI API untuk mendapatkan respons dari model Chat GPT. Setiap respons kemudian dicetak ke layar.**

    - Catat respons AI dan analisis keakuratan serta relevansi query yang dihasilkan.

        ![Output Prompting](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/08_Output-prompting.png?raw=true)

        **Menghasilkan output dengan perintah SQL yang sesuai dengan kebutuhan. Sejuah  ini hasil yang didapatkan akurat dengan relevansi query sebagaimana biasanya.**

3. Validasi Query SQL
    - Validasi SQL queries yang dihasilkan menggunakan sistem manajemen database yang ada. Pastikan query berjalan dengan benar dan menghasilkan output yang diharapkan.

        ![Validasi Query SQL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/09_Validasi-query-di-DBMS-MySQL.png?raw=true)

        **Setelah mendapatkan output dari respon promptingnya, hasilnya saya validasi ke DBMS Dbeaver untuk pengecekan apakah query query tersebut benar ataukah salah.**

4. Implementasi dan Analisis Hasil:
    - Terapkan SQL queries yang telah divalidasi dan dioptimalkan dalam sistem database perusahaan.

        ![Terapkan Query SQL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/10_Terapkan-query-menghitung-total-penjualan-per-kategori-produk-setiap-bulan.png?raw=true)

        **Setelah diterapkan query SQL tersebut menghasilkan output yang sesuai yang menampilkan data total penjualan per kategori produk setiap bulan.**

        ![Terapkan Query SQL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/11_Terapkan-query-menampilkan-tanggal-transaksi-dengan-jumlah-penjualan-tertinggi.png?raw=true)

        **Setelah diterapkan query SQL tersebut menghasilkan output yang sesuai yaitu Menampilkan tanggal transaksi dengan jumlah penjualan tertinggi.**

        ![Terapkan Query SQL](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-2/12_Terapkan-query-menghitung-total-pendapatan-per-bulan.png?raw=true)

        **Setelah diterapkan query SQL tersebut menghasilkan output yang sesuai yaitu Menampilkan total pendapatan per bulan.**