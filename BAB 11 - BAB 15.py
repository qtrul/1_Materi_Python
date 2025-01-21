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
















print  ("============================")