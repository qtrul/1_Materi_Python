print("")
print ("PENDAHULUAN")
print("------------")

#BAB 1 (VARIABEL)
#larangan dalam menulis variable
#   1. 10data =     (tidak boleh, angka tidak boleh di depan huruf)
#      data10 =     (boleh)
#   2. data 10 =    (tidak boleh ada spasi)
#      data-10 =    (tidak boleh ) 
#      data_10 =    (boleh)
#   3. 1000 = 10    (tidak boleh angka)
#      a = 10       (boleh)

print("") # hanya spasi

print("BAB 1")

a = 10
b = 25 

print ("a" , "b")

print("") # hanya spasi

print("BAB 2")

#BAB 2 (TIPE DATA)
#   1. Integer adalah tipe data angka tanpa koma atau bilangan bulat. cth: 1, 2, 3
a = 100
print ("data = ", a)
print ("- bertipe =", type (a))

#   2. Float adalah tipe data angka dengan koma. cth: 1.2, 1.3, 4.5
b = 100.5
print ("data = ", b)
print ("- bertipe = ", type (b))

#   3. String adalah tipe data kumpulan karakter cth: jarwo, cerek, curuk
c = "jarwo"     # harus di kasih tanda petik "...", jarwo 10 juga termasuk string meski ada angka nya
print ("data = ", c)
print ("- bertipe = ", type (c))

#   4. boolean adalah tipe data yang hanya ada 2 pilihan yaitu true atau false 
d = True # bisa juga diganti False, harus kapital di awal kata
print ("data = ", d)
print ("- bertipe = ", type (d))

print("") # hanya spasi

print("BAB 3")

#BAB 3 (TIPE DATA KHUSUS)
#   1. Bilangan kompleks yaitu yang terdiri dari bilangan real dan imajiner 
e = complex (5,6) # 5 adalah bilangan real, 6 adalah biangan imajiner 
print ("data = ", e)
print ("- bertipe = ", type (e))


#   2. Tipe data dari bahasa C adalah kita bisa menggunakan tipe data dari bahasa C 

from ctypes import c_double # bisa menggunakan tipe bahasa yang lain seperti float dan lain-lain 
f = c_double(100.5)
print ("data = ", f)
print ("- bertipe = ", type (f))

print("") # hanya spasi




















print("") # hanya spasi
print("") # hanya spasi
print("") # hanya spasi
print("") # hanya spasi