## Soal Merancang Skema Database (Relational Database)

1. Sistem dapat menyimpan data mengenai detail item product, yaitu : product, product_type, product_description, operator, payment_methods.
2. Sistem juga harus menyimpan data mengenai pelanggan yang akan membeli product tsb diantaranya : nama, alamat, tanggal lahir, status_user, gender, created_at, updated_at.
3. Sistem dapat mencatat transaksi pembelian dari pelanggan.
4. Sistem dapat mencatat detail transaksi pembelian dari pelanggan.

**Jawaban :**

**Gambar ERD**

![Gambar ERD](https://github.com/rayhanrere008/de_rayhan-qalby-r/blob/main/08_Relational-Database/screenshots/ERD/ERD-Oldshop.png?raw=true)

1. Sistem dapat menyimpan data mengenai detail item product, yaitu : product, product_type, product_description, operator, payment_methods :

    Terlihat pada tabel product terdapat sebuah attribut yang bisa menyimpan data-data yang diinginkan mulai dari **product_id** sebagai primary key, **product_name**, **type_id** yang diambil dari tabel **Product_types** (Tipe produknya) dengan relasi **many to 1** (1 tipe produk memiliki banyak produk), **description_id** yang diambil dari tabel **Product_descriptions** (deskripsi produknya) dengan relasi **1 to 1** (setiap produk memiliki deskripsi produknya sendiri), **operator_id** yang diambil dari tabel **Operators** dengan relasi **many to 1** (satu operator dapat terikat dengan banyak produk), **method_id** yang diambil dari tabel **Payment_methods** (metode pembayarannya) dengan relasi **many to many** (banyak produk memiliki banyak metode pembayaran).

2. Sistem juga harus menyimpan data mengenai pelanggan yang akan membeli product tsb diantaranya : nama, alamat, tanggal lahir, status_user, gender, created_at, updated_at :

    Terlihat pada tabel **Users** digunakan untuk menyimpan data pelanggan yang akan membeli product. Terdapat atribut **user_id** sebagai primary key, **name** (nama pelanggan), **address** (alamat pelanggan), **date_of_birth** (tanggal lahir pelanggan), **status_user** (jenis level pelanggan), **gender** (jenis kelamin pelanggan), **created_at** (menunjukkan waktu kapan data pelanggan dibuat), **updated_at** (menunjukkan waktu kapan data pelanggan diubah).

3. Sistem dapat mencatat transaksi pembelian dari pelanggan :

    Terlihat pada tabel **Transcations** sistem dapat mencatat transaksi pembelian dari pelanggan dengan menyimpan beberapa attribut seperti **transaction_id** sebagai primary key, **user_id** yang diambil dari data dalam tabel **Users** (data pelanggan) dengan relasi **many to 1** (setiap pelanggan bisa memiliki banyak transaksi), **transaction_date** (tanggal transaksi), **total_amount** (total pembelian), **created_at** (menunjukkan waktu kapan data transaksi dibuat), **updated_at** (menunjukkan waktu kapan data transaksi diubah).

4. Sistem dapat mencatat detail transaksi pembelian dari pelanggan :

    Terlihat pada tabel **Transaction_details** sistem dapat mencatat detail transaksi pembelian dari pelanggan dengan menyimpan beberapa attribut seperti **transaction_detail_id** sebagai primary key, **transaction_id** yang diambil dari data dalam tabel **Transaction** (data transaksi pelanggan) dengan relasi **1 to many** (satu transaksi memiliki banyak detail transaksi), **product_id** yang diambil dari data dalam tabel **Products** (data produk) dengan **relasi 1 to 1** (satu produk hanya terikat dengan 1 detail transaksi), **quantity** (jumlah produk yang dibeli), **unit_price** (harga satuan yang dibeli).

