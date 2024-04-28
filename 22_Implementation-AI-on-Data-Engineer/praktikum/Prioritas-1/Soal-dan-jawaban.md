## Soal dan Jawaban Prioritas 1 - Implementation AI on Data Engineer

1. Set Environment dan Dataset:
    - Siapkan dataset penjualan dalam format CSV atau Excel.

        ![Siapkan dataset](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/01_Menyiapkan-dataset-penjualan.png?raw=true)

    - Dataset harus mencakup informasi penting seperti tanggal, jumlah penjualan, harga, kategori produk, dan lainnya.

        **Dataset penjualan saya sudah mencakup tanggal, jumlah penjualan, harga, dan kategori produk.**

    - Buat file .env untuk menyimpan kredensial API OpenAI (misalnya, OPENAI_API_KEY).

        ![Buat file .env](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/02_Persiapkan-file-.env.png?raw=true)

        **Disini saya menggunakan API Key dari NAGA AI untuk melakukan prompting.**

2. Integrasi OpenAI API
    - Gunakan Python untuk membaca kredensial dari file .env.

        ![Install Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/03_Install-library-yang-diperlukan.png?raw=true)

        ![Import Library](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/04_Import-library.png?raw=true)

        **Install dan import library yang diperlukan seperti pandas, matplotlib, openai, python-dotenv, os.**

    - Integrasikan OpenAI API dengan skrip Python Anda untuk menganalisis dataset penjualan.

        ![Integrasikan OpenAI API](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/05_integrasikan-dengan-openAI.png?raw=true)

        **Kode di atas adalah contoh penggunaan modul atau library tertentu untuk mengelola environment variables dan inisialisasi koneksi ke API NAGA AI. Dengan menggabungkan langkah-langkah ini, maka dapat memuat kunci API dari file .env, mengaksesnya dalam kode, dan menggunakan kunci tersebut untuk mengautentikasi permintaan API ke NAGA AI.**

        ![Load dataset csv](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/06_load-dataset-csv.png?raw=true)

        **Code tersebut digunakan untuk memuat data dari dataset penjualan yang telah dibuat.**

3. Optimasi Prompt Engineering:
    - Kembangkan berbagai prompt yang dirancang untuk mendapatkan insight dari dataset penjualan menggunakan OpenAI API.

        ![Function prompting](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/07_function-prompting.png?raw=true)

        **Fungsi generate(prompt, model="gpt-3.5-turbo") di atas adalah fungsi yang menggunakan objek client (yang diasumsikan sebagai objek yang sudah diinisialisasi sebelumnya untuk berinteraksi dengan API NAGA AI) untuk menghasilkan teks berdasarkan prompt yang diberikan.**

    - Fokuskan pada analisis tren penjualan, segmentasi pelanggan, dan prediksi penjualan.

        ![Prompt 1 analisis tren penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/08_Code-prompt1-analisis-tren-penjualan.png?raw=true)

        **Kode di atas menggunakan fungsi generate yang telah didefinisikan sebelumnya untuk menghasilkan teks berdasarkan prompt yang diberikan. Hasil ini adalah teks yang dihasilkan oleh model AI berdasarkan prompt yang diberikan, termasuk informasi tentang tren penjualan dan kesimpulan yang mungkin ditarik dari pola penjualan harian.**

        ![Output Prompt 1 analisis tren penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/09_Output-prompt1-analisis-tren-penjualan.png?raw=true)

        ![Prompt 2 segmentasi pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/10_Code-prompt2-segmentasi-pelanggan.png?raw=true)

        **Kode di atas hampir identik dengan yang sebelumnya, hanya berbeda pada prompt yang diberikan dan judul yang dicetak. Hasil ini adalah teks yang dihasilkan oleh model AI berdasarkan prompt yang diberikan, termasuk informasi tentang segmentasi pelanggan dan pola pembelian yang konsisten dari kelompok pelanggan tertentu.**

        ![Output Prompt 2 segmentasi pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/11_Output-prompt2-segmentasi-pelanggan.png?raw=true)

        ![Prompt 3 prediksi penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/12_Code-prompt3-prediksi-penjualan.png?raw=true)

        **Kode ini juga mirip dengan yang sebelumnya, dengan perbedaan pada prompt yang diberikan.  Hasil ini adalah teks yang dihasilkan oleh model AI berdasarkan prompt yang diberikan, termasuk informasi tentang performa prediksi penjualan dan perbandingannya dengan realitas.**

        ![Output Prompt 3 prediksi penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/13_Output-prompt3-prediksi-penjualan.png?raw=true)

4. Analisis dan Visualisasi Data:
    - Gunakan Pandas untuk analisis data awal dan visualisasi menggunakan Matplotlib atau Seaborn.

        ![Code visualisasi data tren penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/14_Code-visualisasi-data-tren-penjualan.png?raw=true)

        **Ini adalah kode untuk membuat plot garis yang menunjukkan tren penjualan selama bulan April 2024 berdasarkan data yang dimiliki.**

        ![Output visualisasi data tren penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/15_hasil-visualisasi-data-tren-penjualan.png?raw=true)

        ![Code visualisasi data segmentasi pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/16_Code-visualisasi-data-segmentasi-pelanggan.png?raw=true)

        **Kode ini membuat plot batang yang menunjukkan total jumlah pembelian untuk setiap kategori produk, yang membantu dalam segmentasi pelanggan berdasarkan kategori produk.**

        ![Output visualisasi data segmentasi pelanggan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/17_Output-visualisasi-data-segmentasi-pelanggan.png?raw=true)

        ![Code visualisasi data prediksi penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/18_Code-visualisasi-data-prediksi-penjualan.png?raw=true)

        **Kode ini menciptakan visualisasi tren penjualan historis bersama dengan proyeksi sederhana dalam bentuk rata-rata penjualan.**

        ![Output visualisasi data prediksi penjualan](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/22_Implementation-AI-on-Data-Engineer/screenshots/Prioritas-1/19_Output-visualisasi-data-prediksi-penjualan.png?raw=true)

    - Bandingkan hasil analisis tradisional dengan insight yang diperoleh dari OpenAI API.

        - **Tren Penjualan** : Dengan demikian, meskipun visualisasi data memberikan pemahaman yang baik tentang tren penjualan, insight dari OpenAI API memberikan tambahan informasi yang lebih rinci dan mendalam tentang pola penjualan harian serta faktor-faktor yang mempengaruhi permintaan konsumen. Hal ini dapat membantu pengambilan keputusan yang lebih tepat dalam pengembangan strategi penjualan dan manajemen persediaan produk. 

        - **Segmentasi pelangan** : Dari hasil analisis tradisional, mungkin sulit untuk langsung mengidentifikasi pola pembelian yang konsisten dari kelompok pelanggan tertentu. Analisis tradisional biasanya fokus pada visualisasi data dan statistik deskriptif, yang mungkin tidak memberikan informasi yang cukup mendalam tentang perilaku pelanggan.
        
            Namun, insight dari OpenAI API memberikan informasi yang lebih mendalam tentang segmentasi pelanggan berdasarkan jumlah pembelian dan kategori produk yang dibeli. Dari analisis tersebut, ditemukan bahwa ada pola pembelian yang konsisten dari kelompok pelanggan tertentu, misalnya, pelanggan yang cenderung membeli produk elektronik memiliki jumlah pembelian yang relatif tinggi dan konsisten di sekitar 50-60 unit, sementara pelanggan yang cenderung membeli pakaian memiliki jumlah pembelian yang relatif rendah di sekitar 30-40 unit.
        
            Dengan informasi ini, perusahaan dapat mengoptimalkan strategi pemasaran atau penawaran produk untuk masing-masing kelompok pelanggan tersebut. Misalnya, mereka dapat mengembangkan program loyalitas atau promosi khusus untuk pelanggan yang cenderung membeli produk elektronik, atau mereka dapat meningkatkan inventaris produk pakaian untuk menarik lebih banyak pelanggan dalam kategori tersebut.
        
        - **Prediksi penjualan** : Insight dari OpenAI mengenai prediksi penjualan memberikan pemahaman tentang bagaimana kita dapat menggunakan data historis untuk memprediksi penjualan pada tanggal-tanggal tertentu di masa depan. Dengan menggunakan metode analisis data seperti regresi linier atau time series forecasting, kita dapat membuat perkiraan tentang bagaimana penjualan akan berkembang di masa mendatang. Dengan demikian, insight dari OpenAI API memberikan pandangan yang berguna tentang bagaimana kita dapat menggunakan analisis data untuk membuat prediksi penjualan dan mengukur kinerja model prediksi tersebut. Hal ini dapat membantu perusahaan untuk mengambil keputusan yang lebih baik dalam perencanaan dan strategi bisnis mereka.

5. Dokumentasi Proses:
    - Dokumentasikan setiap langkah, mulai dari pengaturan lingkungan, pengolahan data, hingga analisis akhir.

        **Sudah dilakukan dokumentasi setiap langkah seperti diatas.**

    - Catat bagaimana penggunaan file .env dan OpenAI API mempengaruhi proses dan hasil analisis.

        **Penggunaan file .env dan OpenAI API memiliki dampak yang signifikan pada proses dan hasil analisis. Berikut:**

        - **Keamanan Kredensial:** Menggunakan file .env untuk menyimpan kredensial API (seperti kunci API OpenAI) meningkatkan keamanan karena kredensial tidak akan terlihat secara langsung dalam kode sumbernya.
        
        - **Autentikasi API:** Dengan menggunakan kredensial yang disimpan dalam file .env, maka dapat mengautentikasi permintaan API ke OpenAI.
        
        - **Pemrosesan Data:** Penggunaan OpenAI API memungkinkan untuk melakukan analisis teks yang lebih kompleks dan mendapatkan wawasan tambahan dari dataset penjualan Anda.