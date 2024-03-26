## Soal Prioritas 1 - Data Warehouse and Data Lake

1. Sebutkan dan jelaskan tantangan yang perlu dihadapi dalam penggunaan Data Warehouse!
2. Perhatikan diagram ERD berikut.

    ![Gambar Soal ERD](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/Gambar_Soal-ERD.png?raw=true)

    Berdasarkan diagram ERD tersebut buatlah berbagai tabel dengan menggunakan Citus.

**Jawaban :**

1. Dalam penggunaan data warehouse terdapat tantangan yang perlu dihadapi
    - **Keamanan Data**:
        - Data warehouse yang mengintegrasikan data dari berbagai sumber juga meningkatkan risiko keamanan.
        - Perlindungan data dan kepatuhan peraturan sangat penting.
    - **Manajemen Data yang Rumit**:
        - Semakin banyak data yang dikumpulkan, semakin rumit pula manajemen data.
        - Mengelola data dengan efisien dan memastikan konsistensi adalah tantangan utama.
    - **Integrasi Data yang Rumit**:
        - Integrasi data dari berbagai sumber bisa menjadi rumit dan memakan waktu.
        - Memastikan data terintegrasi dengan baik dan sesuai dengan kebutuhan analitika bisnis adalah tantangan yang perlu dihadapi.

    - **Referensi** :
        - https://www.kompasiana.com/naila981/654a53fb110fce4d104d1de2/data-warehouse-di-era-digital-inovasi-dan-tantangan

2. Pembuatan berbagai tabel di Citus
    - **Table users** :

        ![Gambar Create Table Users](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/01_Create-table-users-in-Citus.png?raw=true)

        ![Gambar Table Users Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/01_Table-users-created.png?raw=true)

        Diatas merupakan bentuk kueri untuk membuat table di Citus, tabel yang dibuat adalah **users** dengan beberapa atribut yaitu id (primary key), username, password, created_at, updated_at.

        **Insert Data to table**

        ![Gambar Insert Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/05_Insert-data-to-tabel-users.png?raw=true)
    
    - **Table categories** :

        ![Gambar Create Table Categories](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/02_Create-table-categories-in-Citus.png?raw=true)

        ![Gambar Table Categories Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/02_Table-categories-created.png?raw=true)

        Diatas merupakan bentuk kueri untuk membuat table di Citus, tabel yang dibuat adalah **categories** dengan beberapa atribut yaitu id (primary key), name, created_at, updated_at.
    
       **Insert Data to table**
       
       ![Gambar Insert Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/06_Insert-data-to-tabel-categories.png?raw=true)
    
    - **Table posts** :

        ![Gambar Create Table Posts](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/03_Create-table-posts-in-Citus.png?raw=true)

        ![Gambar Table Posts Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/03_Table-posts-created.png?raw=true)

        Diatas merupakan bentuk kueri untuk membuat table di Citus, tabel yang dibuat adalah **posts** dengan beberapa atribut yaitu id (primary key), user_id (fk dari tabel users), category_id (fk dari tabel categories), title, content, created_at, updated_at.

        **Insert Data to Table**

        ![Gambar Insert Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/07_Insert-data-to-tabel-posts.png?raw=true)
    
    - **Table comments** :

        ![Gambar Create Table Comments](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/04_Create-table-comments-in-Citus.png?raw=true)

        ![Gambar Table Comments Created](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/04_Table-comments-created.png?raw=true)

        Diatas merupakan bentuk kueri untuk membuat table di Citus, tabel yang dibuat adalah **comments** dengan beberapa atribut yaitu id (primary key), post_id (fk dari tabel posts), user_id (fk dari tabel users), content, created_at, updated_at.

        **Insert Data to Table**

        ![Gambar Insert Data](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/12_Data-Warehouse-and-Data-Lake/screenshots/Prioritas-1/08_Insert-data-to-tabel-comments.png?raw=true)
