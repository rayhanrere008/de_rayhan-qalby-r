class KelasLatihan:
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal
        self.__tersedia = True

    # Metode untuk menampilkan informasi kelas latihan
    def tampilkanInfo(self):
        print("Informasi Kelas Latihan:")
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahunPengalaman)
        print("Jenis Latihan:", self.__jenisLatihan)
        print("Jadwal:", self.__jadwal)

    # Metode untuk memesan kelas
    def pesanKelas(self):
        if self.__tersedia:
            print("Kelas", self.__jenisLatihan, "berhasil dipesan.")
            self.__tersedia = False
        else:
            print("Maaf, kelas", self.__jenisLatihan, "sudah penuh.")

    # Metode untuk membatalkan kelas
    def batalkanKelas(self):
        if not self.__tersedia:
            print("Kelas", self.__jenisLatihan, "telah berhasil dibatalkan.")
            self.__tersedia = True
        else:
            print("Kelas", self.__jenisLatihan, "belum dipesan.")


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__tingkatKesulitan = tingkatKesulitan

    # Override metode pesanKelas() untuk aturan pemesanan kelas yoga
    def pesanKelas(self, tingkat_kesulitan):
        if self._KelasLatihan__tersedia and self.__tingkatKesulitan == tingkat_kesulitan:
            print("Kelas", self._KelasLatihan__jenisLatihan, "berhasil dipesan.")
            self._KelasLatihan__tersedia = False
        elif not self._KelasLatihan__tersedia:
            print("Maaf, kelas", self._KelasLatihan__jenisLatihan, "sudah penuh.")
        elif self.__tingkatKesulitan != tingkat_kesulitan:
            print("Maaf, hanya pelanggan dengan tingkat kesulitan", self.__tingkatKesulitan, "yang dapat memesan kelas", self._KelasLatihan__jenisLatihan + ".")

    # Override metode batalkanKelas() untuk aturan pembatalan kelas yoga
    def batalkanKelas(self):
        if not self._KelasLatihan__tersedia:
            print("Kelas", self._KelasLatihan__jenisLatihan, "telah berhasil dibatalkan.")
            self._KelasLatihan__tersedia = True
        else:
            print("Kelas", self._KelasLatihan__jenisLatihan, "belum dipesan.")


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, beratMaksimum):
        super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__beratMaksimum = beratMaksimum

    # Override metode pesanKelas() untuk aturan pemesanan kelas angkat beban
    def pesanKelas(self, berat):
        if self._KelasLatihan__tersedia and berat <= self.__beratMaksimum:
            print("Kelas", self._KelasLatihan__jenisLatihan, "berhasil dipesan.")
            self._KelasLatihan__tersedia = False
        elif not self._KelasLatihan__tersedia:
            print("Maaf, kelas", self._KelasLatihan__jenisLatihan, "sudah penuh.")
        else:
            print("Maaf, hanya pelanggan dengan beban maksimum kurang dari atau sama dengan", self.__beratMaksimum, "kg yang dapat memesan kelas", self._KelasLatihan__jenisLatihan + ".")

    # Override metode batalkanKelas() untuk aturan pembatalan kelas angkat beban
    def batalkanKelas(self):
        if not self._KelasLatihan__tersedia:
            print("Kelas", self._KelasLatihan__jenisLatihan, "telah berhasil dibatalkan.")
            self._KelasLatihan__tersedia = True
        else:
            print("Kelas", self._KelasLatihan__jenisLatihan, "belum dipesan.")


# Fungsi untuk menampilkan menu pilihan
def tampilkanMenu():
    print("\nMenu:")
    print("1. Pesan Kelas")
    print("2. Batalkan Kelas")
    print("3. Keluar")
    return input("Pilih menu: ")


# Demonstrasi
if __name__ == "__main__":
    # Buat objek Yoga
    yoga_kelas = Yoga("Anselma", "Yoga Instructor", 6, "Yoga", "Senin, Selasa, Kamis", "Intermediate")

    # Buat objek AngkatBeban
    angkat_beban_kelas = AngkatBeban("Rendi", "Weightlifting", 2, "Angkat Beban", "Sabtu, Minggu", 50)

    while True:
        menu = tampilkanMenu()
        if menu == "1":
            submenu = input("Pilih jenis kelas (1. Yoga, 2. Angkat Beban): ")
            if submenu == "1":
                tingkat_kesulitan = input("Masukkan tingkat kesulitan (Beginner, Intermediate, Advanced): ")
                yoga_kelas.pesanKelas(tingkat_kesulitan)
            elif submenu == "2":
                berat = float(input("Masukkan berat maksimum yang bisa diangkat (kg): "))
                angkat_beban_kelas.pesanKelas(berat)
            else:
                print("Opsi tidak valid.")
        elif menu == "2":
            submenu = input("Pilih jenis kelas (1. Yoga, 2. Angkat Beban): ")
            if submenu == "1":
                print("\nPembatalan kelas Yoga:")
                yoga_kelas.batalkanKelas()
            elif submenu == "2":
                print("\nPembatalan kelas AngkatBeban:")
                angkat_beban_kelas.batalkanKelas()
            else:
                print("Opsi tidak valid.")
        elif menu == "3":
            break
        else:
            print("Menu tidak valid.")