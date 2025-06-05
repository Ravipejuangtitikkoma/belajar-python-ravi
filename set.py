teknologi={'samsung','apple','xiamoi','apple'}#ini merupakan set dan dia akan mengapus variabel yang sama
print("apa saja brand teknologi yang sekarang makin berkembang ? ", teknologi)

pertama={'samsung','apple','xiamoi','apple'}
kedua={'samsung','apple','oppo','vivo'}
yang_sama=pertama.intersection(kedua)#jadi kalau kita ingin mencari data yang sama dari dua set kita bisa menggunakan intersection
menggabungkan=pertama.union(kedua)#jadi kalau kita ingin menggabungkan dua set kita bisa menggunakan union
print("apa saja yang sama antara kedua set tersebut ? ", yang_sama)
print("apa saja yang sudah digabungkan dari kedua set tersebut ? ", menggabungkan)

teknologi_standar=frozenset({"panel surya", "matahari"})#jadi kalau kita ingin membuat set yang tidak bisa diubah kita bisa menggunakan frozenset dan juga tidak bisa di hapus 
teknologi_proyek = {"panel surya", "biomassa"}
bergabung= teknologi_standar.union(teknologi_proyek)#jadi kalau kita ingin menggabungkan dua set kita bisa menggunakan union
teknologi_belum_standar = teknologi_standar.difference(teknologi_proyek)#jadi kalau kita ingin mencari data yang tidak ada di set lain kita bisa menggunakan difference
print("teknologi yang standar adalah ", teknologi_standar)
print("teknologi yang belum standar adalah ", teknologi_belum_standar)
print(bergabung)
teknologi_standar.clear()
print(teknologi_standar)