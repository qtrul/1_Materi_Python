






print ("BAB 28")
print("------")

'''           ====BAB 28 (MANIPULASI LIST)====
''' 

# index  0(-3)    1(-2)   2(-1)
data = ["gois", "aray", "dapin"]

# 1. mengambil data dari list 
data_0 = data[0]
print(data_0)

data_terakhir = data[-1]
print (data_terakhir)

data_aray = data[1]
print (data_aray)

print (10*'=', 'Ending', '='*10, '\n')

# 2. mengambil info jumlah data dalam list

data_jumlah = len(data)
print(f"Panjang data = {data_jumlah}")

print (10*'=', 'Ending', '='*10, '\n')

# 3. menambahkan item pada list sesuai posisi

print(f"Data sebelum ditambahkan\n:{data}")
data.insert(2, "ima")
print (f"Data setelah ditambahkan\n:{data}")

print (10*'=', 'Ending', '='*10, '\n')

# 4. menambahkan item di akhir list

print(f"Data sebelum ditambahkan\n:{data}")
data.append("alysia")
print (f"Data setelah ditambahkan\n:{data}")

print (10*'=', 'Ending', '='*10, '\n')

# 5. menambah list dengan list 

print(f"Data sebelum ditambahkan\n:{data}")
data_baru = ["firgi", "radit", "imel"]
data.extend(data_baru)
print (f"Data setelah ditambahkan\n:{data}")

print (10*'=', 'Ending', '='*10, '\n')

# 6. merubah data
        # cth merubah data 5 menjadi "andro"

print(f"Data sebelum ditambahkan\n:{data}")
data[5] = "andro"
print (f"Data setelah ditambahkan\n:{data}")

print (10*'=', 'Ending', '='*10, '\n')

# 7. menghapus data

print(f"Data sebelum ditambahkan\n:{data}")
data.remove('andro')
print (f"Data setelah ditambahkan\n:{data}")

print (10*'=', 'Ending', '='*10, '\n')

# 8. menghapus data paling belakang 

print(f"Data sebelum ditambahkan\n:{data}")
data.pop()
print (f"Data setelah ditambahkan\n:{data}")

print (10*'=', 'Ending', '='*10, '\n')

# 9. mengeluarkan data paling belakang 

print(f"Data sebelum dikeluarkan\n:{data}")
data_data = data.pop()
print (f"Data setelah dikeluarkan\n:{data_data}")

print (10*'=', 'Ending', '='*10, '\n')

