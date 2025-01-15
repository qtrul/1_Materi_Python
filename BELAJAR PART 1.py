# Fungsi untuk menambahkan dua angka
def tambah(x, y):
    return x + y

# Fungsi untuk mengurangkan dua angka
def kurang(x, y):
    return x - y
# Fungsi nya apa
# Fungsi untuk mengalikan dua angka
def kali(x, y):
    return x * y

# Fungsi untuk membagi dua angka
def bagi(x, y):
    return x / y

# Tampilan pilihan operasi
print("Pilih Operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

# Meminta input dari pengguna
pilihan = input("Masukkan pilihan(1/2/3/4): ")

num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(num1, "+", num2, "=", tambah(num1, num2))

elif pilihan == '2':
    print(num1, "-", num2, "=", kurang(num1, num2))

elif pilihan == '3':
    print(num1, "*", num2, "=", kali(num1, num2))

elif pilihan == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", bagi(num1, num2))
    else:
        print("Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Pilihan tidak valid")

