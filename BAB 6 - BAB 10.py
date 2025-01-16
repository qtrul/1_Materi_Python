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
'''                                      ====BAB 6 (OPERASI ARITMATIKA)====                                      '''
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















