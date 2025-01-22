print("")
print ("PENDAHULUAN")
print("------------")

'''          ====SHORTCUT====            '''    
'''  1. shift + alt + drag               '''       
'''  2. alt + drag                       '''       
'''  3. ctrl + D                         '''       
'''  4. alt + panah atas/bawah           '''   
'''  5. shift + ctrl + panah atas/bawah  '''

print("") # hanya spasi

'''
        JUDUL SETIAP BAB

====BAB 1  (VARIABEL)
====BAB 2  (TIPE DATA)
====BAB 3  (TIPE DATA KHUSUS)
====BAB 4  (CASTING ATAU MENGUBAH TIPE DATA)
====BAB 5  (INPUT ATAU MENGAMBIL TIPE DATA)
====BAB 6  (OPERASI ARITMATIKA)
====BAB 7  (PENGAPLIKASIAN OPERASI ARITMATIKA)
====BAB 8  (OPERASI KOMPARASI)
====BAB 9  (OPERASI LOGIKA ATAU BOOLEAN)
====BAB 10 (OPERASI LOGIKA DAN KOMPARASI)
====BAB 11 (BITWISE) 
====BAB 12 (PENGENALAN STRING) 
====BAB 13 (OPERASI DAN MANUPULASI STRING)
====BAB 14 (OPERATOR DALAM BENTUK METODE)

'''




































print("BAB 1")
print("------")

'''                 ====BAB 1 (VARIABEL)====                           '''                        
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
'''             ====BAB 2 (TIPE DATA)====            '''
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
'''             ====BAB 3 (TIPE DATA KHUSUS)====            '''
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

print("") # hanya spasi








































print ("BAB 5")
print("------")
'''             ====BAB 5 (INPUT ATAU MENGAMBIL TIPE DATA)====            '''
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
'''             ====BAB 6 (OPERASI ARITMATIKA)====                                  '''
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
'''                                      ====BAB 7 (PENGAPLIKASIAN OPERASI ARITMATIKA)====                                      '''
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

'''             ====BAB 8 (OPERASI KOMPARASI)====                                                                                   '''
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

'''====BAB 9 (OPERASI LOGIKA ATAU BOOLEAN)===='''


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

'''====BAB 10 (OPERASI LOGIKA DAN KOMPARASI)===='''


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

'''           ====BAB 11 (BITWISE)====                                 
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

'''           ====BAB 12 (PENGENALAN STRING)====                                 
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

'''           ====BAB 13 (OPERASI DAN MANUPULASI STRING)====
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

'''           ====BAB 14 (OPERATOR DALAM BENTUK METODE)====
'''

# 1. merubah semua ke upper case

Salam = "AssaLAmuAlAiKUm"
print ("Normal = " + Salam)
SALAM = Salam.upper()
print ("Besaa =" + SALAM)

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







print ("=======================================")