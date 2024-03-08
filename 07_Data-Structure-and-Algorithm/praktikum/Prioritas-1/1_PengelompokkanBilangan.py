def group_numbers(numbers, target):
    # Membuat dua list kosong untuk menyimpan kelompok bilangan
    multiples = []
    non_multiples = []
    
    # Mengelompokkan bilangan ke dalam list yang sesuai
    for num in numbers:
        if num % target == 0:
            multiples.append(num)
        else:
            non_multiples.append(num)
    
    # Mengembalikan kelompok bilangan
    return [multiples, non_multiples]

# Test cases
print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # [[3, 6, 9], [1, 2, 4, 5, 7, 8]]
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5))  # [[15, 20, 75, 30, 45], [23, 19]]
