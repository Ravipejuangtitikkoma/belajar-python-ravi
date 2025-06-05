lokasi_proyek=["desa makmur", "desa sejahtera", "desa mandiri"]
print("apa saja tempat yang ada lokasi proyek ? ", lokasi_proyek)

lokasi_rumah=["rumah 1", "rumah 2", "rumah 3"]
lokasi_rumah.append("rumah 4")#jadi kalau kita ingin menambah list kita bisa menggunakan append dan ini merupakan khusus list
print('apa saja lokasi rumah yang ada ?' , lokasi_rumah)
lokasi_rumah.insert(0, "rumah 5")#jadi kalau kita ingin menambah list di awal kita bisa menggunakan insert dan ini merupakan khusus list
lokasi_rumah[1]="rumah 6"#ini untuk mengubah list yang ada pada index 1
print('apa saja lokasi rumah yang ada ?' , lokasi_rumah)
lokasi_rumah.remove("rumah 3")#jadi kalau kita ingin menghapus list kita bisa menggunakan remove dan ini merupakan khusus list
print('apa saja lokasi rumah yang ada ?' , lokasi_rumah)
lokasi_rumah.pop()#jadi kalau kita ingin menghapus list yang ada di akhir kita bisa menggunakan pop dan ini merupakan khusus list
print('apa saja lokasi rumah yang ada ?' , lokasi_rumah)
lokasi_rumah.clear()#jadi kalau kita ingin menghapus semua list kita bisa menggunakan clear dan ini merupakan khusus list
print('apa saja lokasi rumah yang ada ?' , lokasi_rumah)

lokasi_rumah=["rumah 1", "rumah 2", "rumah 3"]
for rumah in lokasi_rumah:
    print(rumah)
    
lokasi_ruko=["ruko 1", "ruko 2", "ruko 3","rumah aji","rumah revan"]
lokasi_desa=[rumeh for rumeh in lokasi_ruko if "ruko" in rumeh]#jadi kalau kita ingin membuat list baru dari list yang ada kita bisa menggunakan list comprehension dan ini merupakan khusus list
print
#ubah format menjadi uppercase
lokasi_upper=[nama.upper()for nama in lokasi_desa]
print("ini merupakan lokasi yang sudah diubah menjadi uppercase :", lokasi_upper)

[]