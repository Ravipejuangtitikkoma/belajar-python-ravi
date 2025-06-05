nilai=0
hari=1#kalau di while biar harinya otomatis bertambah kita harus mendeklarasikan variabel hari terlebih dahulu, jadi tidak seperti for yang harus mengunakan range dan pada saat di dalamnya kita harus tambah kan hari +=1 untuk menambah harinya
while nilai < 100:#kalau dalam while kita bisa menggunakan kondisi yang kita inginkan, jadi tidak harus sama dengan for yang sudah ditentukan
    print("hari ke", hari)
    nilai += 10
    print(f"nilai yang saya dapatkan hari ini adalah {nilai}")
    hari += 1
    if nilai >= 100:
        print("nilai sudah tercapai")
        break
kapasitas_baterai =0
kapasitas_aman=80
while kapasitas_baterai < 100:
    kapasitas_baterai += 10
    print(f"kapasitas baterai sekarang adalah {kapasitas_baterai} % dan ini merupakan baterai yang {kapasitas_baterai <= kapasitas_aman and 'aman' or 'tidak aman'}")
    if kapasitas_baterai >= kapasitas_aman:
        print("baterai sudah aman")
        break
    
kapasitas_baterai_1 =0
kapasitas_aman_2=200
error=False
while kapasitas_baterai_1 < 200:
    kapasitas_baterai_1 +=10
    if kapasitas_baterai_1 == 50 and not error :
        print("baterai mengalami error, silahkan ganti baterai")
        error=True
        continue#jadi fungsi dari continue adalah untuk melanjutkan ke iterasi berikutnya,
    print(f"kapasitas baterai sekarang adalah {kapasitas_baterai_1} % dan ini merupakan baterai yang {kapasitas_baterai_1 <= kapasitas_aman_2 and 'aman' or 'tidak aman'}")
    if kapasitas_baterai_1 >= kapasitas_aman_2:
        print("baterai sudah aman")
        break
else:
     print("baterai belum aman, silahkan isi ulang")
        
    
    
        
    
    
        