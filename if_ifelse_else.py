nilai_a=60
nilai_b=80
if nilai_a  >=90:
    print("anda lulus ujian dengan nilai a")
elif nilai_a <=80:
    print("anda lulus ujian dengan nilai b")
else:
    print("anda tidak lulus ujian")
    
print (nilai_a)


uts=500
umum=600
ujian=500
umum_2=200
if uts >= umum and ujian >= umum_2:#jika kita pakai and maka apabila salah satu nilai tidak memenuhi maka hasilnya akan false jadi dia harus memenuhi keduanya
    print("anda lulus dalam penilayan")
elif uts < umum or ujian < umum_2:#sedangkan jika kita pakai or maka apabila salah satu ketentuan terpenuhi maka nilainya akan true jadi dia hanya perlu memenuhi salah satu saja
    print("anda masih kurang dalam penilayan")
else:
    print("anda tidak lulus ")