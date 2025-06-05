nama_proyek="pembuatan pakan ikan lele"
lokasi="desa makmur"
jumlah_panel=50
kapasitas_panel=15000
perubahan=lokasi.strip().title() #menggunakan fungsi strip untuk menghilangkan spasi di awal dan akhir string, dan title untuk mengubah huruf pertama setiap kata menjadi kapital
laporan=f"laporan proyek {nama_proyek} di {perubahan} dengan jumlah panel : {jumlah_panel} dan kapasitas panel adalah {kapasitas_panel}"#dan ini merupakan cara membuat string dengan format f-string yang lebih mudah dibaca dan ditulis, dan bisa langsung memasukan variabel ke dalam string
true='ada'
false='tidak ada'
print(laporan)
print("apakah ada nama 'laporan' di dalam laporan ? ", 'Desa Makmur' in laporan and true or false) #ini menggunakan operator in untuk mengecek apakah ada string tertentu di dalam string lain, dan mengembalikan true atau false sesuai dengan kondisi
