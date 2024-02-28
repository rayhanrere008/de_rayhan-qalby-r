def hitung_tarif(berat, jarak):
    # Tarif berdasarkan berat paket
    if berat >= 1 and berat <= 20:
        tarif_berat = 10000
    elif berat <= 30:
        tarif_berat = 15000
    elif berat <= 60:
        tarif_berat = 20000
    else:
        tarif_berat = 45000

    # Tarif berdasarkan jarak
    if jarak >= 1 and jarak <= 5:
        tarif_jarak = 2000
    elif jarak <= 15:
        tarif_jarak = 5000
    elif jarak <= 30:
        tarif_jarak = 10000
    else:
        tarif_jarak = 15000

    # Total tarif
    total_tarif = tarif_berat + tarif_jarak
    return total_tarif

# Input berat dan jarak dari pengguna
berat = int(input("Berat: "))
jarak = int(input("Jarak: "))

# Hitung dan cetak tarif
tarif = hitung_tarif(berat, jarak)
print("Tarif pengiriman:", tarif)
