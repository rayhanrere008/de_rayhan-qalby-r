def hitung_skor_budget(budget):
    if budget >= 0 and budget <= 50:
        return 4
    elif budget <= 80:
        return 3
    elif budget <= 100:
        return 2
    else:
        return 1

def hitung_skor_waktu(waktu):
    if waktu >= 0 and waktu <= 20:
        return 10
    elif waktu <= 30:
        return 5
    elif waktu <= 50:
        return 2
    else:
        return 1

def hitung_skor_kesulitan(kesulitan):
    if kesulitan >= 0 and kesulitan <= 3:
        return 10
    elif kesulitan <= 6:
        return 5
    elif kesulitan <= 10:
        return 1
    else:
        return 0

def hitung_prioritas(budget, waktu, kesulitan):
    skor_budget = hitung_skor_budget(budget)
    skor_waktu = hitung_skor_waktu(waktu)
    skor_kesulitan = hitung_skor_kesulitan(kesulitan)

    total_skor = skor_budget + skor_waktu + skor_kesulitan

    if total_skor >= 17 and total_skor <= 24:
        return "High"
    elif total_skor >= 10 and total_skor <= 16:
        return "Medium"
    elif total_skor >= 3 and total_skor <= 9:
        return "Low"
    else:
        return "Impossible"

# Input data proyek dari pengguna
budget = int(input("Masukkan budget proyek: "))
waktu = int(input("Masukkan waktu pengerjaan proyek: "))
kesulitan = int(input("Masukkan tingkat kesulitan proyek: "))

# Hitung dan cetak prioritas proyek
prioritas = hitung_prioritas(budget, waktu, kesulitan)
print("Prioritas proyek:", prioritas)
