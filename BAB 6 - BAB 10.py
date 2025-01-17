#print ("BAB 6")
#print("------")
#'''             ====BAB 6 (OPERASI ARITMATIKA)====                                  '''
#'''Jenis-jenis operasi:                                                             '''                            
#'''     1. Operasi penjumlahan (+)                                                  '''                                              
#'''     2. Operasi pengurangan (-)                                                  '''                              
#'''     3. Operasi perkalian (*)                                                    '''                          
#'''     4. Operasi pembagian (/)                                                    '''                                  
#'''     5. Operasi eksponen atau pangkat (**)                                       '''                              
#'''     6. Operasi modulus atau sisa pembagian (%)                                  '''                                      
#'''           cth: -) jika 10 / 2 = 5, maka modulus 0                               '''                                                  
#'''                -) jika 5 / 2 = 2.5, maka modulus 1                              '''                                  
#'''                   maksudnya begini, 5 / 2 sama dengan 2 * x = 5                 '''                           
#'''                   anggap x = 2, maka 2 * 2 = 4, tidak bisa menjadi 5,           '''                          
#'''                   jadi dianggap sisa 1 atau modulus 1                           '''
#'''                -) jika 10 / 3 , maka modulus = 1                                '''                        
#'''                   3 * 2 = 9, sisanya 1 atau modulusnya 1                        '''                    
#'''     7. Operasi floor division atau hasil pembagian yang dibulatkan kebawah (//) '''                        
#'''           cth: -) 10 / 3 = 3,333333                                             '''                        
#'''                   10 // 3 = 3                                                   '''                        
#'''                -) 10 / 6 = 1,666666                                             '''                        
#'''                   10 // 6 = 1                                                   '''                        
#'''                                                                                 '''                                    
#'''Prioritas operasi:                                                               '''                            
#'''     1. Tanda kurung ()                                                          '''                            
#'''     2. Eksponen **                                                              '''                            
#'''     3. Perkalian dan teman" (*, /, %, //)                                       '''                            
#'''     4. Penjumlahan dan pengurangan (+, -)                                       '''                            
#                                                                       
#a = 5
#b = 2
#
##1. Operasi penjumlahan
#c = a + b
#print (a, "+" ,b, "=" ,c)
#
##2. Operasi pengurangan
#c = a - b
#print (a, "-" ,b, "=" ,c)
#
##3. Operasi perkalian
#c = a * b
#print (a, "*" ,b, "=" ,c)
#
##4. Operasi pembagian
#c = a / b
#print (a, "/" ,b, "=" ,c)
#
##5. Operasi eksponen
#c = a ** b
#print (a, "**" ,b, "=" ,c)
#
##6. Operasi modulus
#c = a % b
#print (a, "%" ,b, "=" ,c)
#
##7. Operasi floor division
#c = a // b
#print (a, "//" ,b, "=" ,c)
#
#print ("")
#
#
#
#
#
#
#
#print ("BAB 7")
#print("------")
#'''                                      ====BAB 6 (OPERASI ARITMATIKA)====                                      '''
#''' Rumus umum                                                                                                   '''                                                                                                                                                                              
#'''                                                                                                              '''                                                                                                                                                                   
#''' |          |      celcius        |        Reamur       |       Fahrenheit      |          Kelvin           | '''                                                                                                                                                                                                                                                                             
#''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                                
#''' |celcius   |         -           |(4/5)*celcius        |(9/5)*(celcius+32)     |celcius+273                | '''                                                                                                                                                                                                                                                   
#''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                             
#''' |Reamur    |(5/4)*reamur         |           -         |(9/4)*(reamur+32)      |(5/4)*(reamur+273)         | '''                                                                                                                                                                                                                                             
#''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                               
#''' |Fahrenheit|(5/9)*(fahrenheit-32)|(4/9)*(fahrenheit-32)|           -           |(fahrenheit-32)*((5/9)+273)| '''                                                                                                                                                                                                                                                                 
#''' ------------------------------------------------------------------------------------------------------------ '''                                                                                                                                                                                                                                                                               
#''' |Kelvin    |kelvin-273           |(4/5)*(kelvin-273)   |(kelvin-273)*((9/5)+32)|            -              | '''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#
##Satuan celcius ke satuan lain 
#print ("\n====CELCIUS====")
#celcius = float(input("Masukkan suhu dalam Celcius ="))
#print ("Suhu dalam Celcius = ", celcius, "celcius")
#
#reamur = (4/5)*celcius
#print ("Suhu dalam Reamur = ", reamur, "reamur")
#
#fahrenheit = (9/5)*(celcius+32)
#print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")
#
#kelvin = celcius+273
#print ("Suhu dalam Kelvin = ", kelvin, "kelvin")
#
#
#
#
#
##Satuan reamur ke satuan lain
#print ("\n====REAMUR====")
#reamur = float(input("Masukkan suhu dalam Reamur ="))
#
#celcius = (5/4)*reamur
#print ("Suhu dalam Celcius = ", celcius, "celcius")
#
#print ("Suhu dalam Reamur = ", reamur, "reamur")
#
#fahrenheit = (9/4)*(reamur+32)
#print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")
#
#kelvin = (5/4)*(reamur+273)
#print ("Suhu dalam Kelvin = ", kelvin, "kelvin")
#
#
#
#
#
##Satuan fahrenheit ke satuan lain 
#print ("\n====FAHRENHEIT====")
#fahrenheit = float(input("Masukkan suhu dalam Fahrenheit ="))
#
#celcius = (5/9)*(fahrenheit-32)
#print ("Suhu dalam Celcius = ", celcius, "celcius")
#
#reamur =(4/9)*(fahrenheit-32)
#print ("Suhu dalam Reamur = ", reamur, "reamur")
#
#print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")
#
#kelvin = (fahrenheit-32)*((5/9)+273)
#print ("Suhu dalam Kelvin = ", kelvin, "kelvin")
#
#
#
#
#
##Satuan kelvin ke satuan lain 
#print ("\n====CELCIUS====")
#kelvin = float(input("Masukkan suhu dalam Kelvin ="))
#
#celcius = kelvin-273
#print ("Suhu dalam Celcius = ", celcius, "celcius")
#
#reamur = (4/5)*(kelvin-273)
#print ("Suhu dalam Reamur = ", reamur, "reamur")
#
#fahrenheit = (kelvin-273)*((9/5)+32)
#print ("Suhu dalam Fahrenheit = ", fahrenheit, "fahrenheit")
#
#print ("Suhu dalam Kelvin = ", kelvin, "kelvin")
#
#print ("")
#
#
#
#
#
#
#print ("BAB 8")
#print("------")
#
#print ("\n====Operasi Komparasi====\n")
#
#'''Operasi komparasi adalah operasi yang dimana hasilnya selalu boolean (True or False)                                             '''
#'''                                                                                                                                 '''                         
#'''Jenis-jenis operasi komparasi:                                                                                                   '''                             
#'''     1. lebih besar dari (>)                                                                                                     '''                                                     
#'''         cth: 4 > 2 = True                                                                                                       '''                             
#'''              1 > 2 = False                                                                                                      '''                                 
#'''              2 > 2 = False                                                                                                      '''                                 
#'''     2. kurang dari (<)                                                                                                          '''                         
#'''         cth: 4 < 2 = False                                                                                                      '''                                         
#'''              1 < 2 = True                                                                                                       '''                                                                                                                                          
#'''              2 < 2 = False                                                                                                      '''                                          
#'''     3. lebih dari sama dengan (>=)                                                                                              '''                                                 
#'''         cth: 4 >= 2 = True                                                                                                      '''                                         
#'''              1 >= 2 = False                                                                                                     '''                                           
#'''              2 >= 2 = True                                                                                                      '''                                         
#'''     4. kurang dari sama dengan (<=)                                                                                             '''                                                  
#'''         cth: 4 <= 2 = False                                                                                                     '''                                          
#'''              1 <= 2 = True                                                                                                      '''                                         
#'''              2 <= 2 = True                                                                                                      '''                                         
#'''     5. sama dengan (==)                                                                                                         '''                                      
#'''         cth: 4 == 4 = True                                                                                                      '''                                         
#'''              4 == 2 = False                                                                                                     '''                                           
#'''     6. tidak sama dengan (!=)                                                                                                   '''                                            
#'''         cth: 4 != 4 = False                                                                                                     '''                                          
#'''              4 != 2 = True                                                                                                      '''                                          
#'''     7. is                                                                                                                       '''                    
#'''        is hanya membandingkan objek degan objek                                                                                 '''                                    
#'''   Objek sendiri adalah sesuatu yang memiliki nilai                                                                              '''                                    
#'''   cth:   a = 5, maka a adalah objek yang dimana nilai dari a adalah 5, sedangkan 5 bukan objek tapi "literal" yaitu selain objek'''                                
#'''   Maka a is 5 , tidak bisa karna is hanya membandingkan objek dengan objek, bukan objek dengan literal                          '''                                    
#'''     8. is not                                                                                                                   '''                                        
#'''        is not kebalikan dari is, tapi cara menggunakan nya sama dengan is yaitu membandingkan objek dengan objek                '''                                                        
#
#
#
#b = 10
#c = 5
#
#print( "==== LEBIH BESAR DARI (>)")
##   1. lebih besar dari (>)
#a = b > 8
#print (b, ">" ,8, "=" ,a)
#a = b > 20
#print (b, ">" ,20, "=" ,a)
#a = b > 10
#print (b, ">" ,10, "=" ,a)
#
#print( "==== KURANG DARI (<)")
##   2. kurang dari (<)
#a = b < 8
#print (b, "<" ,8, "=" ,a)
#a = b < 20
#print (b, "<" ,20, "=" ,a)
#a = b < 10
#print (b, "<" ,10, "=" ,a)
#
#print( "==== LEBIH DARI SAMA DENGAN (>=)")
##   3. lebih dari sama dengan >=
#a = b >= 8
#print (b, ">=" ,8, "=" ,a)
#a = b >= 20
#print (b, ">=" ,20, "=" ,a)
#a = b >= 10
#print (b, ">=" ,10, "=" ,a)
#
#print( "==== KURANG DARI SAMA DENGAN (<=)")
##   4. kurang dari sama dengan <=
#a = b <= 8
#print (b, "<=" ,8, "=" ,a)
#a = b <= 20
#print (b, "<=" ,20, "=" ,a)
#a = b <= 10
#print (b, "<=" ,10, "=" ,a)
#
#print( "==== SAMA DENGAN (==)")
##   5. sama dengan ==
#a = b == 20
#print (b, "==" ,20, "=" ,a)
#a = b == 10
#print (b, "==" ,10, "=" ,a)
#
#print( "==== TIDAK SAMA DENGAN (!=)")
##   6. tidak sama dengan !=
#a = b != 20
#print (b, "!=" ,20, "=" ,a)
#a = b != 10
#print (b, "!=" ,10, "=" ,a)
#
#print( "==== is (is)")
##   6. is
#a = b is c
#print (b, "is" ,c, "=" ,a)
#a = b is b
#print (b, "is" ,b, "=" ,a)
#
#print( "==== is not (is not)")
##   7.  is not
#a = b  is not c
#print (b, " is not" ,c, "=" ,a)
#a = b  is not b
#print (b, " is not" ,b, "=" ,a)
#
#print ("")
#




print ("BAB 9")
print("------")

print ("\n====Operasi Logika atau Boolean====\n")

'''Jenis-jenis operasi logika                                                                                           '''
'''     1. not                                                                                                          '''                                                    
'''         not adalah kebalikan, jika a = True maka b = False. Yang artinya a not b atau True not False                '''                                        
'''     2. or                                                                                                           '''                                        
'''         jika ada pilihan True or False hasilnya akan True, intinya dia akan False jika kedua pilihannya itu False.  '''                        
'''       cth: True or False hasilnya True                                                                              '''                                
'''            True or True hasilnya True                                                                               '''                                    
'''            False or False hasilnya False                                                                            '''                                        
'''     3, and                                                                                                          '''                    
'''         and adalah kebalikan dari or, jika ada pilihan True and False hasilnya akan False,                          '''                                                    
'''       intinya dia akan True jika kedua pilihannya itu True.                                                         '''                            
'''       cth: True and False hasilnya False                                                                            '''                                    
'''            True and True hasilnya True                                                                              '''                                    
'''            False and False hasilnya False                                                                           '''                                    
'''     4. xor                                                                                                          '''                                        
'''         Jika True xor False hasilnya False, jika True xor True atau False xor False maka hasilnya True,             '''                                        
'''       intinya dia akan True jika pilihannya berbeda, dan akan False jika pilihannya sama                            '''                                    
'''       cth: True xor True hasilnya False                                                                             '''                                        
'''            False xor False hasilnya False                                                                           '''                                    
'''            True xor False hasilnya True                                                                             '''                                                    
'''            False xor True hasilnya True                                                                             '''                                        

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


















print ("===============================")

















