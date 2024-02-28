def hitung_luas_persegi_panjang(p, l):
    # Menghitung luas persegi panjang
    L = p * l
    return L

def cek_kelipatan(L):
    # Memeriksa apakah luas persegi panjang genap atau ganjil
    if L % 2 == 0:
        return "even rectangle"  # luas genap
    else:
        return "odd rectangle"   # luas ganjil

# Input panjang dan lebar persegi panjang
p = int(input("p = "))
l = int(input("l = "))

# Hitung luas persegi panjang
L = hitung_luas_persegi_panjang(p, l)

# Cek apakah luas persegi panjang genap atau ganjil
hasil_cek = cek_kelipatan(L)

# Tampilkan hasil
print("Luas persegi panjang:", L)
print("Jenis persegi panjang:", hasil_cek)