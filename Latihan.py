#-----------0++++++++++5-------------8++++++++++++++11---------------
# x akan True jika x bernilai di antara 0 - 5
# x juga akan True jika x bernilai di antara 8 - 11
#
# x akan False jika x kurang dari 0 dan x lebih dari 11
# x juga akan False jika x bernilai diantara 5 - 8


# Meminta input dari pengguna
x = float(input("Masukkan nilai x: "))

# Evaluasi kondisi menggunakan logika boolean
is_true = (0 < x < 5) or (8 < x < 11)
is_false = (x < 0 or x > 11 or (5 < x < 8))

# Menentukan hasil tanpa if/else tapi menggunakan and not 
result = is_true and not is_false

# Menampilkan hasil
print(f"Maka nilai x = {result}")



#+++++++++++0----------5+++++++++++++8--------------11++++++++++++++++
# x akan False jika x bernilai di antara 0 - 5
# x juga akan False jika x bernilai di antara 8 - 11
#
# x akan True jika x kurang dari 0 dan x lebih dari 11
# x juga akan True jika x bernilai diantara 5 - 8

# Meminta input dari pengguna
x = float(input("Masukkan nilai x: "))

# Evaluasi kondisi menggunakan logika boolean
is_true = (x < 0) or (5 < x < 8) or (x > 11)
is_false = ((0 < x < 5) or (8 < x < 11))

# Menentukan hasil tanpa if/else tapi menggunakan and not 
result = is_true and not is_false

# Menampilkan hasil
print(f"Maka nilai x = {result}")































