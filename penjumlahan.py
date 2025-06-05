nilai_input= 1000
nilai_output= 850
proses= nilai_output/nilai_input*100
proses_mendalam= 80
proses += 5 #ini contoh pertambahan yang singkat dan artinya sama dengan proses = proses + 5, dan bisa mengunakan operator lainya seperti -,/,+,*, dan masih banyak lagi
print("efisiensi proses adalah", proses, "%")
print("apakah efisiensi memenuhi standar ? ", proses >= proses_mendalam)#ini tipe data boolena yang bisa langsung dikombinasikan dengam operator logika
print("\n \n")
nilai_input= 1000
nilai_output= 850
proses= nilai_output/nilai_input*100
proses_mendalam= 80
is_operasi= "hasinya adalah true" #ini tipe data boolean yang bisa diisi dengan True atau False dan bisa juga kita costum dengan string yang kita inginkan
data="data gagal"
print("apakah operasi sama dengan operasional efisiensi proses adalah =", proses >= proses_mendalam and is_operasi or data )#ini tipe data boolena yang bisa langsung dikombinasikan dengam operator logika contoh and berfunsi untuk menggabungkan dua kondisi yang harus benar semua, sedangkan or berfungsi untuk menggabungkan dua kondisi dimana salah satu saja yang benar sudah cukup
print("apakah efisiensi memenuhi standar ? ", not (proses >= proses_mendalam))# dan fungsi not untuk membalikkan nilai boolean jika nilai data true maka hasilnya akan false dan jika nilai data false makan hasilnya akan true
