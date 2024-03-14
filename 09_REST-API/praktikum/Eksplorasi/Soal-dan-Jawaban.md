## Soal Eksplorasi - REST API

1. Eksplorasi API RentABook:
    - Pelajari dokumentasi API dari RentABook: https://app.swaggerhub.com/apis-docs/sepulsa/RentABook-API/1.0.0.

        ![Gambar Dokumentasi RentABook API](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/09_REST-API/screenshots/Eksplorasi/1_Tampilan-dokumentasi-RentABook-API.png?raw=true)

    - Identifikasi endpoint yang tersedia dan fungsinya.

        **Authentication :**
        - /token : Request **GET** untuk mendapatkan akses token

        **Client Resource :**
        - /client/{id} : Request **GET** untuk mendapatkan detail client berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/client/{id}
        - /client/{id} : Request **PUT** untuk melakukan update client berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/client/{id}
        - /client/{id} : Request **DELETE** untuk menghapus client berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/client/{id}
        - /client : Request **GET** untuk mendapatkan daftar semua client
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/client
        - /client : Request **POST** untuk menambahkan client baru
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/client
        
        **User Resource :**
        - /user/{id} : Request **GET** untuk mendapatkan detail user berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/user/{id}
        - /user/{id} : Request **PUT** untuk melakukan update detail user berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/user/{id}
        - /user/{id} : Request **DELETE** untuk menghapus user berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/user/{id}
        - /user : Request **GET** untuk mendapatkan daftar semua user
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/user
        - /user : Request **POST** untuk menambahkan user baru
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/user
        
        **Book Resource :**
        - /book/{id} : Request **GET** untuk mendapatkan detail book berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/book/{id}
        - /book/{id} : Request **PUT** untuk melakukan update detail book berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/book/{id}
        - /book/{id} : Request **DELETE** untuk menghapus book berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/book/{id}
        - /book : Request **GET** untuk mendapatkan daftar semua book
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/book
        - /book : Request **POST** untuk menambahkan book baru
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/book
        
        **Rent Transaction**
        - /rent/{id} : Request **GET** untuk mendapatkan detail Rent transaction (transaksi penyewaan) berdasarkan ID
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/rent/{id}
        - /rent : Request **GET** untuk mendapatkan daftar semua Rent transaction
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/rent
        - /rent : Request **POST** untuk menambahkan Rent transaction baru 
            URL : https://virtserver.swaggerhub.com/sepulsa/RentABook-API/1.0.0/rent

2. Implementasi 4 Method pada RentABook API:
    - Lakukan request dengan method GET, POST, PUT, dan DELETE pada endpoint yang tersedia di RentABook API.
        Contoh: Lakukan operasi CRUD pada resource client.

        - Request GET (client/id) Menampilkan daftar client berdasarkan ID :

            ![Gambar GET daftar client by ID](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/09_REST-API/screenshots/Eksplorasi/2_Get-client-by-id.png?raw=true)

        - Request POST (client) Menambahkan client baru : 

            ![Gambar POST New Client](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/09_REST-API/screenshots/Eksplorasi/2_Post-new-data-client.png?raw=true)

        - Request PUT (client/id) Mengupdate daftar client berdasarkan ID :

            ![Gambar PUT daftar Client by ID ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/09_REST-API/screenshots/Eksplorasi/2_Put-data-client-by-id-update.png?raw=true)

        - Request DELETE (client/id) Menghapus client berdasarkan ID :

            ![Gambar DELETE Client by ID ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/09_REST-API/screenshots/Eksplorasi/2_Delete-data-client-by-id.png?raw=true)

3. Dokumentasi Eksplorasi:
    - Simpan semua request dan response yang berkaitan dengan RentABook API dalam Postman Collection baru.

        ![Gambar RentABook API Simpan ke Collection ](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/09_REST-API/screenshots/Eksplorasi/3_Simpan-ke-New-Collection.png?raw=true)