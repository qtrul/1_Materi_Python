#++++++++++++++++++++5---------------10+++++++++90-------92
#+++++++102----------------200++++++++++++++202------------

x = float (input("Masukkan angka  = " ))

dia_true = (x < 5 or 10 < x < 90 or 92 < x < 102 or 200 < x < 202)
dia_false = (5 < x < 10 or 90 < x < 92 or 102 < x < 200 or x > 202)

hasil = dia_true and not dia_false

print ("Maka nilai X adalah = ", hasil)










