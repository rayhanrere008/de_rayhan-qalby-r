import pandas as pd

# Data
data = {
    'Nama': ['John', 'Anna', 'Peter', 'Linda'],
    'Usia': [28, 35, 45, 32],
    'Kota': ['New York', 'Paris', 'London', 'Berlin']
}

# Buat DataFrame
df = pd.DataFrame(data)

def main():
    # Tampilkan DataFrame
    print("DataFrame Awal:")
    print(df)

    # Lakukan manipulasi data
    df['Usia'] = df['Usia'] + 1

    # Tampilkan DataFrame setelah manipulasi
    print("\nDataFrame Setelah Manipulasi Usia:")
    print(df)

if __name__ == '__main__':
    main()
