'''                   ==== JUDUL SETIAP BAB ====

====BAB 1  (Variabel)
====BAB 2  (Tipe Data)
====BAB 3  (Tipe Data Khusus)
====BAB 4  (Casting atau Mengubah Tipe Data)
====BAB 5  (Input atau Mengambil Tipe Data)
====BAB 6  (Operasi Aritmatika)
====BAB 7  (Pengaplikasian Operasi Aritmatika)
====BAB 8  (Operasi Komparasi)
====BAB 9  (Operasi Logika atau Boolean)
====BAB 10 (Operasi Logika dan Komparasi)
====BAB 11 (Bitwise)
====BAB 12 (Pengenalan String)
====BAB 13 (Operasi dan Manupulasi String)
====BAB 14 (Operator Dalam Bentuk Metode)
====BAB 15 (Format String)
====BAB 16 (String Width and Multiline)
====BAB 17 (Date and Time)
====BAB 18 (if and else statement)
====BAB 19 (elif = else if statement)
====BAB 20 (Membuat Kalkulator Sederhana)
====BAB 21 (for loop (perulangan))
====BAB 22 (while loop)
====BAB 23 (continue and pass)
====BAB 24 (break)
====BAB 25 (Latihan loop (for and while))
====BAB 26 (Latihan Membuat Bangun Datar Menggunakan loop)
====BAB 27 (list)
====BAB 28 (manipulasi list)
====BAB 29 (Operasi list)
====BAB 30 (Cara Menduplikat list)
====BAB 31 (Membuat list di Dalam list)
====BAB 32 (Menduplikat list Menggunakan depp copy)       
====BAB 33 (looping dari list)
====BAB 34 (Latihan list Sederhana)
====BAB 35 (tuples dan sets)
====BAB 36 (dictionary (dict))
====BAB 37 (Operasi pada dictionary)
====BAB 38 (looping dictionary)
====BAB 39 (copy and pop dictionary)
====BAB 40 (multi keys dan nesting dictionary)
====BAB 41 (Latihan dictionary part 1)
====BAB 42 (Latihan dictionary part 2)
====BAB 43 (Pengenalan fungsi)
====BAB 44 (fungsi Dengan argument)
====BAB 45 (fungsi Dengan return)
====BAB 46 (default argumen fungsi)
====BAB 47 (Latihan fungsi)
====BAB 48 (Penggunaan type hints pada fungsi)
====BAB 49 (Penggunaan *args)
====BAB 50 (Penggunaan **kwargs)
====BAB 51 (fungsi lambda dan anonymous)
====BAB 52 (global dan locak scope)
====BAB 53 (import statement)
====BAB 54 (Penggunaan from dan alias(as))
====BAB 55 (Cara Menghitung Waktu Eksekusi Suatu File Dalam Python)
====BAB 56 (Membuat package Sederhana)
====BAB 57 (Cara Penggunaan __init__.py)
====BAB 58 (standard library)
====BAB 59 (tkinter)
====BAB 60 (Mengenal pip)
====BAB 61 (Package Numpy (contoh PIP))
====BAB 62 (Membuat Game sederhana Menggunakan Pygame)
====BAB 63 (Cara Penggunaan __main__.py)
====BAB 64 (Membaca File Eksternal dengan open dan with)
====BAB 65 (Menulis File Eksternal)
====BAB 66 (Mengenal Macam-macam error dan try-except)

'''

print("-------------------------------------------------------------------------------------------------------------------")

'''
                        ==== CODE PENTING ====

1. type()  
   - Fungsi: Mengembalikan tipe data suatu objek.  
   - Terdapat di **BAB 2** dan beberapa tempat lain.

2. input(prompt)  
   - Fungsi: Mengambil input dari pengguna.  
   - Terdapat di **BAB 5** dan beberapa bab lainnya.

3. abs(x)  
   - Fungsi: Mengembalikan nilai absolut dari angka.  
   - Terdapat di **BAB 7** (operasi aritmatika).

4. min()  
    - Fungsi: Mengembalikan nilai minimum dari iterable.  
    - Terdapat di **BAB 13**.

5. max()  
    - Fungsi: Mengembalikan nilai maksimum dari iterable.  
    - Terdapat di **BAB 13**.

6. .count(value)  
    - Fungsi: Menghitung jumlah kemunculan elemen tertentu dalam string.  
    - Terdapat di **BAB 13**.

7. ord(char)  
    - Fungsi: Mengembalikan nilai Unicode dari karakter tertentu.  
    - Terdapat di **BAB 13**.

8. chr(code)  
    - Fungsi: Mengembalikan karakter berdasarkan nilai Unicode.  
    - Terdapat di **BAB 13**.

9. .upper()  
   - Fungsi: Mengubah string menjadi huruf besar.  
   - Terdapat di **BAB 14**.

10. .lower()  
    - Fungsi: Mengubah string menjadi huruf kecil.  
    - Terdapat di **BAB 14**.

11. .rjust(width, fillchar) 
    - Fungsi: Meratakan string ke kanan dengan padding.  
    - Terdapat di **BAB 14**.

12. .ljust(width, fillchar) 
    - Fungsi: Meratakan string ke kiri dengan padding.  
    - Terdapat di **BAB 14**.

13. .center(width, fillchar)  
    - Fungsi: Meratakan string di tengah dengan padding.  
    - Terdapat di **BAB 14**.

14. .strip(chars)  
    - Fungsi: Menghapus karakter tertentu dari awal dan akhir string.  
    - Terdapat di **BAB 14**.

15. .startswith(prefix)  
    - Fungsi: Mengecek apakah string dimulai dengan prefix tertentu.  
    - Terdapat di **BAB 14**.

16. .endswith(suffix)  
    - Fungsi: Mengecek apakah string diakhiri dengan suffix tertentu.  
    - Terdapat di **BAB 14**.

17. .join(iterable)  
    - Fungsi: Menggabungkan elemen iterable menjadi string.  
    - Terdapat di **BAB 14**.

18. .split(separator)  
    - Fungsi: Memisahkan string menjadi elemen-elemen berdasarkan separator tertentu.  
    - Terdapat di **BAB 14**.

19. .isspace()` 
    - Fungsi: Mengecek apakah string hanya berisi karakter spasi.  
    - Terdapat di **BAB 14**.

20. .isalpha()  
    - Fungsi: Mengecek apakah string hanya berisi huruf.  
    - Terdapat di **BAB 14**.

21. .isalnum()  
    - Fungsi: Mengecek apakah string berisi huruf dan angka tanpa karakter khusus.  
    - Terdapat di **BAB 14**.

22. .isdecimal()  
    - Fungsi: Mengecek apakah string hanya berisi angka desimal.  
    - Terdapat di **BAB 14**.

23. .title()  
    - Fungsi: Mengubah huruf pertama setiap kata menjadi huruf besar.  
    - Terdapat di beberapa bagian manipulasi string.

24. .format()  
    - Fungsi: Memformat string dengan nilai yang diberikan.  
    - Terdapat di **BAB 15**.

25. range(start, stop, step)  
    - Fungsi: Mengembalikan urutan angka berdasarkan parameter.  
    - Terdapat di **BAB 21**.

26. .append()  
    - Fungsi: Menambahkan elemen baru di akhir list.  
    - Terdapat di **BAB 28**.

27. .insert(index, value)  
    - Fungsi: Menyisipkan elemen pada indeks tertentu di list.  
    - Terdapat di **BAB 28**.

28. .extend(iterable)  
    - Fungsi: Menambahkan elemen iterable ke akhir list.  
    - Terdapat di **BAB 28**.
29. .pop()  
    - Fungsi: Menghapus elemen terakhir dalam list dan mengembalikannya.  
    - Terdapat di **BAB 28**.

30. .remove(value)  
    - Fungsi: Menghapus elemen tertentu dari list.  
    - Terdapat di **BAB 28**.

31. len()  
    - Fungsi: Mengembalikan jumlah elemen dalam iterable.  
    - Terdapat di **BAB 28**.
                                                                                                                                                                                       
32. type()  
    - Fungsi: Mengembalikan tipe data suatu objek.  
    - Terdapat di **BAB 2** dan beberapa tempat lain.

33. float()  
    - Fungsi: Mengonversi nilai menjadi tipe float.  
    - Terdapat di **BAB 4** dan **BAB 5**.

34. int()  
    - Fungsi: Mengonversi nilai menjadi tipe integer.  
    - Terdapat di **BAB 4** dan **BAB 5**.

35. bool()  
    - Fungsi: Mengonversi nilai menjadi boolean.  
    - Terdapat di **BAB 4**.

36. complex()  
    - Fungsi: Membuat angka kompleks dari bilangan real dan imajiner.  
    - Terdapat di **BAB 3**.

37. from ctypes import c_double  
    - Fungsi: Mengimpor tipe data dari modul `ctypes`.  
    - Terdapat di **BAB 3**.

38. is  
    - Fungsi: Membandingkan dua objek apakah memiliki referensi yang sama.  
    - Terdapat di **BAB 8**.

39. is not  
    - Fungsi: Mengecek apakah dua objek tidak memiliki referensi yang sama.  
    - Terdapat di **BAB 8**.

40. and`, `or`, `not  
    - Fungsi: Operator logika untuk mengoperasikan nilai boolean.  
    - Terdapat di **BAB 9**.

41.`+`, `-`, `*`, `/`, `//`, `%`, `**  
    - Fungsi: Operator aritmatika untuk operasi matematika dasar, modulus, dan pangkat.  
    - Terdapat di **BAB 6**.

42. if`, `elif`, `else  
    - Fungsi: Struktur kontrol untuk mengatur alur logika berdasarkan kondisi.  
    - Terdapat di beberapa bagian dalam file Anda.

43. while  
    - Fungsi: Struktur perulangan untuk mengulang blok kode berdasarkan kondisi.  
    - Terdapat di **BAB 22**.

44. break  
    - Fungsi: Menghentikan perulangan lebih awal.  
    - Terdapat di **BAB 24**.

45. continue  
    - Fungsi: Melewati iterasi saat ini dan melanjutkan iterasi berikutnya.  
    - Terdapat di **BAB 23**.

46. pass
    - Fungsi: Menandai blok kosong tanpa menghasilkan error.  
    - Terdapat di **BAB 23**.

47. bin()  
    - Fungsi: Mengonversi bilangan menjadi representasi biner.  
    - Terdapat di **BAB 15**.

48. oct()  
    - Fungsi: Mengonversi bilangan menjadi representasi oktal.  
    - Terdapat di **BAB 15**.

49. hex()  
    - Fungsi: Mengonversi bilangan menjadi representasi heksadesimal.  
    - Terdapat di **BAB 15**.

50. datetime.date()  
    - Fungsi: Membuat objek tanggal dari modul `datetime`.  
    - Terdapat di **BAB 17**.

51. eval(expression)  
    - Fungsi: Mengeksekusi ekspresi Python dalam bentuk string.  
    - Terdapat di bagian evaluasi string dalam file Anda.

52. exec(code)  
    - Fungsi: Mengeksekusi pernyataan Python dalam bentuk string.  
    - Terdapat di bagian evaluasi string dalam file Anda.                                                                                                
'''


























































































print("BAB 1")
print("------")

'''                 ====BAB 1  (Variabel)====                           '''                        
'''larangan dalam menulis variable                                     '''                                                                
'''   1. 10data =     (tidak boleh, angka tidak boleh di depan huruf)  '''                                            
'''      data10 =     (boleh)                                          '''                    
'''   2. data 10 =    (tidak boleh ada spasi)                          '''            
'''      data-10 =    (tidak boleh )                                   '''        
'''      data_10 =    (boleh)                                          '''    
'''   3. 1000 = 10    (tidak boleh angka)                              '''                        
'''      a = 10       (boleh)                                          '''                                

a = 10
b = 25 

print ("a" , "b")

print("") # hanya spasi



































































print("BAB 2")
print("------")
'''             ====BAB 2  (Tipe Data)====            '''
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
print("------")
'''             ====BAB 3  (Tipe Data Khusus)====            '''
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















































































print ("BAB 4")
print("------")
'''             ====BAB 4  (Casting atau Mengubah Tipe Data))====            '''
print ("====INTEGER====")

#   1. Mengubah tipe data "integer" ke tipe data lain
a = 10          # data integer      # bentuk bilangan bulat
b = float(a)    # diubah ke float   # bentuk bilangan desimal
c = str (a)     # diubah ke string  # bentuk karakter bukan angka karna string
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====FLOAT====")

#   2. Mengubah tipe data "float" ke tipe data lain
a = 10.9        # data float        # bentuk bilangan desimal       # akan di bulatkan ke bawah meskipun 10.9 menjadi 10 bukan 11 
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = str (a)     # diubah ke string  # bentuk karakter bukan angka karna string
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====STRING====")

#   3. Mengubah tipe data "string" ke tipe data lain
a = 10          # data string       # bentuk karakter bukan angka karna string
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = float (a)   # diubah ke float   # bentuk bilangan desimal
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====BOOLEAN====")

#   4. Mengubah tipe data "boolean" ke tipe data lain
a = True        # data boolean      # hasilnya false jika a = 0, dan true jika a = selain 0 
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = float (a)   # diubah ke float   # bentuk bilangan desimal
d = str (a)     # diubah ke boolean # bentuk karakter bukan angka karna string 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi












































































print ("BAB 5")
print("------")
'''             ====BAB 5  (Input atau Mengambil Tipe Data)====            '''
a = input ("Masukkan data = ")
print ("data = ", a, ", type = ", type (a)) # hasil pasti string

b = int(input ("Masukkan data = "))
print ("data = ", b, ", type = ", type (b)) # data yang dimasukkan harus integer

c = float(input ("Masukkan data = "))
print ("data = ", c, ", type = ", type (c)) # data yang dimasukkan harus float

d = bool(int(input ("Masukkan data = ")))
print ("data = ", d, ", type = ", type (d)) # data yang dimasukkan harus integer jika memasukkan data float maka error

e = bool(float(input ("Masukkan data = ")))
print ("data = ", e, ", type = ", type (e)) # data yang dimasukkan bisa integer bisa float, hasil false jika data yang dimasukkan 0 

print("") # hanya spasi











































































print ("BAB 6")
print("------")
'''             ====BAB 6  (Operasi Aritmatika)====                                  '''
'''Jenis-jenis operasi:                                                             '''                            
'''     1. Operasi penjumlahan (+)                                                  '''                                              
'''     2. Operasi pengurangan (-)                                                  '''                              
'''     3. Operasi perkalian (*)                                                    '''                          
'''     4. Operasi pembagian (/)                                                    '''                                  
'''     5. Operasi eksponen atau pangkat (**)                                       '''                              
'''     6. Operasi modulus atau sisa pembagian (%)                                  '''                                      
'''           cth: -) jika 10 / 2 = 5, maka modulus 0                               '''                                                  
'''                -) jika 5 / 2 = 2.5, maka modulus 1                              '''                                  
'''                   maksudnya begini, 5 / 2 sama dengan 2 * x = 5                 '''                           
'''                   anggap x = 2, maka 2 * 2 = 4, tidak bisa menjadi 5,           '''                          
'''                   jadi dianggap sisa 1 atau modulus 1                           '''
'''                -) jika 10 / 3 , maka modulus = 1                                '''                        
'''                   3 * 2 = 9, sisanya 1 atau modulusnya 1                        '''                    
'''     7. Operasi floor division atau hasil pembagian yang dibulatkan kebawah (//) '''                        
'''           cth: -) 10 / 3 = 3,333333                                             '''                        
'''                   10 // 3 = 3                                                   '''                        
'''                -) 10 / 6 = 1,666666                                             '''                        
'''                   10 // 6 = 1                                                   '''                        
'''                                                                                 '''                                    
'''Prioritas operasi:                                                               '''                            
'''     1. Tanda kurung ()                                                          '''                            
'''     2. Eksponen **                                                              '''                            
'''     3. Perkalian dan teman" (*, /, %, //)                                       '''                            
'''     4. Penjumlahan dan pengurangan (+, -)                                       '''                            
                                                                       
a = 5
b = 2

#1. Operasi penjumlahan
c = a + b
print (a, "+" ,b, "=" ,c)

#2. Operasi pengurangan
c = a - b
print (a, "-" ,b, "=" ,c)

#3. Operasi perkalian
c = a * b
print (a, "*" ,b, "=" ,c)

#4. Operasi pembagian
c = a / b
print (a, "/" ,b, "=" ,c)

#5. Operasi eksponen
c = a ** b
print (a, "**" ,b, "=" ,c)

#6. Operasi modulus
c = a % b
print (a, "%" ,b, "=" ,c)

#7. Operasi floor division
c = a // b
print (a, "//" ,b, "=" ,c)

print ("")

























































print ("BAB 7")
print("------")
'''                                      ====BAB 7  (Pengaplikasian Operasi Aritmatika)====                                      '''
''' Rumus umum                                                                                                   '''                                                                                                                                                                              
'''                                                                                                              '''                                                                                                                                                                   
''' |          |      celcius        |        Reamur       |       Fahrenheit      |          Kelvin           | '''                                                                                                                                                                                                                                                                             
''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                                
''' |celcius   |         -           |(4/5)*celcius        |(9/5)*(celcius+32)     |celcius+273                | '''                                                                                                                                                                                                                                                   
''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                             
''' |Reamur    |(5/4)*reamur         |           -         |(9/4)*(reamur+32)      |(5/4)*(reamur+273)         | '''                                                                                                                                                                                                                                             
''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                               
''' |Fahrenheit|(5/9)*(fahrenheit-32)|(4/9)*(fahrenheit-32)|           -           |(fahrenheit-32)*((5/9)+273)| '''                                                                                                                                                                                                                                                                 
''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                               
''' |Kelvin    |kelvin-273           |(4/5)*(kelvin-273)   |(kelvin-273)*((9/5)+32)|            -              | '''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

#Satuan celcius ke satuan lain 
print ("\n====CELCIUS====")
celcius = float(input("Masukkan suhu dalam Celcius ="))
print ("Suhu dalam Celcius = ", celcius, "celcius")

reamur = (4/5)*celcius
print ("Suhu dalam Reamur = ", reamur, "reamur")

fahrenheit = (9/5)*(celcius+32)
print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")

kelvin = celcius+273
print ("Suhu dalam Kelvin = ", kelvin, "kelvin")





#Satuan reamur ke satuan lain
print ("\n====REAMUR====")
reamur = float(input("Masukkan suhu dalam Reamur ="))

celcius = (5/4)*reamur
print ("Suhu dalam Celcius = ", celcius, "celcius")

print ("Suhu dalam Reamur = ", reamur, "reamur")

fahrenheit = (9/4)*(reamur+32)
print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")

kelvin = (5/4)*(reamur+273)
print ("Suhu dalam Kelvin = ", kelvin, "kelvin")





#Satuan fahrenheit ke satuan lain 
print ("\n====FAHRENHEIT====")
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit ="))

celcius = (5/9)*(fahrenheit-32)
print ("Suhu dalam Celcius = ", celcius, "celcius")

reamur =(4/9)*(fahrenheit-32)
print ("Suhu dalam Reamur = ", reamur, "reamur")

print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")

kelvin = (fahrenheit-32)*((5/9)+273)
print ("Suhu dalam Kelvin = ", kelvin, "kelvin")





#Satuan kelvin ke satuan lain 
print ("\n====CELCIUS====")
kelvin = float(input("Masukkan suhu dalam Kelvin ="))

celcius = kelvin-273
print ("Suhu dalam Celcius = ", celcius, "celcius")

reamur = (4/5)*(kelvin-273)
print ("Suhu dalam Reamur = ", reamur, "reamur")

fahrenheit = (kelvin-273)*((9/5)+32)
print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")

print ("Suhu dalam Kelvin = ", kelvin, "kelvin")

print ("")




















































print ("BAB 8")
print("------")

'''             ====BAB 8  (Operasi Komparasi)====                                                                                   '''
'''                                                                                                                                 '''
'''Operasi komparasi adalah operasi yang dimana hasilnya selalu boolean (True or False)                                             '''
'''                                                                                                                                 '''                         
'''Jenis-jenis operasi komparasi:                                                                                                   '''                             
'''     1. lebih besar dari (>)                                                                                                     '''                                                     
'''         cth: 4 > 2 = True                                                                                                       '''                             
'''              1 > 2 = False                                                                                                      '''                                 
'''              2 > 2 = False                                                                                                      '''                                 
'''     2. kurang dari (<)                                                                                                          '''                         
'''         cth: 4 < 2 = False                                                                                                      '''                                         
'''              1 < 2 = True                                                                                                       '''                                                                                                                                          
'''              2 < 2 = False                                                                                                      '''                                          
'''     3. lebih dari sama dengan (>=)                                                                                              '''                                                 
'''         cth: 4 >= 2 = True                                                                                                      '''                                         
'''              1 >= 2 = False                                                                                                     '''                                           
'''              2 >= 2 = True                                                                                                      '''                                         
'''     4. kurang dari sama dengan (<=)                                                                                             '''                                                  
'''         cth: 4 <= 2 = False                                                                                                     '''                                          
'''              1 <= 2 = True                                                                                                      '''                                         
'''              2 <= 2 = True                                                                                                      '''                                         
'''     5. sama dengan (==)                                                                                                         '''                                      
'''         cth: 4 == 4 = True                                                                                                      '''                                         
'''              4 == 2 = False                                                                                                     '''                                           
'''     6. tidak sama dengan (!=)                                                                                                   '''                                            
'''         cth: 4 != 4 = False                                                                                                     '''                                          
'''              4 != 2 = True                                                                                                      '''                                          
'''     7. is                                                                                                                       '''                    
'''        is hanya membandingkan objek degan objek                                                                                 '''                                    
'''   Objek sendiri adalah sesuatu yang memiliki nilai                                                                              '''                                    
'''   cth:   a = 5, maka a adalah objek yang dimana nilai dari a adalah 5, sedangkan 5 bukan objek tapi "literal" yaitu selain objek'''                                
'''   Maka a is 5 , tidak bisa karna is hanya membandingkan objek dengan objek, bukan objek dengan literal                          '''                                    
'''     8. is not                                                                                                                   '''                                        
'''        is not kebalikan dari is, tapi cara menggunakan nya sama dengan is yaitu membandingkan objek dengan objek                '''                                                        



b = 10
c = 5

print( "==== LEBIH BESAR DARI (>)")
#   1. lebih besar dari (>)
a = b > 8
print (b, ">" ,8, "=" ,a)
a = b > 20
print (b, ">" ,20, "=" ,a)
a = b > 10
print (b, ">" ,10, "=" ,a)

print( "==== KURANG DARI (<)")
#   2. kurang dari (<)
a = b < 8
print (b, "<" ,8, "=" ,a)
a = b < 20
print (b, "<" ,20, "=" ,a)
a = b < 10
print (b, "<" ,10, "=" ,a)

print( "==== LEBIH DARI SAMA DENGAN (>=)")
#   3. lebih dari sama dengan >=
a = b >= 8
print (b, ">=" ,8, "=" ,a)
a = b >= 20
print (b, ">=" ,20, "=" ,a)
a = b >= 10
print (b, ">=" ,10, "=" ,a)

print( "==== KURANG DARI SAMA DENGAN (<=)")
#   4. kurang dari sama dengan <=
a = b <= 8
print (b, "<=" ,8, "=" ,a)
a = b <= 20
print (b, "<=" ,20, "=" ,a)
a = b <= 10
print (b, "<=" ,10, "=" ,a)

print( "==== SAMA DENGAN (==)")
#   5. sama dengan ==
a = b == 20
print (b, "==" ,20, "=" ,a)
a = b == 10
print (b, "==" ,10, "=" ,a)

print( "==== TIDAK SAMA DENGAN (!=)")
#   6. tidak sama dengan !=
a = b != 20
print (b, "!=" ,20, "=" ,a)
a = b != 10
print (b, "!=" ,10, "=" ,a)

print( "==== is (is)")
#   6. is
a = b is c
print (b, "is" ,c, "=" ,a)
a = b is b
print (b, "is" ,b, "=" ,a)

print( "==== is not (is not)")
#   7.  is not
a = b  is not c
print (b, " is not" ,c, "=" ,a)
a = b  is not b
print (b, " is not" ,b, "=" ,a)

print ("")























































print ("BAB 9")
print("------")

'''====BAB 9  (Operasi Logika atau Boolean)===='''


#Jenis-jenis operasi logika                                                                                          
#
#     Operator AND
# True and True    # Hasilnya: True
# False and False  # Hasilnya: False
# True and False   # Hasilnya: False
# False and True   # Hasilnya: False
#
#     Operator OR
# True or True     # Hasilnya: True
# False or False   # Hasilnya: False
# True or False    # Hasilnya: True
# False or True    # Hasilnya: True
#
#     Operator XOR (Exclusive OR)
# True ^ True      # Hasilnya: False
# False ^ False    # Hasilnya: False
# True ^ False     # Hasilnya: True
# False ^ True     # Hasilnya: True
#
#     Operator NOT
# not True         # Hasilnya: False
# not False        # Hasilnya: True
#
#     Operator OR NOT
# True or not True   # Hasilnya: True 
# False or not False # Hasilnya: True 
# True or not False  # Hasilnya: True
# False or not True  # Hasilnya: False 
#
#     Operator AND NOT
# True and not True   # Hasilnya: False
# False and not False # Hasilnya: False 
# True and not False  # Hasilnya: True
# False and not True  # Hasilnya: False




#   NOT 
a = True
b = not a

print ("====NOT====")
print ("data a = ",a)
print ("-----------NOT")
print ("data b = ",b, "\n")

#   OR (jika ada salah satu pilihan yang True maka hasilnya True)

print ("====OR====")
a = False
b = False
c = a or b
print (a, "or" ,b, "=" ,c)
a = False
b = True
c = a or b
print (a, "or" ,b, "=" ,c)
a = True
b = False
c = a or b
print (a, "or" ,b, "=" ,c)
a = True
b = True
c = a or b
print (a, "or" ,b, "=" ,c, "\n")

#   and (jika ada salah satu pilihan yang False maka hasilnya False)

print ("====AND====")
a = False
b = False
c = a and b
print (a, "and" ,b, "=" ,c)
a = False
b = True
c = a and b
print (a, "and" ,b, "=" ,c)
a = True
b = False
c = a and b
print (a, "and" ,b, "=" ,c)
a = True
b = True
c = a and b
print (a, "and" ,b, "=" ,c, "\n")

#   xor (jika pilihannya sama maka hasilnya False, jika pilihannya berbeda maka hasilnya True )

print ("====XOR====")
a = False
b = False
c = a ^ b
print (a, "xor" ,b, "=" ,c)
a = False
b = True
c = a ^ b
print (a, "xor" ,b, "=" ,c)
a = True
b = False
c = a ^ b
print (a, "xor" ,b, "=" ,c)
a = True
b = True
c = a ^ b
print (a, "xor" ,b, "=" ,c)

print ("")




















































print ("BAB 10")
print("------")

'''====BAB 10 (Operasi Logika dan Komparasi)===='''


# ++++++++3------------10+++++++++++
#   True di +
#   False di -

angka1 = float(input ("Syarat: \n 1. Angka kurang dari 3 \n 2. Angka lebih dari 10 \nMasukkkan angka: "))

kurang_dari = (angka1 < 3)
print ("kurang dari 3 = ", kurang_dari)

lebih_dari = (angka1 > 10)
print ("lebih dari 10 = ", lebih_dari)

huruf = kurang_dari or lebih_dari

print ("angka yang anda masukkan =", huruf)

print ("")
#-------3++++++++++10----------
#   True di +
#   False di -

angka2 = float (input ("Syarat: \n 1. Angka lebih dari 3 \n 2. Angka kurang dari 10 \nMasukkkan angka: "))

kurang_dari = angka2 > 3
print ("lebih dari 3 = ", kurang_dari)

lebih_dari = angka2 < 10
print ("kurang dari 10 =", lebih_dari)

huruf2 = kurang_dari and lebih_dari
print ("Angka yang anda masukkan =", huruf2)

















































print ("BAB 11")
print("------")

'''           ====BAB 11 (Bitwise)====                                 
'''
a = 9
b = 5

# Bitwise OR (|)
print ("==============OR==============")
print ("Nilai a =", a, ", binary:", format(a,"08b"))
print ("Nilai b =", b, ", binary:", format(b,"08b"))
print ("------------------------------(|)")
c = a | b
print ("Nilai c =", c, ", binary:", format(c,"08b"))

# Bitwise AND (&)
print ("\n=============AND==============")
print ("Nilai a =", a, ", binary:", format(a,"08b"))
print ("Nilai b =", b, ", binary:", format(b,"08b"))
print ("------------------------------(&)")
c = a & b
print ("Nilai c =", c, ", binary:", format(c,"08b"))

# Bitwise XOR (^)
print ("\n=============XOR==============")
print ("Nilai a =", a, ", binary:", format(a,"08b"))
print ("Nilai b =", b, ", binary:", format(b,"08b"))
print ("------------------------------(^)")
c = a ^ b
print ("Nilai c =", c, ", binary:", format(c,"08b"))

# Bitwise NOT (~)
print ("\n=============NOT==============")
print ("Nilai a =", a, ", binary:", format(a,"08b"))
print ("------------------------------(~)")
c = ~a
print ("Nilai c =", c, ", binary:", format(c,"08b"))
print ("------------------------------(^)") 
d = 0b00001001  #gunakan XOR NOT jika ingin mengflip semua biner 
e = 0b11111111
print ("Nilai e =", e^d, ", binary:", format(e^d,"08b"))

# Shifting (mengeser-geser)
# Shifting right (>>)
print ("\n========Shifting right========")
c = a >> 2
print ("Nilai a =", a, ", binary:", format(a,"08b"))
print ("------------------------------(>>)")
print ("Nilai c =", c, ", binary:", format(c,"08b"))

# Shifting left (<<)
print ("\n========Shifting left========")
c = a << 2
print ("Nilai a =", a, ", binary:", format(a,"08b"))
print ("------------------------------(<<)")
print ("Nilai c =", c, ", binary:", format(c,"08b"))

print ("")





















































print ("BAB 12")
print("------")

'''           ====BAB 12 (Pengenalan String)====                                 
'''

# 1. cara membuat string 

'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
    3. menggunakan single dan double quote secara bersamaan '"..."' atau "'...'"
'''

data = 'menggunakan single quote'
print  (data)

data = "menggunakan double quote"
print  (data)

data = '"menggunakan single dan double quote secara bersamaan"'
print  (data)

data = "'menggunakan single dan double quote secara bersamaan'"
print  (data)

# 2. Penggunakan tanda (\)

# 3. mengubah tanda (') menjadi string 
print ('hari ini adalah hari jum\'at') # ditambah \ sebelum '

# 4. mengubah tanda (\) menjadi string 
print ('https:\\ucup.com') # ditambah \ sebelum \

# 5. tab (\t)
print ('ucup\tdimas')
print ('ucup\t\t\tdimas') # bisa di stuck

# 6. backspace (\b)
print ('ucup \bdimas')

# 7. newline (\n, \r, \r\n) di windows menggunakan \r\n
print ('baris pertama.\r\nbaris kedua.')

# 8. string literal atua raw 
print (r'ucup www.com\t\n\r\n\b') 

''' menggunakan raw jika terdapat banyak \ dan 
    ingin menampilkan banyak \ kedalam terminal 
'''

# 9. multiline ("""...""") maka akan di print semua 
print ("""
    nama = ghois
    prodi = d3 teknik kimia
    jurusan = teknik kimia
    asal = pasuruan
       """)




























































print ("BAB 13")
print("------")

'''           ====BAB 13 (Operasi dan Manupulasi String)====
'''

# 1. menyambung string 

nama_depan = "Bayu"
nama_tengah = "An"
nama_belakang = "organik"

nama_lengkap = nama_depan + " " + nama_tengah + nama_belakang
print ("Nama lengkap = ", nama_lengkap)
print ("------------------------------")




# 2. menghitung panjang string 

panjang = len(nama_lengkap)
print ("Panjang dari", nama_lengkap, "=",panjang)
print ("------------------------------")




# 3. mengecek apakah ada komponen char di dalam string 

y = "y"
status = y in nama_lengkap
print ("string", y , "ada di", nama_lengkap, ":",  status,)

b = "b" 
status = b in nama_lengkap
print ("string", b , "ada di", nama_lengkap, ":",  status)

        # hasil b false karna b yang ada di Bayu Anorganik adalah B besar bukan b kecil

b = "b" 
status = b not in  nama_lengkap
print ("string", b , "tidak ada di", nama_lengkap, ":",  status)

print ("------------------------------")




# 4. mengulang string 

print ("awok"*5)
print (5*"awok")

print ("------------------------------")




# 5. indexing

print ("index ke-0 =", nama_lengkap[0])
print ("index ke-8 =", nama_lengkap[8])
print ("index ke-(-1) =", nama_lengkap[-1]) # jika min maka dihitung dari belakang 
print ("index ke-(-4) =", nama_lengkap[-4])
print ("index ke-(0:4) =", nama_lengkap[0:4])
print ("index ke-(5:9) =", nama_lengkap[5:9])
print ("index ke-(2, 4, 6, 8, 10) =", nama_lengkap[0:10:2])

print ("------------------------------")

# 6. item paling kecil

print ("Item yang nilai paling kecil \ndi", nama_lengkap, "adalah:", min(nama_lengkap))

print ("------------------------------")

# 7. item paling besar

print ("Item yang nilai paling besar \ndi", nama_lengkap, "adalah:", max(nama_lengkap))

print ("------------------------------")

# 8. ASCII CODE 
#
# fungsinya adalah untuk mengubah huruf menjadi angka dan angka menjadi huruf 
# ord = untuk mengubah huruf menjadi angka
# chr = untuk mengubah angka menjadi huruf 
#
kode = ord("K")
print ("Angka dari huruf K adalah:", kode)

kode = 80
print ("Huruf dari angka", kode , "adalah:", chr(kode))

print ("------------------------------")





# 9. operator dalam bentuk metode

data = "fahri daur ulang"
jumlah = data.count("u")
print ("jumlah u dalam", data, "=", jumlah,)

data = "bedeh bedhek \nebebebenh bedenh bedek pedhe"
jumlah = data.count("e")
print ("jumlah e dalam", data, "=", jumlah)
jumlah = data.count("b")
print ("jumlah b dalam", data, "=", jumlah)


































































print ("BAB 14")
print("------")

'''           ====BAB 14 (Operator Dalam Bentuk Metode)====
'''

# 1. merubah semua ke upper case

Salam = "AssaLAmuAlAiKUm"
print ("Normal = " + Salam)
SALAM = Salam.upper()
print ("Besaa = " + SALAM)

print ("------------------------------\n")

# 2. merubah semua ke lower case

Salam = "AssaLAmuAlAiKUm"
print ("Normal = ", Salam)
salam = Salam.lower()
print ("Kicik =", salam)

print ("------------------------------\n")

# 3. pengecekan lower dan upper case dengan is

nama = "arayyy"
apakah_lower = nama.islower()
print (nama, "is lower =", apakah_lower )
apakah_upper = nama.isupper()
print (nama, "is upper =", apakah_upper )

print ("------------------------------\n")

# 4. pengecekan apakah semuanya huruf menggunakan is 

nama = "arayyy"
apakah_huruf = nama.isalpha()
print (nama, "apakah semuanya \nhuruf ? =", apakah_huruf )
nama = "arayyy123"
apakah_huruf = nama.isalpha()
print (nama, "apakah semuanya \nhuruf ? =", apakah_huruf )

print ("------------------------------\n")

# 5. pengecekan apakah huruf dan angka tanpa menggunakan huruf khusus seperti @,#,$,% mengggunakan is 

nama = "(arayyy)"
apakah_huruf_dan_angka = nama.isalnum()
print (nama, "apakah ada huruf \ndan angka ? =", apakah_huruf_dan_angka )
nama = "(arayyy123)"
apakah_huruf_dan_angka = nama.isalnum()
print (nama, "apakah ada huruf \ndan angka ? =", apakah_huruf_dan_angka )
nama = "(arayyy@gmail)"
apakah_huruf_dan_angka = nama.isalnum()
print (nama, "apakah ada huruf \ndan angka ? =", apakah_huruf_dan_angka )
nama = "(arayyy.gmail)"
apakah_huruf_dan_angka = nama.isalnum()
print (nama, "apakah ada huruf \ndan angka ? =", apakah_huruf_dan_angka )

print ("------------------------------\n")

# 6. pengecekan apakah semuanya angka menggunakan is 

nama = "arayyy"
apakah_angka = nama.isdecimal()
print (nama, "apakah semuanya \nangka ? =", apakah_angka )
nama = "123456789"
apakah_angka = nama.isdecimal()
print (nama, "apakah semuanya \nangka ? =", apakah_angka )

print ("------------------------------\n")

# 7. pengecekan apakah yang terlihat kosong ada spasi 

nama = "arayyy"
apakah_spasi = nama.isspace()
print (nama, "apakah semuanya \nspasi ? =", apakah_spasi )
nama = "     "
apakah_spasi = nama.isspace()
print (nama, "apakah semuanya \nspasi ? =", apakah_spasi )

'''
bukan spasi saja yang bisa di cek 
menggunakan isspace tapi :
    1. spasi
    2. tab
    3. newline
'''

print ("------------------------------\n")

#. 8. pengecekan apakah semua kalimat dimulai dengan huruf kapital

nama = "(Arayyy Punya Ku)"
apakah_title = nama.istitle()
print (nama, "apakah semua\nkalimat dimulai dengan \nhuruf kapital ? =", apakah_title )
nama = "(arayyy punya Ku)"
apakah_title = nama.istitle()
print (nama, "apakah semua \nkalimat dimulai dengan \nhuruf kapital ? =", apakah_title )

print ("------------------------------\n")

# 9. pengecekan startswith() 

cek_start = "botol adalah tempat minun yang dapat di isi berbagai macam minuman".startswith("botol")
print ("start (botol) =",cek_start)
cek_start = "botol adalah tempat minun yang dapat di isi berbagai macam minuman".startswith("dapat")
print ("start (dapat) =",cek_start)

print ("------------------------------\n")

# 10. pengecekan endswith()

cek_start = "botol adalah tempat minun yang dapat di isi berbagai macam minuman".startswith("minuman")
print ("end (minuman) =",cek_start)
cek_start = "botol adalah tempat minun yang dapat di isi berbagai macam minuman".startswith("isi")
print ("end (isi) =",cek_start)

print ("------------------------------\n")

# 11. penggabungan komponen join()

misah = ['aku','dan','kamu']
digabung = '>'.join(misah)
print ("gabungannya menjadi \n=", digabung)

misah = ['aku','dan','kamu']
digabung = ' '.join(misah)
print ("gabungannya menjadi \n=", digabung)

misah = ['aku','dan','kamu']
digabung = ','.join(misah)
print ("gabungannya menjadi \n=", digabung)

misah = ['aku','dan','kamu']
digabung = '@'.join(misah)
print ("gabungannya menjadi \n=", digabung)

misah = ['aku','dan','kamu']
digabung = '#'.join(misah)
print ("gabungannya menjadi \n=", digabung)

print ("------------------------------\n")

# 12. pemisahan komponen split()

gabung = "aku sayang kamu" 
print ("pemisahannya menjadi\n =",gabung.split(' '))

gabung = "aku#sayang#kamu" 
print ("pemisahannya menjadi\n =",gabung.split('#'))

gabung = "aku,sayang,kamu" 
print ("pemisahannya menjadi\n =",gabung.split(','))

gabung = "aku@sayang@kamu" 
print ("pemisahannya menjadi\n =",gabung.split('@'))

gabung = "aku=sayang=kamu" 
print ("pemisahannya menjadi\n =",gabung.split('='))

print ("------------------------------\n")

# 13. alokasi karakter rjust()

'''
jadi rjust() itu akan membuat kalimat nya rata kanan
maksud jadi angka 10 itu adalah karakternya akan ada 10 
jika "kanan" saja sudah berisi 5 huruf 
maka sisanya akan di isi oleh spasi
'''

kanan = "kanan".rjust(10)
print ("|",kanan,"|")

kanan = "kanan".rjust(25)
print ("|",kanan,"|")

kanan = "kanan".rjust(25,".")
print ("|",kanan,"|")

print ("------------------------------\n")

# 13. alokasi karakter ljust()

kiri = "kiri".ljust(10)
print ("|",kiri,"|")

kiri = "kiri".ljust(25)
print ("|",kiri,"|")

kiri = "kiri".ljust(25,".")
print ("|",kiri,"|")

print ("------------------------------\n")

# 14. alokasi karakter center()

tengah = "tengah".center(10)
print ("|",tengah,"|")

tengah = "tengah".center(25)
print ("|",tengah,"|")

tengah = "tengah".center(25,".")
print ("|",tengah,"|")

print ("------------------------------\n")

# 15. penggunaan strip()

'''
strip() berfungsi untuk menghapus seperti contoh 
    :::::::OKEY:::::::
           OKEY
strip akan menghilangkan si ( : )
'''

tengah = "tengah".strip(".")
print ("|",tengah,"|")

























































print ("BAB 15")
print("------")

'''           ====BAB 15 (Format String)====
''' 

# 1. string

nama = "ghois"
format_str = f"Nama = {nama}"
print (format_str)

print ("------------------------------\n")

# 2. angka

angka = 150.567898765
format_str = f"Angka = {angka}"
print (format_str)

print ("------------------------------\n")

# 3. boolean

boolean = True
format_str = f"Boolean = {boolean}"
print (format_str)

print ("------------------------------\n")

# 4. bilangan bulat 

angka = 150
format_str = f"Angka = {angka}"
print (format_str)

print ("------------------------------\n")

# 5. bilangan ribuan keatas (untuk memberikan koma pada bilangan ribuan ke atas)

angka = 1500000
format_str = f"Angka = {angka}"
print (format_str)

angka = 1500000
format_str = f"Angka = {angka:,}"
print (format_str)

angka = 1500000000000000
format_str = f"Angka = {angka:,}"
print (format_str)

print ("------------------------------\n")

# 6. bilangan desimal (untuk menunjukkkan berapa angka di belakang koma)

angka = 150.567898765
format_str = f"Angka = {angka:.2f}"
print (format_str)

angka = 150.567898765
format_str = f"Angka = {angka:.3f}"
print (format_str)

angka = 150.567898765
format_str = f"Angka = {angka:.6f}"
print (format_str)

print ("------------------------------\n")

# 7. menampilkan leading zero

'''
- maksud format ini {angka:10.3f} adalah:

10 = jumlah karakter 
3 = jumlah angka di belakang desimal 
f = format

- maksud format ini {angka:010.3f} adalah:

0 = karakter yang kosong di ganti dengan 0
10 = jumlah karakter 
3 = jumlah angka di belakang desimal 
f = format
'''

angka = 150.56789
format_str = f"Angka = |{angka:10.3f}|"
print (format_str)

angka = 150.56789
format_str = f"Angka = |{angka:20.3f}|"
print (format_str)

angka = 150.56789
format_str = f"Angka = |{angka:010.3f}|"
print (format_str)

angka = 150.56789
format_str = f"Angka = |{angka:020.3f}|"
print (format_str)

print ("------------------------------\n")

# 8. menampilkan angka plus dan minus 

angka_minus = -10.12345
angka_plus = 10.12345
format_minus = f"minus = {angka_minus:+.2f}"
format_plus = f"plus = {angka_plus:+.5f}"
print (format_minus)
print (format_plus)

print ("------------------------------\n")

# 9. memformat persen 

presentase = 0.025
format_persen = f"persen = {presentase:%}"
print (format_persen)

presentase = 0.025
format_persen = f"persen = {presentase:.2%}"
print (format_persen)

presentase = 0.025
format_persen = f"persen = {presentase:.4%}"
print (format_persen)

print ("------------------------------\n")

# 10. melakukan operasi aritmatika di dalam placeholder 

harga = 5000
jumlah = 10

format_harga = f"Harga pesanan = Rp{harga:,},00"
format_jumlah = f"Jumlah pesanan = {jumlah} pesanan\n"
format_harga_total = f"Harga total = Rp{harga*jumlah:,},00"
print (format_harga)
print (format_jumlah)
print (format_harga_total)

print ("------------------------------\n")

# 11. format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"
print (format_binary)
print (format_octal)
print (format_hexadecimal)

print ("------------------------------\n")

























































print ("BAB 16")
print("------")

'''           ====BAB 16 (String Width and Multiline)====
''' 

# 1. data

data_nama = 'ghois ahmad'
data_umur = 19
data_berat_badan = 65.567
data_tinggi_badan = 165

# 2. string standart 

print (5*'=', "DATA STRING", '='*5)

data_string = f"Nama = {data_nama} Umur = {data_umur} Berat badan = {data_berat_badan} Tinggi badan = {data_tinggi_badan}"
print (data_string)
print ('\n')

# 3. string multiline 

print (5*'=', "DATA STRING", '='*5)

data_string = f"Nama = {data_nama} \nUmur = {data_umur} \nBerat badan = {data_berat_badan} \nTinggi badan = {data_tinggi_badan}"
print (data_string)

# 4. string triple multiline

print (5*'=', "DATA STRING", '='*5)

data_string = f"""
Nama = {data_nama} 
Umur = {data_umur} 
Berat badan = {data_berat_badan} 
Tinggi badan = {data_tinggi_badan}
"""
print (data_string)

# 5. mengatur lebar  

print (5*'=', "DATA STRING", '='*5)

data_string = f"""
Nama         = {data_nama:>11} 
Umur         = {data_umur:>11} 
Berat badan  = {data_berat_badan:>11} 
Tinggi badan = {data_tinggi_badan:>11}
"""
print (data_string)

data_string = f"""
Nama         = {data_nama:>15} 
Umur         = {data_umur:>15} 
Berat badan  = {data_berat_badan:>15} 
Tinggi badan = {data_tinggi_badan:>15}
"""
print (data_string)

data_string = f"""
Nama         = {data_nama:>8} 
Umur         = {data_umur:>8} 
Berat badan  = {data_berat_badan:>8} 
Tinggi badan = {data_tinggi_badan:>8}
"""
print (data_string)

data_string = f"""
Nama         = {data_nama:<11} 
Umur         = {data_umur:<11} 
Berat badan  = {data_berat_badan:<11} 
Tinggi badan = {data_tinggi_badan:<11}
"""
print (data_string)
























































print ("BAB 17")
print("------")

'''           ====BAB 17 (Date and Time)====
''' 

# tanggal, bulan, tahun, dan hari ini 

import datetime as dt

hari_ini = dt.date.today()
print (f"sekarang tanggal\n: {hari_ini}, Hari: {hari_ini:%A}")

print ("------------------------------\n")

# tanggal, bulan, tahun yang di inputkan

tanggal = dt.date(2004,6,24)
print (f"Ulang tahun saya adalah\n: {tanggal}, Hari: {tanggal:%A}")

print ("------------------------------\n")

# tanggal,  bulan, tahun lahir saya

print (f"Harap masukkan tannggal, bulan, \ndan tahun lahir anda")
tanggal = int(input("Tanggal \t= "))
bulan = int(input("Bulan \t\t= "))
tahun = int(input("Tahun \t\t= "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print (f"Tanggal lahir anda \nadalah\t: {tanggal_lahir}\nDi hari : {tanggal_lahir:%A}")

# menghitung umur 

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari / 365
umur = umur_tahun.days
print (f"Anda sekarang berusia \n\t: {umur} tahun")
































































print ("BAB 18")
print("------")

'''           ====BAB 18 (if and else statement)====
''' 

nama = input('Siapa kau ??? : ')

if nama == "gois":
    print('hai gois kamu ganteng banget sihhhhh')
else:
    if nama == "gok":
        print('RAWRRRRRRRRRRRRR')
    else:
        print('kamu bukan gois ah ga asik')
print('terima kasih')




























































print ("BAB 19")
print("------")

'''           ====BAB 19 (elif = else if statement)====
''' 

nama = input ("Siapa nama mu = ")

if nama == "gois":
    print ("hai gantengggggggggg")
elif nama == 'aray':
    print ("hai cantikkkkkkkkkk")
elif nama == 'dapin':
    print ("hai dapinnnnnnnnnn")
elif nama == 'ima':
    print ("hai imaaaaaaaaaaaaa")
elif nama == 'alysia':
    print ("hai alysiaaaaaaaaaaaa")
elif nama == 'maul':
    print ("hai maullllllllll")
elif nama == 'imel':
    print ("hai imelllllllllllll")
elif nama == 'firgi':
    print ("hai firgiiiiiiiiiiiiiiii")
else:
    print ("kamuu siapa???")
print ("terima kasih")






























































print ("BAB 20")
print("------")

'''           ====BAB 20 (Membuat Kalkulator Sederhana)====
''' 

print (20*'=')
print('KALKULATOR SEDERHANA')
print (20*'=','\n')

angka_1 = float(input('Masukkan angka 1: '))
angka_2 = float(input('Masukkan angka 2: '))
operator = input('''Pilihan operator:
    1. penjumlahan (+)
    2. pengurangan (-)
    3. perkalian (*)
    4. pembagian (/)
note: Harap masukkan operator
    sesuai dengan yang ada 
    di dalam kurung
Masukkan operator: ''')

if operator == '+':
    hasil = angka_1 + angka_2
    print(f"\n----------------------\nHasilnya adalah = {hasil}")
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f"\n----------------------\nHasilnya adalah = {hasil}")
elif operator == '*':
    hasil = angka_1 * angka_2
    print(f"\n----------------------\nHasilnya adalah = {hasil}")
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f"\n----------------------\nHasilnya adalah = {hasil}")
else:
    print ('\nMasukkan operator yang bener bos,baca note nya terlebih dahulu!!!')
print('----------------------\n\nTERIMA KASIH BOLO...')

























































print ("BAB 21")
print("------")

'''           ====BAB 21 (for loop (perulangan))====
''' 

# ini dengan list

print (7*'=', 'Dengan List', '='*7)

angka_list = [1,2,3,4,5]
print (angka_list, '\n')

for i in angka_list:
    print (f'i sekarang bernilai = {i}')

print ('------------------------')

angka_list = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
print (angka_list, '\n')

for i in angka_list:
    print (f'i sekarang bernilai = {i}')

print (10*'=', 'Ending', '='*10, '\n\n\n')





# ini dengan range

print (7*'=', 'Dengan Range', '='*7)

angka_range = range(5)
print (angka_range, '\n')

for i in angka_range:
    print (f'i sekarang bernilai = {i}')

print ('------------------------')

angka_range = range(10)
print (angka_range, '\n')

for i in angka_range:
    print (f'i sekarang bernilai = {i}')

print ('------------------------')

angka_range = range(1,5)
print (angka_range, '\n')

for i in angka_range:
    print (f'i sekarang bernilai = {i}')

print ('------------------------')

angka_range = range(5,10)
print (angka_range, '\n')

for i in angka_range:
    print (f'i sekarang bernilai = {i}')

print (10*'=', 'Ending', '='*10, '\n\n\n')




# ini dengan data string

print (4*'=', 'Dengan Data String', '='*4)

data_string = 'anjay kamu bohong'

for huruf in data_string:
    print (huruf)

print (10*'=', 'Ending', '='*10, '\n\n\n')































































print ("BAB 22")
print("------")

'''           ====BAB 22 (WHILE LOOP)====
''' 

angka = 0
print (f'angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print (f"angka sekarang ---> {angka}")
    print (f"aduhhhhh ghoissss")
print (10*'=', 'Ending', '='*10, '\n\n\n')

angka = 0
print (f'angka sekarang -> {angka}')

while angka < 10:
    angka += 1
    print (f"angka sekarang ---> {angka}")
    print (f"aduhhhhh ghoissss")
print (10*'=', 'Ending', '='*10, '\n\n\n')

angka = 10
print (f'angka sekarang -> {angka}')

while angka < 1:
    angka += 1
    print (f"angka sekarang ---> {angka}")
    print (f"aduhhhhh ghoissss")
print (10*'=', 'Ending', '='*10, '\n\n\n')

angka = 10
print (f'angka sekarang -> {angka}')

while angka < 12:
    angka += 1
    print (f"angka sekarang ---> {angka}")
    print (f"aduhhhhh ghoissss")
print (10*'=', 'Ending', '='*10, '\n\n\n')



















































print ("BAB 23")
print("------")

'''           ====BAB 23 (continue and pass)====
''' 
'''
                        ====CONTINUE====
'''

print (10*("="),("PERCOBAAN 1"),("=")*10)

angka = 0
print (f'angka sekarang ---> {angka}')

while angka < 5:
    angka += 1
    print (f'---------------------\nangka sekarang ---> {angka}')

    if angka== 3:
        print ('ini tiga')

    print ('kuyyy...\n')
print (10*'=', 'Ending', '='*10, '\n\n\n')



print (10*("="),("PERCOBAAN 2"),("=")*10)

angka = 0
print (f'angka sekarang ---> {angka}')

while angka < 5:
    angka += 1
    print (f'---------------------\nangka sekarang ---> {angka}')

    if angka== 3:
        print ('ini tiga')
        continue # kuyyy... nya tidak akan ditulis atau di skip

    print ('kuyyy...\n')
print (10*'=', 'Ending', '='*10, '\n\n\n')





'''
                        ====PASS====
'''

print (10*("="),("PERCOBAAN 3"),("=")*10)

angka = 0
print (f'angka sekarang ---> {angka}')

while angka < 5:
    angka += 1
    print (f'---------------------\nangka sekarang ---> {angka}')

    if angka== 3:
        pass # if nya tidak akandi eksekusi karna ada pass

    print ('kuyyy...')
print (10*'=', 'Ending', '='*10, '\n\n\n')






















































print ("BAB 24")
print("------")

'''           ====BAB 24 (break)====
''' 

angka = 0
print (f'angka sekarang ---> {angka}')

while angka < 10:
    angka += 1
    print (f'---------------------\nangka sekarang ---> {angka}')
    print ('kuyyy...')

    if angka== 5:
        break

print (10*'=', 'Ending', '='*10, '\n\n\n')



















































print ("BAB 25")
print("------")

'''           ====BAB 25 (Latihan loop (for and while))====
''' 

sisi = 5

# 1. menggunakan for loop

print (5*("="),("MENGGUNAKAN FOR LOOP"),("=")*5)

biasa = 1
for i in range(sisi):
    print ('*'*biasa)
    biasa += 1

print (10*'=', 'Ending', '='*10, '\n\n\n')





# 2. menggunakan while loop

print (4*("="),("MENGGUNAKAN WHILE LOOP"),("=")*4)

biasa = 1
while True:
    print ('*'*biasa)
    biasa += 1

    if biasa > sisi:
        break

print (10*'=', 'Ending', '='*10, '\n\n\n')






















































print ("BAB 26")
print("------")

'''           ====BAB 26 (Latihan Membuat Bangun Datar Menggunakan loop)====
''' 

# 1. membuat segitiga sama sisi

print (5*("="),("SEGITIGA SAMA SISI"),("=")*5)

tinggi = 5

for i in range(1, tinggi + 1):
    spasi = " " * (tinggi - i)  # Spasi di kiri dan kanan
    bintang = "*" * (2 * i -1)  # Bintang di tengah
    print(spasi, bintang, spasi)  # Spasi di kiri dan kanan

print (10*'=', 'Ending', '='*10, '')

tinggi = 5

for i in range(1, tinggi + 1):
    spasi = "0" * (tinggi - i)  # Spasi di kiri dan kanan
    bintang = "*" * (2 * i -1)  # Bintang di tengah
    print(spasi, bintang, spasi)  # Spasi di kiri dan kanan

print (10*'=', 'Ending', '='*10, '\n\n\n')







# 2. membuat persegi 

print (10*("="),("PERSEGI"),("=")*10)

sisi = 5

for i in range(sisi):  # Mengulang sebanyak 'sisi'
    print("* " * sisi)  # Cetak bintang sebanyak 'sisi' di setiap baris

print (10*'=', 'Ending', '='*10)

sisi = 8

for i in range(sisi):  # Mengulang sebanyak 'sisi'
    print("* " * sisi)  # Cetak bintang sebanyak 'sisi' di setiap baris

print (10*'=', 'Ending', '='*10, '\n\n\n')








# 3. membuat persegi panjang

print (7*("="),("PERSEGI PANJANG"),("=")*7)

panjang = 7  # Panjang ke samping
tinggi = 3   # Tinggi tetap satu baris

# Membuat persegi panjang horizontal
for i in range(tinggi):
    print("* " * panjang)


print (10*'=', 'Ending', '='*10)

panjang = 3  # Panjang ke samping
tinggi = 7   # Tinggi tetap satu baris

# Membuat persegi panjang horizontal
for i in range(tinggi):
    print("* " * panjang)

print (10*'=', 'Ending', '='*10, '\n\n\n')








# 4. membuat belah ketupat

print (7*("="),("BELAH KETUPAT"),("=")*7)

'''
rumus belah ketupat sama saja dengan rumus segitiga sama sisi 
cuma ada beberapa penyesuaian, di antaranya:
    1.  rumus segitiga 

        for i in range(1, tinggi + 1):
    
        rumus belah ketupat 

        for i in range(1, setengah + 2):
        
    perbedaan +1 dan +2 pada rumus tersebut adalah karna di belah ketupat 
    nanti banyak barisnya akan di tambah 1, jadi tidak akan sesuai dengan 
    data yang di input.

    2.  rumus segitiga terbalik sama saja cuma berbeda di:
            bagian atas:

            for i in range(1, setengah + 2):
            
            bagian bawah:

            for i in range(setengah, 0, -1):

        wajib menggunakan  0,-1 karna itu dari setengah(anggap 6), dari 6 
        kemudian 0 kemudian -1
'''

# Tinggi belah ketupat (harus ganjil)
tinggi = 13
setengah = tinggi // 2

# Bagian atas belah ketupat
for i in range(1, setengah + 2):
    spasi = " " * (setengah + 1 - i)
    bintang = "*" * (2 * i - 1)
    print(spasi + bintang)

# Bagian bawah belah ketupat
for i in range(setengah, 0, -1):
    spasi = " " * (setengah + 1 - i)
    bintang = "*" * (2 * i - 1)
    print(spasi + bintang)

print (10*'=', 'Ending', '='*10, '')

tinggi = 13
setengah = tinggi // 2

# Bagian atas belah ketupat
for i in range(1, setengah + 2):
    spasi = "0" * (setengah + 1 - i)
    bintang = "*" * (2 * i - 1)
    print(spasi + bintang)

# Bagian bawah belah ketupat
for i in range(setengah, 0, -1):
    spasi = "0" * (setengah + 1 - i)
    bintang = "*" * (2 * i - 1)
    print(spasi + bintang)

print (10*'=', 'Ending', '='*10, '\n\n\n')








# 5. membuat jajar genjang 

print (8*("="),("JAJAR GENJANG"),("=")*8)

# Ukuran jajar genjang
lebar = 5
tinggi = 4

# Membuat jajar genjang
for i in range(tinggi):
    spasi = " " * (tinggi - i - 1)  # Tambahkan spasi di awal
    bintang = "*" * lebar
    print(spasi + bintang)

print (10*'=', 'Ending', '='*10, '')

# Ukuran jajar genjang
lebar = 5
tinggi = 4

# Membuat jajar genjang
for i in range(tinggi):
    spasi = "0" * (tinggi - i - 1)  # Tambahkan spasi di awal
    bintang = "*" * lebar
    print(spasi + bintang)

print (10*'=', 'Ending', '='*10, '\n\n\n')
















































































print ("BAB 27")
print("------")

'''           ====BAB 27 (list)====
''' 

# 1. kumpulan data numbers

data_angka = [1,2,3,4,5]
print (f"{data_angka}")

print (10*'=', 'Ending', '='*10, '\n')

# 2. kumpulan data string

data_string = ["gois","aray","dapin","ima","alysia"]
print (f"{data_string}")

print (10*'=', 'Ending', '='*10, '\n')

# 3. kumpulan data boolean 

data_boolean = [True, False, True, False]
print (f"{data_boolean}")

print (10*'=', 'Ending', '='*10, '\n')

# 4. kumpulan data campuran 

data_campuran = [1, 'gois', 'aray', 3, 7, True, 5, 'dapin', False]
print (f"{data_campuran}")

print (10*'=', 'Ending', '='*10, '\n')

# 5. alternatif membuat list 

data_range = range(0,10,2) # (start, stop, step)
data_list = list(data_range)
print (f"{data_list}")

print (10*'=', 'Ending', '='*10, '\n')

# 6. membuat list dengan for loop

list_for = [i for i in range(0, 6)]
print (f"{list_for}")
        # versi pangkat
list_for = [i**2 for i in range(0, 6)]
print (f"{list_for}")
list_for = [i**3 for i in range(0, 6)]
print (f"{list_for}")
list_for = [i**10 for i in range(0, 6)]
print (f"{list_for}")

print (10*'=', 'Ending', '='*10, '\n')

# 7. membuat list pake for dan if

list_for = [i for i in range(0, 6) if i != 5] # akan menghilangkan angka 5
print (f"{list_for}")
list_for = [i for i in range(0, 6) if i != 2] # akan menghilangkan angka 2
print (f"{list_for}")
list_for = [i for i in range(0, 6) if i != 1] # akan menghilangkan angka 1
print (f"{list_for}")
list_for = [i for i in range(0, 6) if i%2 == 0] # hanya genap yang di print
print (f"{list_for}")
list_for = [i for i in range(0, 6) if i%2 != 0] # hanya ganjil yang di print
print (f"{list_for}")

print (10*'=', 'Ending', '='*10, '\n')

























































































print ("BAB 28")
print("------")

'''           ====BAB 28 (manipulasi list)====
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















































































print ("BAB 29")
print("------")

'''           ====BAB 29 (Operasi list)====
''' 

data_angka = [1,2,1,3,2,1,4,5,3,7,5,4,6,3,3,2,3,2,2,]
data_nama = ['gois','aray', 'ima', 'dapin', 'alysia']

print (10*("="),("DATA AWAL"),("=")*10)
print(f"{data_angka}\n{data_nama} ")
print (10*'=', 'Ending', '='*10, '\n\n\n')

# 1. mencari banyaknya data

print (10*("="),("JUMLAH DATA"),("=")*10)

jumlah_data_angka = data_angka.count(3) # banyaknya data (3)
jumlah_data_nama = data_nama.count('gois') # banyaknya data (gois)

print(f"Data angka (3) berjumlah = {jumlah_data_angka}")
print(f"Data nama (gois) berjumlah = {jumlah_data_nama}")

print (10*'=', 'Ending', '='*10, '\n\n\n')

# 2. mengambil posisi data (index)

print (5*("="),("MENGAMBIL POSISI(INDEX) DATA"),("=")*5)

index_aray = data_nama.index('aray')
print(f'index si aray = {index_aray}')
index_gois = data_nama.index('gois')
print(f'index si gois = {index_gois}')
index_alysia = data_nama.index('alysia')
print(f'index si alysia = {index_alysia}')

print (10*'=', 'Ending', '='*10, '\n\n\n')

# 3. mengurutkan list 

print (5*("="),("MENGURUTKAN POSISI DATA"),("=")*5)

print(f'Data sebelum di urutkan: \n{data_angka}')
print(f'{data_nama}\n')

data_angka.sort()
data_nama.sort()

print(f'Data setelah di urutkan: \n{data_angka}')
print(f'{data_nama}')

print (10*'=', 'Ending', '='*10, '\n\n\n')

# 4. membalik urutan list

print (5*("="),("MEMBALIK POSISI DATA"),("=")*5)

print(f'Data sebelum di balik: \n{data_angka}')
print(f'{data_nama}\n')

data_angka.reverse()
data_nama.reverse()

print(f'Data setelah di balik: \n{data_angka}')
print(f'{data_nama}\n')

print (10*'=', 'Ending', '='*10, '\n\n\n')












































































print ("BAB 30")
print("------")

'''           ====BAB 30 (Cara Menduplikat list)====
''' 

'''
ketika kita menduplikat list dengan cara seperti di atas,
maka kita akan menduplikat list beserta addres nya juga.

Dampaknya negatif nya ketika kita menduplikat sebuah list 
beserta addres nya maka, ketika kita ingin mengubah list a, 
list b akan ikut berubah mengikuti perubahan list a.

Sebaliknya jika kita menduplikat list dengan addres yang berbeda
atau tidak ikut di duplikat. Maka ketika kita ingin mengubah list a, 
list b akan stay tidak ikut berubah
'''

# 1. cara duplikat yang salah karna addres nya ikut ke duplikat 

print(14*('='), ('LIST A'), ('=')*14,"")

a = ['ghois', 'aray', 'dapin', 'ima']
print(f"list a  --------\n= {a}")

b = a
print(f"list b --------\n= {b}")

print('\n',10*('='), ('ADDRES LIST A'), ('=')*10,)

print("Addres a = ",hex(id(a)))
print("Addres b = ",hex(id(b)))

print(14*('='), ('Ending'), ('=')*14,"\n\n\n")






# 2. cara duplikat yang benar agar addres tidak ikut di duplikat

print(14*('='), ('LIST B'), ('=')*14,"")

a = ['ghois', 'aray', 'dapin', 'ima']
print(f"list a  --------\n= {a}")

b = a.copy()
print(f"list b --------\n= {b}")

print('\n',10*('='), ('ADDRES LIST B'), ('=')*10,)

print("Addres a = ",hex(id(a)))
print("Addres b = ",hex(id(b)))

print(14*('='), ('Ending'), ('=')*14)








































































print ("BAB 31")
print("------")

'''           ====BAB 31 (Membuat list di Dalam list)====
''' 

# list biasa

print(10*('='), ('LIST BIASA'), ('=')*10,"")

list_biasa = [1,2,3,4]
print (f"list biasa = {list_biasa}")

print(14*('='), ('Ending'), ('=')*14,"\n\n")




# list gabungan

print(10*('='), ('LIST GABUNGAN'), ('=')*10,"")

list_1 = [1,2]
list_2 = [3,4]
list_gabungan = [list_1, list_2]

print(f"List 1 = {list_1}")
print(f"List 2 = {list_2}")
print(f"List gabungan = {list_gabungan}")

print(14*('='), ('Ending'), ('=')*14,"\n\n\n")






# contoh penggunaan list gabungan

print(10*('='), ('LIST GABUNGAN'), ('=')*10,"")

list_1 = ['ghois', 19, 'pasuruan']
list_2 = ['aray', 21, 'pasuruan']
list_3 = ['alysia', 20, 'pasuruan']
list_gabungan = [list_1, list_2, list_3]

print(f"list 1 = {list_1}")
print(f"list 2 = {list_2}")
print(f"list 3 = {list_3}")
print(f"list gabungan = {list_gabungan}")

print(14*('='), ('Ending'), ('=')*14,"\n\n\n")














































































print ("BAB 32")
print("------")

'''           ====BAB 32 (Menduplikat list Menggunakan depp copy)  ====
''' 

# menggunakan copy biasa 

'''
ketika menggunakan copy biasa kita hanya mengcopy bagian 
luarnya saja.
    cth :
    list 1 = [1,2]
    list 2 = [3,4]
    list gabungan 1 = [[1,2],[3,4]]

    list 3 = [6,7]
    list 4 = [8,9]
    liat gabungan 2 = [[6,7],[8,9]]

copy biasa hanya mengcopy list gabungan saja, jadi Addres 
list 1 dan 2 , 3 dan 4 tidak berubah tetap sama. Jadi ketika 
dibandingkan antara list gabungan 1 dan list gabungan 2 maka 
Addres nya berbeda, tapi ketika di bandingkan antara list 1 dan 2, 
list 3 dan 4 maka sama. 
'''

print(10*('='), ('MENGGUNAKAN COPY BIASA'), ('=')*10,"")

a = ['ghois', 'aray']
print(f"list a  --------\n= {a}")

b = ['dapin', 'ima']
print(f"list b --------\n= {b}")

c = ['alysia']
print(f"list c --------\n= {c}\n")

list_gabungan_1 = [a, b, c]
print(f"list gabungan 1--------> list a,b,c\n= {list_gabungan_1}")

list_gabungan_2 = list_gabungan_1.copy()
print(f"list gabungan 2--------> hasil gabungan list 1\n= {list_gabungan_2}")

print('\n',10*('='), ('ADDRES LIST COPY'), ('=')*10,)

print("Addres list gabungan 1 = ",hex(id(list_gabungan_1)))
print("Addres list gabungan 2 = ",hex(id(list_gabungan_2)), '\n')

print("Addres list a = ",hex(id(list_gabungan_1[0]))) 
print("Addres list d = ",hex(id(list_gabungan_2[0])),'\n') # list d,e,f adalah list dari list gabungan 2

print("Addres list b = ",hex(id(list_gabungan_1[1]))) 
print("Addres list f = ",hex(id(list_gabungan_2[1])),'\n') # list d,e,f adalah list dari list gabungan 2

print("Addres list d = ",hex(id(list_gabungan_2[2]))) # list d,e,f adalah list dari list gabungan 2
print("Addres list a = ",hex(id(list_gabungan_1[2])),'\n') 

print((''),14*('='), ('Ending'), ('=')*14,"\n\n\n")









# menggunakan deepcopy

from copy import deepcopy

print(10*('='), ('MENGGUNAKAN DEEP COPY'), ('=')*10,"")

a = ['ghois', 'aray']
print(f"list a  --------\n= {a}")

b = ['dapin', 'ima']
print(f"list b --------\n= {b}")

c = ['alysia']
print(f"list c --------\n= {c}\n")

list_gabungan_1 = [a, b, c]
print(f"list gabungan 1--------> list a,b,c\n= {list_gabungan_1}")

list_gabungan_2 = deepcopy(list_gabungan_1)
print(f"list gabungan 2--------> hasil gabungan list 1\n= {list_gabungan_2}")

print('\n',10*('='), ('ADDRES LIST COPY'), ('=')*10,)

print("Addres list gabungan 1 = ",hex(id(list_gabungan_1)))
print("Addres list gabungan 2 = ",hex(id(list_gabungan_2)), '\n')

print("Addres list a = ",hex(id(list_gabungan_1[0]))) 
print("Addres list d = ",hex(id(list_gabungan_2[0])),'\n') # list d,e,f adalah list dari list gabungan 2

print("Addres list b = ",hex(id(list_gabungan_1[1]))) 
print("Addres list f = ",hex(id(list_gabungan_2[1])),'\n') # list d,e,f adalah list dari list gabungan 2

print("Addres list d = ",hex(id(list_gabungan_2[2]))) # list d,e,f adalah list dari list gabungan 2
print("Addres list a = ",hex(id(list_gabungan_1[2])),'\n') 

print((''),14*('='), ('Ending'), ('=')*14,"\n\n\n")












































































print ("BAB 33")
print("------")

'''           ====BAB 33 (looping dari list)====
''' 

# 1. for loop 

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")



kumpulan_angka = [2,10,4,5,9]

for angka in kumpulan_angka:
    print (f'Data angka = {angka}')



print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")






# 2. for loop and range

print(10*('='), ('FOR LOOP AND RANGE'), ('=')*10,"")



kumpulan_angka = [2,10,4,5,9]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print (f'Data angka = {kumpulan_angka[i]}')



print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# 3. while loop

print(10*('='), ('WHILE LOOP'), ('=')*10,"")



kumpulan_angka = [2,10,4,5,9]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print (f'Data angka = {kumpulan_angka[i]}')
    i += 1



print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")








# 4. list comprehension

print(10*('='), ('LIST COMPREHENSION'), ('=')*10,"")



kumpulan_angka = [2,10,4,5,9]

[print(f'Data angka = {i}') for i in kumpulan_angka ]



print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# 5. enumerate

print(10*('='), ('ENUMERATE'), ('=')*10,"")



kumpulan_angka = [2,10,4,5,9]

for index,data in enumerate(kumpulan_angka):
    print (f'Data angka {data},\t Index = {index}')



print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")








# 5. mengkuadratkan list menggunakan for loop 

print(10*('='), ('LIST KUADRAT MENGGUNAKAN FOR LOOP'), ('=')*10,"")



kumpulan_angka = [2,10,4,5,9]

kumpulan_angka_kuadrat = [i**2 for i in kumpulan_angka]

print (f'Data angka asli \t\t= {kumpulan_angka}')
print (f'Data angka yang di kuadratkan \t= {kumpulan_angka_kuadrat}')



print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")




















































































print ("BAB 34")
print("------")

'''           ====BAB 34 (Latihan list Sederhana)====
''' 

list_buku = []
while True : 
    print(("\n\n\n"),10*('-'), ('MASUKKAN DATA MATKUL SEMESTER 1'), 10*('-'), ("\n"))
    nama_matkul = input(f"Nama matkul \t\t= ")
    Nama_dosen = input(f"Nama dosen pengajar\t= ")
    print("\n")

    buku_baru = [nama_matkul, Nama_dosen]
    list_buku.append(buku_baru)

    print(10*('='), ("DATA MATKUL SEMESTER 1"), 10*('='))
    for index, buku in enumerate(list_buku):
        print (f"{index+1} | {buku[0]} | {buku[1]}")

    print(("\n\n"),30*('-'))   
    el_lanjut = input (f"Apakah anda mau melanjutkan? \n( ketik n untuk selesai/ klik enter untuk lanjut )\nMasukkan jawaban anda: ")
    print(30*('-'))   

    if el_lanjut == "n":
        break
        
print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")




























































































print ("BAB 35")
print("------")

'''           ====BAB 35 (tuples dan sets)====
''' 

# list []

a = [1,2,3,4,5]
print (a)

# tuples ()

'''
        tuples adalah semacam list cuma tidak bisa diganti atau semua fungsi yang 
        ada di list tidak bisa digunakan di dalam tuples
'''

a = (1,2,3,4,5)
print (a)

# sets {}

'''
        sets cukup mirip dengan list, bedanya sets tidak bisa digunakan 
        untuk mencari index 
'''
a = {1,2,3,4,5}
print (a)


print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")





















































































print ("BAB 36")
print("------")

'''           ====BAB 36 (dictionary (dict))====
''' 

# ============================= perbedaan dictionary dengan list =============================

'''
    Perbedaan list dan dictionary adalah pada saat memanggil input nya, 
list menggunakan index, sedangkan dictionary menggunakan key atau kunci.

    'gs' : 'ghois'
ketika ingin memanggil ghois menggunakan key nya yaitu gs

    dictionary bisa diisi semua seperti int, float, bool, string, list, bahkan 
dictionary itu sendiri

'''

# 1. list []

data_list = ['ghois', 'aray', 'dapin']
print (f"list = {data_list[0]}")

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")

# 2. dictionary {}

data_dict = {
    'key': 'value',
    'gs' : 'ghois',
    'ry' : 'aray',
    'int' : 100,
    'float' : 100.12345,
    'boolean' : True,
    'list' : data_list,
}

print ("data dictionary =",data_dict['key'])
print ("data dictionary =",data_dict['gs'])
print ("data dictionary =",data_dict['ry'])
print ("data dictionary =",data_dict['int'])
print ("data dictionary =",data_dict['float'])
print ("data dictionary =",data_dict['boolean'])
print ("data dictionary =",data_dict['list'])

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")

























































































print ("BAB 37")
print("------")

'''           ====BAB 37 (Operasi pada dictionary)====
''' 

data_dict = {
    'key': 'value',
    'gs' : 'ghois',
    'ry' : 'aray',
    'int' : 100,
    'float' : 100.12345,
    'boolean' : True,
}

# 1. mencari panjang dictionary 

print((''),10*('='), ('MENCARI PANJANG DICT'), ('=')*10,"")

LENDICT = len(data_dict)
print(f"Panjang data_dict adalah: {LENDICT}")

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# 2. mengecek suatu kata kunci ada atau tidak didalam dictionary 

print((''),10*('='), ('MENGECEK SUATU KEY'), ('=')*10,"")

KEY = 'gs'
CHECKKEY = KEY in data_dict
print (f"Apakah {KEY} ada didalam data_dict: {CHECKKEY}")

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")








# 3. memanggil kata kunci dengan get 

print((''),10*('='), ('MEMANGGIL KATA KUNCI DENGAN GET'), ('=')*10,"")

'''
    perbedaan memanggil kata kunci dengan get adalah ketika kata kunci yang 
kita panggil ternyata tidak ada di dalam dictionary, ketika tidak menggunakan 
get maka dia akan error, tapi ketika menggunakan get dia akan (none) 
atau bahkan none nya bisa kita ganti sesuka hati  
'''

        # tanpa get 
print(data_dict['ry']) 
print ('------------------------------------------------')
        # dengan get 
print(data_dict.get('ry'))
print(data_dict.get('gs'))
print(data_dict.get('ab'))
print(data_dict.get('ab', 'key tidak ada di dalam dictionary'))
print(data_dict.get('ab', 'key gaono nde dictionary '))

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")






# 4. mengupdate data

print((''),10*('='), ('MENGUPDATE DATA'), ('=')*10,"")

print (10*('-'),'data sebelum di update', 10*('-'))
print (data_dict)



print (10*('-'),'data setelah di update', 10*('-'))

data_dict.update({'dv':'davin'})
data_dict.update({'aly':'alysia'})
data_dict.update({'gs':'goissss'}) # jika data yang di update ternyata sudah ada di dalam dictionary, maka data tersebtu akan di ganti dengan yang baru
data_dict.update({'ry':'arrayyy'}) 
print (data_dict)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# 5. mendelete data

print((''),10*('='), ('MENDELETE DATA'), ('=')*10,"")

print (10*('-'),'data sebelum didelete', 10*('-'))

print (data_dict)



print (10*('-'),'data setelah didelete', 10*('-'))

del data_dict['int']
del data_dict['float']
del data_dict['boolean']
del data_dict['key']
print (data_dict)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")





















































































print ("BAB 38")
print("------")

'''           ====BAB 38 (looping dictionary)====
''' 

teman_teman = {
    'is' : 'gois',
    'ray' : 'aray',
    'pin' : 'dapin',
    'im' : 'ima',
    'lys' : 'alysia'
}

# looping langsung

print((''),10*('='), ('LOOPING LANGSUNG'), ('=')*10,"")

'''
    jika di looping langsung maka yang keluar hanya key nya saja, value nya tidak keluar  
'''

for teman in teman_teman:
    print (teman)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# mengambil key nya saja 

print((''),10*('='), ('MENGAMBIL KEY NYA SAJA'), ('=')*10,"")

keys = teman_teman.keys()
print (keys)

print(50*('-'))

for key in teman_teman.keys():
    print (key)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# mengambil value nya saja 

print((''),10*('='), ('MENGAMBIL VALUE NYA SAJA'), ('=')*10,"")

value = teman_teman.values()
print (value)

print(50*('-'))

for value in teman_teman.values():
    print (value)


print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")







# mengambil key dan value menggunakan get 

print((''),10*('='), ('MENGAMBIL KEY DAN VALUE MENGGUNAKAN GET'), ('=')*10,"")

'''
        ketika menggunakan get, yang di dictionary akan keluar key, tapi ketika di loop 
    yang keluar adalah value 
'''

keys = teman_teman.keys()
print (keys)

print(50*('-'))

for key in teman_teman.keys():
    print (teman_teman.get(key))


print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")






# mengambil key dan value secara bersamaan 

print((''),9*('='), ('MENGAMBIL KEY DAN VALUE SECARA BERSAMAAN'), ('=')*9,"")

items = teman_teman.items()
print (items)

print(50*('-'))

for item in teman_teman.items():
    print (item)


print(('\n'),50*('='),('\n'))


items = teman_teman.items()
print (items)

print(50*('-'))

for item,value in teman_teman.items():
    print (f'item = {item}\t value = {value}')

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")























































































print ("BAB 39")
print("------")

'''           ====BAB 39 (copy and pop dictionary)====
''' 

# copy dictionary

print((''),30*('*'), ('COPY'), ('*')*30,"")

teman_1 = {
    'is' : 'gois',
    'ray' : 'aray',
    'pin' : 'dapin',
}

teman_2 = teman_1.copy()

print((''),10*('='), ('TEMAN 1 SEBELUM DI UBAH'), ('=')*10,"")
print(teman_1)
print((''),10*('='), ('TEMAN 2 SEBELUM DI UBAH'), ('=')*10,"")
print(teman_2,('\n'))

''' ------------- mengubah item teman_1 saja item teman_2 tetap ------------'''

print((''),10*('='), ('TEMAN 1 SETELAH DI UBAH'), ('=')*10,"")

teman_1 ["pin"] = "jhon"
print(teman_1)

print((''),10*('='), ('TEMAN 2 SETELAH DI UBAH'), ('=')*10,"")

print(teman_2)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")









# pop dictionary (mengeluarkan item menggunakan key )

print((''),30*('*'), ('POP'), ('*')*30,"")

print((''),10*('='), ('TEMAN 2 SEBELUM DAPIN KELUAR'), ('=')*10,"")

print(teman_2)

mengambil_datadapin = teman_2.pop('pin')

print((''),10*('='), ('TEMAN 2 SETELAH DAPIN KELUAR'), ('=')*10,"")

print(teman_2, '\n')
print(mengambil_datadapin)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")









# popitem dictionary (mengeluarkan item terakhr)

print((''),30*('*'), ('POP ITEM'), ('*')*30,"")

print((''),10*('='), ('TEMAN 2 SEBELUM ARAY KELUAR'), ('=')*10,"")

print(teman_2)

mengambil_dataaray = teman_2.popitem()

print((''),10*('='), ('TEMAN 2 SETELAH ARAY KELUAR'), ('=')*10,"")

print(teman_2, '\n')
print(mengambil_dataaray)
print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")

























































































print ("BAB 40")
print("------")

'''           ====BAB 40 (multi keys dan nesting dictionary)====
''' 

import datetime

mahasiswa_1 = {
    'nama' : 'Qotrul Ghoist',
    'nim' : '0090001',
    'sks' : '144',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2006,3,18)
}

mahasiswa_2 = {
    'nama' : 'Citra Yuana',
    'nim' : '0090002',
    'sks' : '144',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2004,6,24)
}

mahasiswa_3 = {
    'nama' : 'Rohmatus',
    'nim' : '0090003',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_4 = {
    'nama' : 'Dapin Jhon',
    'nim' : '0090004',
    'sks' : '132',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2002,4,21)
}

mahasiswa_5 = {
    'nama' : 'Ridwan Chelse',
    'nim' : '0090005',
    'sks' : '120',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_6 = {
    'nama' : 'Rizwan Shahan Shah',
    'nim' : '0090006',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_7 = {
    'nama' : 'Dafa Afandi',
    'nim' : '0090007',
    'sks' : '140',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_8 = {
    'nama' : 'Jepri Nichol',
    'nim' : '0090008',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_9 = {
    'nama' : 'Ajeng Dewanti',
    'nim' : '0090009',
    'sks' : '140',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_10 = {
    'nama' : 'Pinka Rivka',
    'nim' : '0090010',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_11 = {
    'nama' : 'Firgi Asmoro',
    'nim' : '0090011',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_12 = {
    'nama' : 'Radit Benictus',
    'nim' : '0090012',
    'sks' : '120',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_13 = {
    'nama' : 'Andro Sofyan',
    'nim' : '0090013',
    'sks' : '120',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2004,3,19)
}

mahasiswa_14 = {
    'nama' : 'Imelya windy',
    'nim' : '0090014',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_15 = {
    'nama' : 'Itfinah Khoirun',
    'nim' : '0090015',
    'sks' : '120',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2004,3,19)
}

mahasiswa_16 = {
    'nama' : 'Marwa Mirwi',
    'nim' : '0090016',
    'sks' : '130',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2004,3,19)
}

mahasiswa_17 = {
    'nama' : 'Dimas Kuy',
    'nim' : '0090017',
    'sks' : '110',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2004,3,19)
}

mahasiswa_18 = {
    'nama' : 'Haikal Ramadhan',
    'nim' : '0090018',
    'sks' : '130',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_19 = {
    'nama' : 'Rivaldi Muhammad',
    'nim' : '0090019',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_20 = {
    'nama' : 'Hasna Deandra',
    'nim' : '0090020',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_21 = {
    'nama' : 'Cleo Dewanti',
    'nim' : '0090021',
    'sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_22 = {
    'nama' : 'Aurora Dewanti',
    'nim' : '0090022',
    'sks' : '110',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_23 = {
    'nama' : 'Abyan Abyin',
    'nim' : '0090023',
    'sks' : '120',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2006,3,19)
}

mahasiswa_24 = {
    'nama' : 'Getha Pinkandao',
    'nim' : '0090024',
    'sks' : '110',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2005,3,19)
}

mahasiswa_25 = {
    'nama' : 'alfi Alfiansyah',
    'nim' : '0090025',
    'sks' : '130',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2007,3,20)
}

data_mahasiswa = {
    'MAH001' : mahasiswa_1,
    'MAH002' : mahasiswa_2,
    'MAH003' : mahasiswa_3,
    'MAH004' : mahasiswa_4,
    'MAH005' : mahasiswa_5,
    'MAH006' : mahasiswa_6,
    'MAH007' : mahasiswa_7,
    'MAH008' : mahasiswa_8,
    'MAH009' : mahasiswa_9,
    'MAH0011' : mahasiswa_11,
    'MAH0012' : mahasiswa_12,
    'MAH0013' : mahasiswa_13,
    'MAH0014' : mahasiswa_14,
    'MAH0015' : mahasiswa_15,
    'MAH0016' : mahasiswa_16,
    'MAH0017' : mahasiswa_17,
    'MAH0018' : mahasiswa_18,
    'MAH0019' : mahasiswa_19,
    'MAH0020' : mahasiswa_20,
    'MAH0021' : mahasiswa_21,
    'MAH0022' : mahasiswa_22,
    'MAH0023' : mahasiswa_23,
    'MAH0024' : mahasiswa_24,
    'MAH0025' : mahasiswa_25
}

print(f"|{' KEY':<10}|{' NAMA':<20} |{' NIM':<11} |{' SKS':<7} |{' BEASISWA':<12} |{' LAHIR':<10}")
print (75*('-'))

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa [KEY]['nama']
    NIM = data_mahasiswa [KEY] ['nim']
    SKS = data_mahasiswa [KEY] ['sks']
    BEASISWA = data_mahasiswa [KEY] ['beasiswa']
    LAHIR = data_mahasiswa [KEY] ['lahir'].strftime('%x')

    print(f"|{KEY:<10}| {NAMA:<20}| {NIM:<11}| {SKS:<7}| {BEASISWA:^12}| {LAHIR:<10}")























































































import datetime
import os
os.system('cls')

print ("BAB 41")
print("------")

'''           ====BAB 41 (Latihan dictionary part 1))====
''' 

mahasiswa_template = {
    'nama' : 'Qotrul Ghoist',
    'nim' : '0090001',
    'sks' : '144',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2006,3,18)
}

data_mahasiswa = {}

print (f"{'MASUKKAN DATA MAHASISWA':^40}")
print ("-"*40)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa_nama = mahasiswa['nama'] = input ('Nama mahasiswa: ')
mahasiswa_nim = mahasiswa['nim'] = input ('NIM mahasiswa: ')
mahasiswa_sks = mahasiswa['sks'] = int(input('Jumlah sks mahasiswa: '))
mahasiswa_bea = mahasiswa['beasiswa'] = bool ('Beasiswa mahasiswa (1/0): ')
TAHUN_LAHIR = int(input ('Tahun lahir (YYYY): '))
BULAN_LAHIR = int(input ('Bulan lahir (1-12): '))
TANGGAL_LAHIR = int(input ('Tanggal lahir (1-31): '))
mahasiswa_lahir = mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)


print(f"|{' NAMA':<20} |{' NIM':<11} |{' SKS':<7} |{' BEASISWA':<12} |{' LAHIR':<10}")
print (70*('-'))
print(f"| {mahasiswa_nama:<20}| {mahasiswa_nim:<11}| {mahasiswa_sks:<7}| {mahasiswa_bea:^12}| {mahasiswa_lahir.strftime('%x')}")


























































































import datetime
import os
import string
import random

print ("BAB 42")
print("------")

'''           ====BAB 42 (Latihan dictionary part 2)====
''' 

mahasiswa_template = {
    'nama' : 'Qotrul Ghoist',
    'nim' : '0090001',
    'sks' : '144',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2006,3,18)
}

data_mahasiswa = {}


while True:      
    os.system('cls')
    print ("-"*67)
    print (f"{'MASUKKAN DATA MAHASISWA':^60}")
    print ("-"*67,'\n')

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa_nama = mahasiswa['nama'] = input ('NAMA\t\t\t: ')
    mahasiswa_nim = mahasiswa['nim'] = input ('NIM\t\t\t: ')
    mahasiswa_sks = mahasiswa['sks'] = int(input('Jumlah sks lulus\t: '))
    TAHUN_LAHIR = int(input ('Tahun lahir (YYYY)\t: '))
    BULAN_LAHIR = int(input ('Bulan lahir (1-12)\t: '))
    TANGGAL_LAHIR = int(input ('Tanggal lahir (1-31)\t: '))
    mahasiswa_lahir = mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)


    print (67*('-'))
    print(f"\n\n\n\n\n\n\n|{'KODE':<8}|{' NAMA':<20} |{' NIM':<11} |{' SKS':<7} |{' LAHIR':<11} |")
    print (67*('-'))


    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa [KEY]['nama']
        NIM = data_mahasiswa [KEY] ['nim']
        SKS = data_mahasiswa [KEY] ['sks']
        LAHIR = data_mahasiswa [KEY] ['lahir'].strftime('%x')

        print(f"|{KEY:<8}| {NAMA:<20}| {NIM:<11}| {SKS:<7}| {LAHIR:<11}|")

    print(f'\n\n\n----------------------------\nTekan "enter" untuk lanjut \nKlik "n" untuk selesai')
    is_mareh = input('Mau lanjut kah? ')
    if is_mareh == "n":
        break
print("\n\n\n",35*('='), ('Ending'), ('=')*35,"\n\n\n\n\n")




























































































print ("BAB 43")
print("------")

'''           ====BAB 43 (Pengenalan fungsi)====
''' 

'''
        fungsi adalah sebuah kode yang dibuat untuk mempersingkat kode, fungsinya 
    agar kita tdak mengulang kode yang sama.

    fungsi dalam beberapa bahasa 
        1. fungsi
        2. function
        3. method
        4. rutin
        5. sub rutin
'''

def anjay():
    print('Perhatian untuk yang bernama supri')
    print('diharap untuk segerra kembali ke kelas')

anjay(), anjay()
anjay()

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")

def aray():
    print('aku cinta kamu')
    print('I LOVE U')

aray()
aray()

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")
































































































print ("BAB 44")
print("------")

'''           ====BAB 44 (fungsi Dengan argument)====
''' 

def Teman_teman(nama):
    print(f"oi {nama}, lama ga jumpa")

Teman_teman("dapin")
Teman_teman("ima")
Teman_teman("alysia")

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")






def peserta (list_peserta):
    list_copy = list_peserta.copy()
    for list_ini in list_copy:
        print(f'Yang terhormat {list_ini}')


lomba1 = ['aray', 'dapin', 'ima', 'alysia']
lomba2 = ['lita', 'imel', 'surya', 'bayu']
lomba3 = ['rizwan', 'ridwan', 'jepri', 'pandi']


peserta(lomba1)
print(20*("-"))

peserta(lomba2)
print(20*("-"))

peserta(lomba3)
print(20*("-"))

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")

























































































print ("BAB 45")
print("------")

'''           ====BAB 45 (fungsi Dengan return)====
''' 

# hasil return hanya satu

print(10*('='), ('HASIL RETURN HANYA SATU'), ('=')*10)

def kuadrat(input_angka):
    hasil = input_angka ** 2
    return hasil

x = kuadrat(4)
print(x)


print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")



# hasil return lebih dari satu

print(10*('='), ('HASIL RETURN LEBIH DARI SATU'), ('=')*10)
print(10*('='), ('YANG DI WAKILKAN PAS'), ('=')*10)

def operasi (angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

a,b,c,d = operasi(10,5) # yang mewakilkan harus ada 4 

print(f'hasil tambah = {a}')
print(f'hasil kurang = {b}')
print(f'hasil kali = {c}')
print(f'hasil bagi = {d}')

'''
        tambah, kurang, kali, dan bagi di wakilkan oleh a,b,c,d tapi 
    penting ntuk di perhatikan jika ingin mewakilkan hasil, hasil harus 
    sama dengan jumlah yang harus di wakilkan. contoh jika tambah, 
    kurang, kali, dan bagi jumlahnya ada 4. maka yang mewakilkan 
    harus ada 4, kalau kurang atau lebih maka hasil akan error
'''

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")



# hasil return lebih dari satu

print(10*('='), ('HASIL RETURN LEBIH DARI SATU'), ('=')*10)
print(10*('='), ('YANG DI WAKILKAN TIDAK PAS'), ('=')*10)

def operasi (angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

a,b,*sisa = operasi(10,5) # jika memang hanya mau 2 saja, maka sisa harus di wakilkan seperti pada contoh

print(f'hasil tambah = {a}')
print(f'hasil kurang = {b}')
print(f'hasil kurang = {sisa}')

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")































































































import os
os.system('cls')

print ("BAB 46")
print("------")

'''           ====BAB 46 (default argumen fungsi)====
''' 

# contoh 1

def say_hallo(nama = "ganteng"):
    print(f"hallo {nama}")

say_hallo("ucup")
say_hallo() # jika nama tidak di isi maka otomatis di isi dengan ganteng

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")



# contoh 2

def sapa_dia(nama, pesan = "apa kabar ?"):
    print (f"hai {nama}, {pesan}")

sapa_dia("dapin", "mau kemana ?")
sapa_dia("dapin")

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")





# contoh 3

def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(5))

hasil = hitung_pangkat(pangkat=5, angka=10) # meski di balik maka akan tetap 10 pangkat 5 bukan 5 pangkat 10 
print(hasil)

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")










# contoh 4

def fungsi (input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10)) # menggant nilai input3 yang awalnya 3 menjadi 10
print(fungsi(input3=10, input4= 20)) 
print(fungsi(input2=5, input3=10, input4= 20)) 

print((''),10*('='), ('Ending'), ('=')*10,"\n\n\n")






























































































import os
os.system('cls')

print ("BAB 47")
print("------")

'''           ====BAB 47 (Latihan fungsi)====
''' 

'''                     JIKA MENGGUNAKAN CARA BIASA                     '''

            # # membuat header program 
            # while True:
            #     print(f"{"PROGRAM MENGHITUNG LUAS":^40}")
            #     print(f"{"DAN KELILING PERSEGI PANJANG":^40}")
            #     print(f"{"-"*40:<40}")
            #     
            #     # mengambil input user 
            #     LEBAR = int(input("Masukkkan nilai lebar = "))
            #     PANJANG = int(input("Masukkkan nilai panjang = "))
            #     
            #     # perhitungan 
            #     
            #     LUAS = PANJANG*LEBAR
            #     KELILING = 2*(PANJANG+LEBAR)
            #     
            #     # tampilkan hasil 
            #     
            #     print (f"Hasil perhitungan luas = {LUAS}")
            #     print (f"Hasil perhitungan panjang = {KELILING}")
            #     


'''                     MENGGGUNAKAN FUNGSI                     '''

def header():
    ''' FUNGSI HEADER '''
    print(f"{"-"*40:<40}")
    print(f"{"PROGRAM MENGHITUNG LUAS":^40}")
    print(f"{"DAN KELILING PERSEGI PANJANG":^40}")
    print(f"{"-"*40:<40}")

def input_user():
    ''' MENGAMBIL INPUT USER '''
    lebar = int(input("Masukkkan nilai lebar = "))
    panjang = int(input("Masukkkan nilai panjang = "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    ''' MENGHITUNG LUAS'''
    return panjang * lebar 

def hitung_keliling(panjang, lebar):
    ''' MENGHITUNG KELILING'''
    return 2 * (panjang + lebar)
















while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling (LEBAR, PANJANG)

    print(f"{"_"*40:<40}")

    print (f"Hasil perhitungan luas = {LUAS}")
    print (f"Hasil perhitungan panjang = {KELILING}")

    print(f"{"_"*40:<40}")

    el_lanjut = input("Mau lanjut kah? (y/n) : ")
    print("\n\n\n\n\n")
    if el_lanjut == "n":
        break

print(30*('='), ('Ending'), ('=')*30,"\n\n\n")





















































































import os
import string
os.system('cls')

print ("BAB 48")
print("------")

'''           ====BAB 48 (Penggunaan type hints pada fungsi)====
''' 

'''
        type hints adalah type data yang digunakan untuk mempermudah ketika meakukan 
    poject besar dalam python. untuk penggunaan sendiri opsional tapi disarankan 
    digunakan ketika membuat projek besar. Fungsinya adalah untuk membedakan 
    setiap class, apakah dia int, float, string, atau boolean.
'''

# penggunaan type hints 

def sepuluh_pangkat(argument:int) -> int:
    output = 10**argument
    return output 

HASIL = sepuluh_pangkat(2)
print(HASIL)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")

def display(argument:string):
    print(argument)

display("ghois")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")





















































































import os
os.system('cls')

print ("BAB 49")
print("------")

'''           ====BAB 49 (Penggunaan *args)====
''' 

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi ('ghois', 165, 65)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")

def fungsi (data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi (['aray', 160, 68])

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")

# MENGGUNAKAN *args

def fungsi (*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi ('aray', 160, 68)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")





# studi kasus

def tambah(*data):
    output = 0
    for angka in data:
        output += angka

    return output 

hasil = tambah (1,2,3,4,5,6,7,8,9)
print (f"hasil = {hasil}")

hasil = tambah (10,5,15)
print (f"hasil = {hasil}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")










































































import os
os.system('cls')

print ("BAB 50")
print("------")

'''           ====BAB 50 (Penggunaan **kwargs)====
''' 

'''
     hasil **kwargs selalu dictionary 
'''

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi ('ghois', 165, 65)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")

# menggunakan **kwargs

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi (nama='ghois', tinggi=165, berat=65)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")








# studi kasus 

def math(*args, **kwargs):
    output = 0
    if kwargs ["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs ["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")

    return output 

hasil = math(1,2,3,4,5,6,option="tambah")
print (f"hasil jumlah = {hasil}")
hasil = math(1,2,3,4,5,6,option="kali")
print (f"hasil kali = {hasil}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")






















































































import os
os.system('cls')

print ("BAB 51")
print("------")

'''           ====BAB 51 (fungsi lambda dan anonymous)====
''' 

# FUNGSI LAMBDA

print(10*('='), ('MENGKUADRATKAN ANGKA'), ('=')*10,"")
print(10*('<'), ('TANPA LAMBDA'), ('>')*10,"")

def f_kuadrat (angka):
    return angka**2

print(f"Hasil fungsi kuadrat = {f_kuadrat(5)}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")






# menggunakan lambda 

print(10*('<'), ('DENGAN LAMBDA'), ('>')*10,"")

''' output = lambda arguments:expression '''
kuadrat = lambda angka:angka**2
print(f"Hasil fungsi kuadrat = {kuadrat(5)}")

print(50*('-'))

angka = lambda ang,pang:ang**pang
print(f"Hasil fungsi kuadrat = {angka(5,2)}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")







# sorting atau mengurutkan list menggunakan list biasa 

print(10*('='), ('SORT CARA BIASA'), ('=')*10,"")

data_list_biasa = ["ghoist", "aray", "dapin Jhon"]
print(f"sebelum di sort atau di urutkan  \n= {data_list_biasa}")

print(50*('-'))

data_list_biasa.sort()
print(f"setelah di sort atau di urutkan  \n= {data_list_biasa}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")







# sorting sesuai panjang kata

print(10*('='), ('SORT SESUAI PANJANG KATA'), ('=')*10,"")
print(10*('<'), ('MENGGUNAKAN CARA BIASA'), ('>')*10,"")

data_list_biasa = ["ghoist", "aray", "dapin Jhon"]
print(f"sebelum di sort atau di urutkan  \n= {data_list_biasa}")

print(50*('-'))

data_list_biasa.sort(key=len)
print(f"setelah di sort atau di urutkan  \n= {data_list_biasa}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")








# sorting sesuai panjang kata menmggunakan def

print(10*('<'), ('MENGGUNAKAN def'), ('>')*10,"")

data_list_def = ["ghoist", "aray", "dapin Jhon"]
print(f"sebelum di sort atau di urutkan  \n= {data_list_def}")

print(50*('-'))

def panjang_nama(nama):
    return len(nama)
data_list_def.sort(key=len)
print(f"setelah di sort atau di urutkan  \n= {data_list_def}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")







# sorting sesuai panjang kata menmggunakan lambda

print(10*('<'), ('MENGGUNAKAN lambda'), ('>')*10,"")

data_list_lambda = ["ghoist", "aray", "dapin Jhon"]
print(f"sebelum di sort atau di urutkan  \n= {data_list_lambda}")

print(50*('-'))

data_list_lambda = ["ghoist", "aray", "dapin Jhon"]
data_list_lambda.sort(key=lambda nama:len(nama))
print(f"setelah di sort atau di urutkan  \n= {data_list_lambda}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")








# filter 

print(10*('='), ('FILTER'), ('=')*10,"")
print(10*('<'), ('MENGGUNAKAN def'), ('>')*10,"")

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(data_angka_baru)



print(10*('<'), ('MENGGUNAKAN lambda'), ('>')*10,"")

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

data_angka_baru = list(filter(lambda x:x<5, data_angka))
print(data_angka_baru)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")



# filter angka ganjil genap 

print(10*('='), ('FILTER ANGKA GANJIL'), ('=')*10,"")
data_angka_baru = list(filter(lambda x:(x%2!=0), data_angka))
print(data_angka_baru)

print(10*('='), ('FILTER ANGKA GENAP'), ('=')*10,"")
data_angka_baru = list(filter(lambda x:(x%2==0), data_angka))
print(data_angka_baru)

print(10*('='), ('FILTER ANGKA KELIPATAN 3'), ('=')*10,"")
data_angka_baru = list(filter(lambda x:(x%3==0), data_angka))
print(data_angka_baru)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n")


















# FUNGSI ANONYMMOUS

print(10*('='), ('MENGKUADRATKAN ANGKA'), ('=')*10,"")
print(10*('<'), ('MENGGUNAKAN def'), ('>')*10,"")

def pangkat (angka,n):
    hasil = angka**n
    return hasil 

data_hasil_pangkat_2 = pangkat(5,2)
data_hasil_pangkat_3 = pangkat(5,3)
data_hasil_pangkat_10 = pangkat(5,10)
print(f"hasil fungsi kuadrat = {data_hasil_pangkat_2} \nhasil fungsi kuadrat = {data_hasil_pangkat_3} \nhasil fungsi kuadrat = {data_hasil_pangkat_10}")




print(10*('<'), ('MENGGUNAKAN anonymous'), ('>')*10,"")

def pangkat (n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
pangkat3 = pangkat(3)
pangkat10 = pangkat(10)
print(f"hasil fungsi kuadrat = {pangkat2(5)} \nhasil fungsi kuadrat = {pangkat3(5)} \nhasil fungsi kuadrat = {pangkat10(5)} ")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n")






















































































import os
os.system('cls')

print ("BAB 52")
print("------")

'''           ====BAB 52 (global dan locak scope)====
''' 

'''
        Varible global adaah variable yang di deklarasikan di luar fungsi, jadi 
    kita bisa mengaksesnya di manapun juga, ntah menggunakan def, loop,
    percabangan, dll
'''

nama_global = "(ghois versi global)"   # <-- itu adalah variabel global 



# akses variable global dalam fungsi

print(10*('='), ('VARIABLE GLOBAL DALAM def'), ('=')*10,"")

def fungsi ():
    print (f"fungsi menampilkan {nama_global}")

fungsi()

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")




# akses variable global dalam loop 

print(10*('='), ('VARIABLE GLOBAL DALAM loop'), ('=')*10,"")

for i in range(1,5):
    print(f"loop menampilkan {nama_global} --- ke {i}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")




# akses variable global dalam if

print(10*('='), ('VARIABLE GLOBAL DALAM if'), ('=')*10,"")

if True:
    print(f"If menampilkan {nama_global}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")





'''
        Variable local / local scope adalah varible yang ada di dalam 
    fungsi, loop atau percabangan. jadi dia hanya bisa di gunakan 
    dalam satu tempat saja, seperti fungsi saja, loop saa, atau 
    percabangan saja.
'''

# akses variable local dalam def

print(10*('='), ('VARIABLE LOCAL DALAM def'), ('=')*10,"")

def fungsi2():
    nama_local = "(ghois versi local)"    # <-- itu adalah variabel local yang berada di dalam def
    print(f"fungsi menampilkan {nama_local} ")
    print(f"fungsi menampilkan {nama_local_versi_lain} ")

nama_local_versi_lain = "(aray versi local)" # jika di taruh luar juga bisa, tapi harus sebelum fungsinya di panggil 
fungsi2()

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")






# akses variable local dalam loop

print(10*('='), ('VARIABLE LOCAL DALAM loop'), ('=')*10,"")

for i in range(1,5):
    nama_local = "(ghois versi local)"   # <-- itu adalah variabel local yang berada di dalam loop
    nama_local_versi_lain = "(aray versi local)"
    print(f"loop menampilkan {nama_local} dan {nama_local_versi_lain} --- ke {i}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")





# akses variable local dalam percabangan 

print(10*('='), ('VARIABLE LOCAL DALAM if'), ('=')*10,"")

if True:
    nama_local = "(ghois versi local)"   # <-- itu adalah variabel local yang berada di dalam if / percabangan 
    nama_local_versi_lain = "(aray versi local)"
    print(f"If menampilkan {nama_local}")   
    print(f"If menampilkan {nama_local_versi_lain}")   
print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")





# merubah variabel global 

print(10*('='), ('MERUBAH VARIBLE GLOBAL DALAM def'), ('=')*10,"")

angka = 0
nama = "ghois"

def ubah (angka_baru, nama_baru):
    global angka # menandakan bahwa angka yang awalnya local berubah jadi global
    global nama # menandakan bahwa nama yang awalnya local berubah jadi global
    angka = angka_baru
    nama = nama_baru

print (f"Sebelum di ubah {angka, nama}")
ubah(10, "aray")
print (f"Sesudah di ubah {angka, nama}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")




print(10*('='), ('MERUBAH VARIBLE GLOBAL DALAM loop'), ('=')*10,"")

angka = 0 

for i in range(1,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")





print(10*('='), ('MERUBAH VARIBLE GLOBAL DALAM if'), ('=')*10,"")

angka = 0 

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



























































































import os
os.system('cls')

print ("BAB 53")
print("------")

'''           ====BAB 53 (import statement)====
''' 

'''
        Import statement adalah suatu tools yang sangat berguna untuk 
    menyambung project satu dengan project yang lain.  
'''

# 1. menyambung project C1 dan project C2 dan project C3

print(10*('='), (' 1 '), ('=')*10)

''' isi hanya print saja'''

from Package_1 import Modul_1 # <-- Modul_1 adah contoh modul

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




# 2. import dengan data

print(10*('='), (' 2 '), ('=')*10)

''' isi nya ada datanya bukan hanya print '''

from Package_1 import Modul_2

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




# 3. import dengan data

print(10*('='), (' 3 '), ('=')*10)

''' 
        Bedanya dengan poin yang no 2 adalah file yang di import belum di print, 
    jadi kita print nya di file yang ini. kalua yang poin no 2 print nya sudah 
    dari fie yang di import, atau sebelum di import sudah di print, sedangkan 
    yang poin no 3 ini sebelum di import belum di print jadi baru di print 
    setelah di import 
'''
from Package_1 import Modul_3
print(Modul_3.data_semua )

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")






# 4. import yang ada fungsi, loop, dan percabangan nya. sebagai contoh pake yang def saja

print(10*('='), (' 4 '), ('=')*10)

from Package_1 import Modul_4

hasil = Modul_4.tambah(10,20)
print (f"hasilnya = {hasil}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")






# 5. contoh penggunaan import 

from Package_1 import Modul_5

hasil_tambah = Modul_5.tambah()
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = Modul_5.kali()
print(f"hasil kali = {hasil_kali}")

pangkat_3 = Modul_5.pangkat(3)
print(f"hasi pangkat 3 = {pangkat_3(3)}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")






































































































import os
os.system('cls')

print ("BAB 54")
print("------")

'''           ====BAB 54 (Penggunaan from dan alias(as))====
''' 

# PENGGUNAAN FROM DALAM MENGIMPORT MODUL

''' 
        Fungsi from adalah agar kita tidak menaruh fungsi seperti tambah, ,kali, dan pangkat 
    di semua tempat yang akan di gunakan fungsi tersebut, tapi cukup memindah fungsi tambah, 
    kali, dan pangkat di bagian import agar tidak menulsi ulang kode yang akan di import 
    secara terus menerus. tapi hanya cukup menulis sekali saja yaitu di bagian import 
'''

from Package_1.Modul_5 import tambah, kali, pangkat


hasil_tambah = tambah()
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali()
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"hasi pangkat 3 = {pangkat_3(3)}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")







# PENGGUNAAN ALIAS(as )DALAM MENGIMPORT MODUL

''' 
        Alias berfungsi untuk mengubah nama asli module atau fungsi yang akan di import 
    dengan nama lain sesuka kalian

'''

# alias digunakan untuk mengubah nama fungsi yang di import 

from Package_1.Modul_5 import tambah as terserah_diubah_sesuka_kamu
from Package_1.Modul_5 import kali as kali_aghi
from Package_1.Modul_5 import pangkat as wdohhhhhhh


hasil_tambah = terserah_diubah_sesuka_kamu() # yang awalnya tambah di aliaskan ke terserah_diubah_sesuka_kamu
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali_aghi()
print(f"hasil kali = {hasil_kali}")

pangkat_3 = wdohhhhhhh(3)
print(f"hasi pangkat 3 = {pangkat_3(3)}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")







# alias digunakan untuk mengubah module yang di import

from Package_1 import Modul_5 as module_lima

hasil_tambah = module_lima.tambah() # yang awalnya Modul_5 di aliaskan ke module_lima
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = module_lima.kali()
print(f"hasil kali = {hasil_kali}")

pangkat_3 = module_lima.pangkat(3)
print(f"hasi pangkat 3 = {pangkat_3(3)}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

































































































import time

print ("BAB 55")
print("------")

'''           ====BAB 55 (Cara Menghitung Waktu Eksekusi Suatu File Dalam Python)====
''' 

'''
        Module time adalah module yang sangat berguna untuk menghitung seberapa cepat suatu file ketika 
    di eksekusi atau di run. itu sangat berguna ketika kita sudah membuat project yang besar. akan 
    sangat terasa beda nya ketika di run. 

    template module time

    * import time

    * module time awal
    * isi yang ingin anda cek waktu eksekusi nya 
    * module time akhir
    * perhitungan
'''

# menggunakan module time

t_start = time.time() # module time awal


print ("BAB 4")
print("------")
'''             ====BAB 4 (CASTING ATAU MENGUBAH TIPE DATA)====            '''
print ("====INTEGER====")

#   1. Mengubah tipe data "integer" ke tipe data lain
a = 10          # data integer      # bentuk bilangan bulat
b = float(a)    # diubah ke float   # bentuk bilangan desimal
c = str (a)     # diubah ke string  # bentuk karakter bukan angka karna string
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====FLOAT====")

#   2. Mengubah tipe data "float" ke tipe data lain
a = 10.9        # data float        # bentuk bilangan desimal       # akan di bulatkan ke bawah meskipun 10.9 menjadi 10 bukan 11 
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = str (a)     # diubah ke string  # bentuk karakter bukan angka karna string
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====STRING====")

#   3. Mengubah tipe data "string" ke tipe data lain
a = 10          # data string       # bentuk karakter bukan angka karna string
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = float (a)   # diubah ke float   # bentuk bilangan desimal
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====BOOLEAN====")

#   4. Mengubah tipe data "boolean" ke tipe data lain
a = True        # data boolean      # hasilnya false jika a = 0, dan true jika a = selain 0 
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = float (a)   # diubah ke float   # bentuk bilangan desimal
d = str (a)     # diubah ke boolean # bentuk karakter bukan angka karna string 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # hanya spasi


t_end = time.time() # module time akhir

print("--------------------------------------------------------------------------------") # hanya spasi
print (f"Waktu eksekusi nya adalah = {t_end - t_start}") # perhitungan
print("--------------------------------------------------------------------------------") # hanya spasi



























































































import os
os.system("cls")

print ("BAB 56")
print("------")

'''           ====BAB 56 (Membuat package Sederhana)====
''' 

import Package_1.Modul_5_kw                             # cara 1 # cara biasa 
from Package_1 import Modul_4_kw                        # cara 2 # jika package sudah memiliki 2 modul atau lebih, dan hanya ingin memilih satu modul saja
from Package_1.Modul_4_kw import tambah as wdohhhhhh    # cara 3 # sama seperti cara 2, tapi yang ini lebih dalam karena langsung memamnggil fungsi yang ingin di pakai
                                                        # di alias kan karena tambah bertabrakan dengan kode yang lain, 
hasil_tambah = Package_1.Modul_5_kw.tambah(1,2,3,4,5)
print (f"Hasil tambah dari package adalah {hasil_tambah}")

tambah = Modul_4_kw.tambah(10,20)
print(f"Hasil tambah = {tambah}")

tambah = wdohhhhhh(10,20) # diganti wdohhhh karena fungsi tambah sudah di pakai oleh fungsi yang di atas. jadi betabrakan 
print(f"Hasil tambah = {tambah}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
























































































import os
os.system("cls")

print ("BAB 57")
print("------")

'''           ====BAB 57 (Cara Penggunaan __init__py)====
'''

'''
    contoh template folder yang saya gunakan, kamu hanya perlu fokus ke folder" tersebut saja

        Package_1/
        |── __init__.py
        |── Package_1_1/
        |   |── __init__.py
        |   |── penjumlahan.py
        |   |── pengurangan.py
        |   |── perkalian.py

'''

''' Saya menggunakan fungsi __init__py'''

'''
di __init__.py dalam Package_1_1

    from .Penjumlahan import tambah
    from .Pengurangan import kurang
    from .Perkalian import kali

    

di __init__.py dalam Package_1

    from .Package_1_1 import tambah, kurang, kali

    

di file Materi_Belum_FIX

    import Package_1

    print(Package_1.tambah(10, 5))   
    print(Package_1.kurang(10, 5))   
    print(Package_1.kali(10, 5))     


    

intinya fungsi dari __init__ adalah untuk memudahkan kita dalam hal mengimport
'''




import Package_1

print(Package_1.tambah(10, 5))   # Output: 15
print(Package_1.kurang(10, 5))   # Output: 5
print(Package_1.kali(10, 5))     # Output: 50

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




























































































import os
import io
os.system("cls")

print ("BAB 58")
print("------")

'''           ====BAB 58 (standard library)====
'''

'''
    standard library adalah suatu kumpulan kode yang sudah di buat oleh developer python itu sendiri.

    cara mengakses standard library ada di situs resmi python 
        caranya hanya perlu search: standard library python 
'''

# contoh penggunaan standard library 

import io # menggunakan (io)

# fungsi (io) adalah untuk membaca suatu file

if os.path.exists("file_text.txt"):
    with io.open("file_text.txt", "r") as file: # untuk membaca file File_text.txt
        print(file.read())                      # "r" untuk read atau baca
else:
    print("File tidak ditemukan.")

''' file yang akan di baca harus satu folder dengan file yang akan membaca '''

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")































































































import os
os.system("cls")

print ("BAB 59")
print("------")

'''           ====BAB 59 (tkinter)====
'''

'''
        tkinter adalah salah satu app untuk mengrun hasil code dari python, selama kita hanya menggunakan cmd 
    atau terminal untuk mengrun hasil code kita, selain cmd dan terminal ada tkinter untuk mliat hasil 
    code kita 
'''


# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeeng!"
    showinfo(title="Whazzup!",message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang:")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop()




























































































import os
os.system("cls")

print ("BAB 60")
print("------")

'''           ====BAB 60 (Mengenal pip)====
'''

'''

    pip adalah manajer paket untuk Python yang digunakan untuk menginstal dan 
mengelola pustaka atau modul pihak ketiga. Dengan pip, kamu bisa dengan 
mudah menambahkan berbagai paket Python dari Python Package Index (PyPI) 
ke dalam proyekmu

PyPI bisa di search: PyPI python

    untuk menjalankan beberapa perintah seperti install dan uninstall bisa di 
lakukan di cmd, power shell, ataupun terminal

ada beberapa perintah yang bisa di jalankan:
    1. install 

        pip install (yang akan di install)
cth:    pip install numpy

    2. uninstall

        pip uninstall (yang akan di install)
cth:    pip uninstall numpy

    3. memeriksa pip yang sudah di install

        pip list

    4. memeriksa versi pip

        pip --version

    5. mengupgrade

        pip install --upgrade (yang akan di upgrade)
cth:    pip install --upgrade numpy

    6. memilih versi yang akan d install

        pip install (yang akan di install)==(versi yang di pilih)
cth:    pip install numpy==1.21.0
'''
























































































import os
os.system("cls")

print ("BAB 61")
print("------")

'''           ====BAB 61 (Package Numpy (contoh PIP))====
'''

import numpy as np

# 1. perkenalan menggunakan vektor 

list_a = [1,2,3,4]                  # output list_a = [1, 2, 3, 4]  list ada koma nya 
vector_a = np.array([1,2,3,4])      # output vector_a = [1 2 3 4]   vektor tidak ada koma nya jadi lebih rapi timbang list 

print(f"list_a = {list_a}")         # list tidak bisa di kali langsng
# print(list_a**2) <- ini akan gagal
print(f"vector_a = {vector_a}")
print(f"a pangkat 2 = {vector_a**2}") # vektor bisa di kali langsung
print(f"a kali 5 = {vector_a*5}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")



# 2. membuat matriks menggunakan vektor  

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")



# 3. matriks nol

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")



# 4. matriks satu

ones_d = np.ones((2,2))
print(f"ones c = \n{ones_d}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")



# 5. operasi penjumlahan pada matriks

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n\n\n")





































































































import os
os.system("cls")

print ("BAB 62")
print("------")

'''           ====BAB 62 (Membuat Game sederhana Menggunakan Pygame)====
'''

import pygame

## init
pygame.init()
# variable running game
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

while isRun:
    pygame.time.delay(10)

    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed

    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # game dynamic
    
    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))
    # render ke display
    pygame.display.update()

pygame.quit()


































































































import os
os.system("cls")

print ("BAB 63")
print("------")

'''           ====BAB 63 (Cara Penggunaan __main__.py)====
'''

'''
        Dalam sebuah package rata" akan ada folder __init__ dan __main__, apa 
    fungsinya?, seperti yang kita tahu __init__ berfungsi untuk menyimpan 
    semua import yang kita butuhkan, sedangkan __main__ berfungsi untuk 
    menandai fungsi dari sebuah package, dalam projeck yang besar kita 
    mestinya akan membuat puluhan package nantinya, untuk menandai setiap 
    package kita akan butuh sebuah penanda yang dimana __main__ akan 
    berfungsi sebagai penanda tersebut.   
'''


# __main__ adalah top level code environment

# __name__ == "__main__" ; name akan berubah jadi main jika di jalankan di program utama alias tidak di import 
# jika ada di file program utama

## __name__ pada file program utama

print(10*('='), ('JIKA DI PROGRAM UTAMA'), ('=')*10,"")

print(f"nilai __name__ pada main.py = '{__name__}'")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")





## __name__ pada file program eksternal ; akan berubah jadi nama file bukan main lagi 

print(10*('='), ('JIKA DI IMPORT'), ('=')*10,"")

from Package_1 import Modul_6

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")





## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")


## import package
from Package_1 import Package_1_2



































































































import os
os.system("cls")

print ("BAB 64")
print("------")

'''           ====BAB 64 (Membaca File Eksternal dengan open dan with)====
'''


''' Membuka dan menutup file dengan cara biasa '''




'''
    template membuka dan menutup file degan cara biasa:

    file = open("......txt",mode="r")
    file.close()
'''

print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt",mode="r") # r untuk read atau membaca
                                 # w untuk write atau menulis

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")


'''     1. Baca semua baris sebagai list

        print(file.readlines())


        2. Baca per baris
        
        print(file.readline(),end="")        baca baris pertama
        print(file.readline(),end="")        baca baris kedua


        3. Baca seluruh file
        print(file.read())      read untuk membaca
                                write untuk menulis
 '''        

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")









''' Membuka dan menutup file dengan cara cepat '''




'''
    template membuka dan menutup file degan cara cepat:

    with open(".....txt",mode="r") as file:
        terserah = file.readline()
        print(terserah,end="")   

    Tidak perlu pake close sudah otomatis
'''

## salah satu teknik membuka file di python

print("\n",3*"=", " Membaca file txt dengan with", 3*"=")

with open("data.txt",mode="r") as file:
    teserah = file.readline()
    print(teserah,end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")















































































































import os
os.system("cls")

print ("BAB 65")
print("------")

'''           ====BAB 65 (Menulis File Eksternal)====
'''

# 1. mode write

'''
    Mode Write(w) adalah dia akan menimpa file yang lama dengan yang baru.
'''

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("overwrite")






# 2. mode append

'''
        Mode Append(a) adalah dia akan menambah file lama dengan file baru, 
    kebalikan dari write(w). dengan syarat file pertama harus di 
    formatkan w kemudian file keduanya baru menggunakan format a
'''

with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")






# 3. mode r+

'''
    Mode r+ adalah menimpa isi text sesuai dengan panjang data. 
    
    cth: file lama 

    baris 1
    baris 2
    baris 3

        file baru 

    ucup

    panjang ucup adaah 4 huruf maka otong akan mengganti 4 huruf dari file yang lama 

        output 

    ucups 1
    baris 2
    baris 3
'''

with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("ucup") # menimpa isi text sesuai dengan panjang data








































































































import os
os.system("cls")

print ("BAB 66")
print("------")

'''           ====BAB 66 (Mengenal Macam-macam error dan try-except)====
'''

'''
        Exception dalam Python adalah kondisi atau peristiwa yang terjadi saat program berjalan 
    dan menyebabkan program berhenti secara tiba-tiba jika tidak ditangani. Exception 
    biasanya muncul karena kesalahan, seperti mencoba membagi angka dengan nol, mengakses 
    indeks yang tidak ada dalam sebuah list, atau membaca file yang tidak ditemukan.

'''

# Contoh sederhana exception adalah:

        # angka = 10
        # pembagi = 0
        # hasil = angka / pembagi  # Ini akan memunculkan ZeroDivisionError


'''
        Untuk mencegah program berhenti tiba-tiba, kita bisa menggunakan blok try-except. Dengan cara 
    ini, kita bisa menangani error yang muncul dan memberi respon yang sesuai.
'''

try:
    angka = 10
    pembagi = 0
    hasil = angka / pembagi
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")









# contoh membuat exception

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(5,6))









# contoh aplikasi untuk membuat file data_4.txt 
try:
    with open("data_4.txt",'r') as file:
        print(file.read())
except:
    print("file data_4.txt tidak ditemukan, membuat file baru")
    with open("data_4.txt",'w',encoding='utf-8') as file:
        file.write("file baru")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")






# contoh di aplikasi

while(True):
    angka = int(input("masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukan input lagi")

print(10*('='), ('Ending'), ('=')*10,"\n\n\n")


print ("=======================================")