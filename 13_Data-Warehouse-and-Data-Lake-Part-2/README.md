## Data Warehouse and Data Lake Part 2 - Resume

**Columnar table** adalah jenis tabel yang disusun secara vertikal, dengan setiap kolom menyimpan nilai dari satu jenis data. **Dalam Citus**, menggunakan columnar table bisa menjadi strategi yang baik dalam beberapa situasi, terutama ketika terdapat query yang membutuhkan akses ke sebagian kecil dari kolom dalam tabel yang sangat besar. Dengan penyimpanan kolom, hanya kolom yang diperlukan yang akan dimuat, mengurangi jumlah data yang harus dipindahkan dan memungkinkan eksekusi query menjadi lebih cepat. Untuk perintah kueri saat ingin menggunakan columnar table biasanya terdapat sintaks **USING columnar;**. Di Citus, **sharding** dan **replikasi** adalah dua fitur kunci yang memungkinkan penyebaran dan replikasi data secara terdistribusi untuk meningkatkan kinerja, ketersediaan, dan skalabilitas. **Sharding** adalah proses membagi data menjadi bagian-bagian yang lebih kecil yang disebut shard dan mendistribusikannya ke beberapa node atau server. Kueri penggunaan sharding adalah **SELECT create_distributed_table();**. Replikasi adalah proses membuat dan memelihara salinan data yang identik di beberapa lokasi untuk meningkatkan ketersediaan data dan toleransi terhadap kegagalan. Kueri penggunaan replication adalah **SELECT create_reference_tables();**. Selain itu terdapat juga **Collocation** yang merupakan sebuah konsep dalam database terdistribusi, di mana data yang sering diakses bersama-sama ditempatkan atau dikelompokkan bersama di node yang sama dalam klaster. 