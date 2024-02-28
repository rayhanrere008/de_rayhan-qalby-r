def cek_anagram(kata1, kata2):
    # Menghapus spasi dan mengubah huruf menjadi lowercase
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Jika panjang kedua kata tidak sama, bukan anagram
    if len(kata1) != len(kata2):
        return False

    # Menghitung frekuensi setiap huruf pada kata pertama
    frekuensi = {}
    for huruf in kata1:
        if huruf in frekuensi:
            frekuensi[huruf] += 1
        else:
            frekuensi[huruf] = 1

    # Membandingkan frekuensi huruf pada kata kedua
    for huruf in kata2:
        if huruf in frekuensi:
            frekuensi[huruf] -= 1
        else:
            # Jika huruf tidak ada di kata pertama, bukan anagram
            return False

    # Memastikan semua frekuensi huruf adalah nol
    for value in frekuensi.values():
        if value != 0:
            return False

    return True

# Input dua kata dari pengguna
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

# Memeriksa apakah kata tersebut adalah anagram dan mencetak output
if cek_anagram(kata1, kata2):
    print("Anagram")
else:
    print("Bukan Anagram")
