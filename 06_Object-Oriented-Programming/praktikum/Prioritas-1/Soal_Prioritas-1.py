class Pelanggan:
    def __init__(self, nama, usia, IdPelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__IdPelanggan = IdPelanggan
    
    # Method Getter
    def getNama(self):
        return self.__nama
    def getUsia(self):
        return self.__usia
    def getIdPelanggan(self):
        return self.__IdPelanggan
    
    # Method Setter
    def setNama(self, nama):
        self.__nama = nama
    def setUsia(self, usia):
        self.__usia = usia
    def setIdPelanggan(self, IdPelanggan):
        self.__IdPelanggan = IdPelanggan
    
    # Method untuk menampilkan informasi pelanggan
    def tampilkanInfo(self):
        print("Informasi Pelanggan:")
        print("Nama:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__IdPelanggan)
        print()


class Pelatih:
    def __init__(self, nama, spesialisasi, tahunPengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman
    
    # Method Getter
    def getNama(self):
        return self.__nama
    def getSpesialisasi(self):
        return self.__spesialisasi
    def getTahunPengalaman(self):
        return self.__tahunPengalaman
    
    # Method Setter
    def setNama(self, nama):
        self.__nama = nama
    def setSpesialisasi(self, spesialisasi):
        self.__spesialisasi = spesialisasi
    def setTahunPengalaman(self, tahunPengalaman):
        self.__tahunPengalaman = tahunPengalaman
    
    # Method untuk menampilkan informasi pelatih
    def tampilkanInfo(self):
        print("Informasi Pelatih:")
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahunPengalaman)
        print()

    
class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(nama, spesialisasi, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal
    
    # Getter
    def getJenisLatihan(self):
        return self.__jenisLatihan
    
    def getJadwal(self):
        return self.__jadwal
    
    # Setter
    def setJenisLatihan(self, jenisLatihan):
        self.__jenisLatihan = jenisLatihan
    
    def setJadwal(self, jadwal):
        self.__jadwal = jadwal
    
    # Override metode tampilkanInfo untuk menampilkan informasi tambahan
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Jenis Latihan:", self.__jenisLatihan)
        print("Jadwal:", self.__jadwal)
        print()

# Demonstrasi
if __name__ == "__main__":
    # Buat objek Pelanggan
    pelanggan1 = Pelanggan("Rayhan", 21, "P001")
    
    # Buat objek Pelatih
    pelatih1 = Pelatih("Dedy", "Bodybuilding", 6)
    
    # Buat beberapa objek KelasLatihan
    kelas1 = KelasLatihan("Ganesya", "Cardio", 3, "Balance", "Jumat, Sabtu, Minggu")
    kelas2 = KelasLatihan("Sopyan", "Crossfit", 5, "Interval Training", "Rabu, Kamis")
    
    # Tampilkan informasi setiap objek menggunakan method tampilkanInfo()
    pelanggan1.tampilkanInfo()
    
    pelatih1.tampilkanInfo()
    
    kelas1.tampilkanInfo()
    kelas2.tampilkanInfo()