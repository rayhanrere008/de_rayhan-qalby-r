phi = 3.14  # Inisialisasi nilai phi

def hitung_volume_bola(r):
    # Menghitung volume bola
    V = (4/3) * phi * r**3
    return V

# Masukkan jari-jari bola
r = float(input("r bola: "))

# Hitung volume bola
V = hitung_volume_bola(r)

# Tampilkan hasil
print("Volume bola :", V)
