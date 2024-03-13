## Soal Data Definition Language - DDL (Relational Database)

1. Create database alta_online_shop.

    ![Gambar Create Database](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/01_Create-database.png?raw=true)

    **Query tersebut akan melakukan perintah pembuatan database, dan melakukan penggunaan database yang telah dibuat, serta menampilkan database yang telah dibuat.**

2. Dari schema Olshop yang telah kamu kerjakan di, Implementasikanlah menjadi table pada MySQL.
    - Create table user.

        ![Gambar Create Table Users](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Users.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table bernama "Users" dengan beberapa column seperti user_id sebagai primary key, name, address, date_of_birth, status_user, gender, created_at, updated_at sesuai dengan tipe data yang diinginkan.**

    - Create table product, product type, operators, product description, payment_method.

        ![Gambar Create Table Products](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Products.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Products" dengan beberapa column product_id sebagai primary_key, product_name, type_id(FK), description_id(FK), operator_id(FK), method_id(FK). Yang Foreign Key (FK) datanya diambil dari tabel yang berbeda.**

        ![Gambar Create Table Product_types](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Product_types.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Products_types" dengan beberapa column type_id sebagai primary_key, type_name sesuai dengan tipe data yang diinginkan.**

        ![Gambar Create Table Operators](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Operators.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Operators" dengan beberapa column operator_id sebagai primary_key, operator_name sesuai dengan tipe data yang diinginkan.**

        ![Gambar Create Table Product_descriptions](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Product_descriptions.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Product_descriptions" dengan beberapa column description_id sebagai primary_key, description sesuai dengan tipe data yang diinginkan.**

        ![Gambar Create Table Payment_methods](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Payment_methods.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Payment_methods" dengan beberapa column method_id sebagai primary_key, method_name sesuai dengan tipe data yang diinginkan.**

    - Create table transaction, transaction detail.

        ![Gambar Create Table Transactions](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Transactions.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Transaction" dengan beberapa column transaction_id sebagai primary_key, user_id(FK) yang diambil dari tabel Users, transaction_date, total_amount, created_at, updated_at sesuai dengan tipe data yang diinginkan.**

        ![Gambar Create Table Transaction_details](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/02_Create-table-Transaction_details.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan table "Transaction_details" dengan beberapa column transaction_detail_id sebagai primary_key, transaction_id(FK) yang diambil dari tabel Transactions, product_id(FK) yang diambil dari tabel Products, quantity, unit_price sesuai dengan tipe data yang diinginkan.**

3. Create tabel kurir dengan field id, name, created_at, updated_at.

    ![Gambar Create Table kurir](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/03_Create-table-kurir.png?raw=true)

    **Query tersebut akan melakukan perintah pembuatan table "kurir" dengan field id, name,created_at, updated_at sesuai dengan tipe data yang diinginkan dan melakukan proses DESCRIBE untuk melihat struktur table tersebut.**

4. Tambahkan ongkos_dasar column di tabel kurir.

    ![Gambar Add Column ongkos_dasar](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/04_Add-column-ongkos_dasar.png?raw=true)

    **Query tersebut akan melakukan perintah untuk menambahkan column "ongkos_dasar" di table kurir setelah column name dengan menggunakan alter table untuk melakukan perubahan.**

5. Rename tabel kurir menjadi shipping.

    ![Gambar Rename table kurir](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/05_Rename-table-kurir.png?raw=true)

    **Query tersebut akan melakukan perintah untuk melakukan penggantian nama pada tabel yang awalnya kurir menjadi shipping. Lalu untuk mengecek apakah berhasil lakukan pengecekan dengan SHOW TABLES; apakah table tersebut sudah berubah.**

6. Hapus / Drop tabel shipping karena ternyata tidak dibutuhkan.

    ![Gambar Drop table shipping](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/06_Drop-table-shipping.png?raw=true)

    **Query tersebut akan melakukan perintah untuk melakukan penghapusan tabel dengan perintah DROP**

7. Silahkan menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many. Seperti:
    - 1-to-1: payment method description.

        ![Gambar Create table payment method description](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/07_Add-Entity-payment_method_description.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan entity baru yaitu sebuah table "payment_method_description" dengan beberapa column seperti id sebagai primary_key, method_id(FK) yang diambil dari tabel Payment_methods, method_description sesuai dengan tipe data yang diinginkan.**

    - 1-to-many: user dengan alamat.

        ![Gambar Create table user_address](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/07_Add-Entity-user_address.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan entity baru yaitu sebuah table "user_address" dengan beberapa column seperti address_id sebagai primary_key, user_id(FK) yang diambil dari tabel Users, address, city, country sesuai dengan tipe data yang diinginkan.**

    - many-to-many: user dengan payment method menjadi user_payment_method_detail.

        ![Gambar Create table user_payment_method_detail](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/07_Add-Entity-user_payment_method_detail.png?raw=true)

        **Query tersebut akan melakukan perintah pembuatan entity baru yaitu sebuah table "user_payment_method_detail" dengan beberapa column seperti user_id(FK) yang diambil dari tabel Users, method_id(FK) yang diambil dari tabel Payment_methods sesuai dengan tipe data yang diinginkan.**

**Tampilan ERD Final**

![Gambar ERD Olshop](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/ERD_Olshop_Finish.png?raw=true)

**Jumlah Table yang ada di Database alta_online-shop**

![Gambar Jumlah Table Database pada Alta Olshop](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/DDL/Tables-in_alta_online_shop.png?raw=true)