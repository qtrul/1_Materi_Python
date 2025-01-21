#print ("BAB 11")
#print("------")
#
#'''           ====BAB 11 (BITWISE)====                                 
#'''
#a = 9
#b = 5
#
## Bitwise OR (|)
#print ("==============OR==============")
#print ("Nilai a =", a, ", binary:", format(a,"08b"))
#print ("Nilai b =", b, ", binary:", format(b,"08b"))
#print ("------------------------------(|)")
#c = a | b
#print ("Nilai c =", c, ", binary:", format(c,"08b"))
#
## Bitwise AND (&)
#print ("\n=============AND==============")
#print ("Nilai a =", a, ", binary:", format(a,"08b"))
#print ("Nilai b =", b, ", binary:", format(b,"08b"))
#print ("------------------------------(&)")
#c = a & b
#print ("Nilai c =", c, ", binary:", format(c,"08b"))
#
## Bitwise XOR (^)
#print ("\n=============XOR==============")
#print ("Nilai a =", a, ", binary:", format(a,"08b"))
#print ("Nilai b =", b, ", binary:", format(b,"08b"))
#print ("------------------------------(^)")
#c = a ^ b
#print ("Nilai c =", c, ", binary:", format(c,"08b"))
#
## Bitwise NOT (~)
#print ("\n=============NOT==============")
#print ("Nilai a =", a, ", binary:", format(a,"08b"))
#print ("------------------------------(~)")
#c = ~a
#print ("Nilai c =", c, ", binary:", format(c,"08b"))
#print ("------------------------------(^)") 
#d = 0b00001001  #gunakan XOR NOT jika ingin mengflip semua biner 
#e = 0b11111111
#print ("Nilai e =", e^d, ", binary:", format(e^d,"08b"))
#
## Shifting (mengeser-geser)
## Shifting right (>>)
#print ("\n========Shifting right========")
#c = a >> 2
#print ("Nilai a =", a, ", binary:", format(a,"08b"))
#print ("------------------------------(>>)")
#print ("Nilai c =", c, ", binary:", format(c,"08b"))
#
## Shifting left (<<)
#print ("\n========Shifting left========")
#c = a << 2
#print ("Nilai a =", a, ", binary:", format(a,"08b"))
#print ("------------------------------(<<)")
#print ("Nilai c =", c, ", binary:", format(c,"08b"))
#
#print ("")
#
#
#
#
#
#
#
#
#
#print ("BAB 12")
#print("------")
#
#'''           ====BAB 12 (PENGENALAN STRING)====                                 
#'''
#
## 1. cara membuat string 
#
#'''
#    1. menggunakan single quote '...'
#    2. menggunakan double quote "..."
#    3. menggunakan single dan double quote secara bersamaan '"..."' atau "'...'"
#'''
#
#data = 'menggunakan single quote'
#print  (data)
#
#data = "menggunakan double quote"
#print  (data)
#
#data = '"menggunakan single dan double quote secara bersamaan"'
#print  (data)
#
#data = "'menggunakan single dan double quote secara bersamaan'"
#print  (data)
#
## 2. Penggunakan tanda (\)
#
## 3. mengubah tanda (') menjadi string 
#print ('hari ini adalah hari jum\'at') # ditambah \ sebelum '
#
## 4. mengubah tanda (\) menjadi string 
#print ('https:\\ucup.com') # ditambah \ sebelum \
#
## 5. tab (\t)
#print ('ucup\tdimas')
#print ('ucup\t\t\tdimas') # bisa di stuck
#
## 6. backspace (\b)
#print ('ucup \bdimas')
#
## 7. newline (\n, \r, \r\n) di windows menggunakan \r\n
#print ('baris pertama.\r\nbaris kedua.')
#
## 8. string literal atua raw 
#print (r'ucup www.com\t\n\r\n\b') 
#
#''' menggunakan raw jika terdapat banyak \ dan 
#    ingin menampilkan banyak \ kedalam terminal 
#'''
#
## 9. multiline ("""...""") maka akan di print semua 
#print ("""
#    nama = ghois
#    prodi = d3 teknik kimia
#    jurusan = teknik kimia
#    asal = pasuruan
#       """)
#
#
#
#
#
#
#
#
#print ("BAB 13")
#print("------")
#
#'''           ====BAB 13 (OPERASI DAN MANUPULASI STRING)====
#'''
#
## 1. menyambung string 
#
#nama_depan = "Bayu"
#nama_tengah = "An"
#nama_belakang = "organik"
#
#nama_lengkap = nama_depan + " " + nama_tengah + nama_belakang
#print ("Nama lengkap = ", nama_lengkap)
#print ("------------------------------")
#
#
#
#
## 2. menghitung panjang string 
#
#panjang = len(nama_lengkap)
#print ("Panjang dari", nama_lengkap, "=",panjang)
#print ("------------------------------")
#
#
#
#
## 3. mengecek apakah ada komponen char di dalam string 
#
#y = "y"
#status = y in nama_lengkap
#print ("string", y , "ada di", nama_lengkap, ":",  status,)
#
#b = "b" 
#status = b in nama_lengkap
#print ("string", b , "ada di", nama_lengkap, ":",  status)
#
#        # hasil b false karna b yang ada di Bayu Anorganik adalah B besar bukan b kecil
#
#b = "b" 
#status = b not in  nama_lengkap
#print ("string", b , "tidak ada di", nama_lengkap, ":",  status)
#
#print ("------------------------------")
#
#
#
#
## 4. mengulang string 
#
#print ("awok"*5)
#print (5*"awok")
#
#print ("------------------------------")
#
#
#
#
## 5. indexing
#
#print ("index ke-0 =", nama_lengkap[0])
#print ("index ke-8 =", nama_lengkap[8])
#print ("index ke-(-1) =", nama_lengkap[-1]) # jika min maka dihitung dari belakang 
#print ("index ke-(-4) =", nama_lengkap[-4])
#print ("index ke-(0:4) =", nama_lengkap[0:4])
#print ("index ke-(5:9) =", nama_lengkap[5:9])
#print ("index ke-(2, 4, 6, 8, 10) =", nama_lengkap[0:10:2])
#
#print ("------------------------------")
#
## 6. item paling kecil
#
#print ("Item yang nilai paling kecil \ndi", nama_lengkap, "adalah:", min(nama_lengkap))
#
#print ("------------------------------")
#
## 7. item paling besar
#
#print ("Item yang nilai paling besar \ndi", nama_lengkap, "adalah:", max(nama_lengkap))
#
#print ("------------------------------")
#
## 8. ASCII CODE 
##
## fungsinya adalah untuk mengubah huruf menjadi angka dan angka menjadi huruf 
## ord = untuk mengubah huruf menjadi angka
## chr = untuk mengubah angka menjadi huruf 
##
#kode = ord("K")
#print ("Angka dari huruf K adalah:", kode)
#
#kode = 80
#print ("Huruf dari angka", kode , "adalah:", chr(kode))
#
#print ("------------------------------")
#
#
#
#
#
## 9. operator dalam bentuk metode
#
#data = "fahri daur ulang"
#jumlah = data.count("u")
#print ("jumlah u dalam", data, "=", jumlah,)
#
#data = "bedeh bedhek \nebebebenh bedenh bedek pedhe"
#jumlah = data.count("e")
#print ("jumlah e dalam", data, "=", jumlah)
#jumlah = data.count("b")
#print ("jumlah b dalam", data, "=", jumlah)
#
#


















print ("============================")