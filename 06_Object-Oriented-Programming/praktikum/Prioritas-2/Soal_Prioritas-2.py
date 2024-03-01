class KelasLatihan:
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal

    # Metode untuk menampilkan informasi kelas latihan
    def tampilkanInfo(self):
        print("Informasi Kelas Latihan:")
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahunPengalaman)
        print("Jenis Latihan:", self.__jenisLatihan)
        print("Jadwal:", self.__jadwal)


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__tingkatKesulitan = tingkatKesulitan

    # Metode khusus untuk Yoga
    def aturPosisiYoga(self, posisi):
        print("Posisi Yoga telah diatur menjadi:", posisi)

    # Override metode tampilkanInfo() untuk menampilkan informasi spesifik Yoga
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat Kesulitan:", self.__tingkatKesulitan)


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, beratMaksimum):
        super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__beratMaksimum = beratMaksimum

    # Metode khusus untuk Angkat Beban
    def aturBeratBeban(self, berat):
        print("Berat beban telah diatur menjadi:", berat)

    # Override metode tampilkanInfo() untuk menampilkan informasi spesifik Angkat Beban
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Berat Maksimum yang Dapat Diangkat:", self.__beratMaksimum)


# Demonstrasi Polymorphism
def cekInfoKelasLatihan(kelas_latihan):
    kelas_latihan.tampilkanInfo()
    if isinstance(kelas_latihan, Yoga):
        kelas_latihan.aturPosisiYoga("Lotus Pose")
    elif isinstance(kelas_latihan, AngkatBeban):
        kelas_latihan.aturBeratBeban(60)


# Demonstrasi
if __name__ == "__main__":
    # Buat objek Yoga
    yoga_kelas = Yoga("Anselma", "Yoga Instructor", 6, "Yoga", "Senin, Selasa, Kamis", "Intermediate")

    # Buat objek AngkatBeban
    angkat_beban_kelas = AngkatBeban("Rendi", "Weightlifting", 2, "Angkat Beban", "Sabtu, Minggu", 50)

    # Tampilkan informasi kelas latihan dan panggil metode khusus
    cekInfoKelasLatihan(yoga_kelas)
    print("\n")
    cekInfoKelasLatihan(angkat_beban_kelas)