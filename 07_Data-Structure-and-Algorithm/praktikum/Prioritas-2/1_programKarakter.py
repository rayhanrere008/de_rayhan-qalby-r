def collect_chars(word, rooms):
    # Menghapus spasi dari kata
    word = word.replace(" ", "")
    
    # Hitung berapa kali kata harus diulang untuk mencapai jumlah ruangan
    repeat_count = rooms // len(word)
    
    # Buat string hasil dengan mengulang kata sebanyak yang diperlukan
    result = word * repeat_count
    
    # Sisa ruangan yang belum terpenuhi
    remaining_rooms = rooms % len(word)
    
    # Tambahkan karakter dari awal kata untuk memenuhi sisa ruangan
    result += word[:remaining_rooms]
    
    return result

# Test cases
print(collect_chars("alta", 10))  # altaaltaal
print(collect_chars("sepulsa", 20))  # sepulsasepulsasepuls
print(collect_chars("sepulsa mantap", 20))  # sepulsamantapsepulsa
