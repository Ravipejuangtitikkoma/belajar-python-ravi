siswa={"nama":"Budi","umur":20,"nilai":85}
print("ini meupakan nama nama siwa :",siswa)

siswa_siswa={"nama":"ravi armanza","umur":20,"nilai":85}
print("nama siswanya adalah :", siswa_siswa["nama"])
siswa_siswa ["status"] = "lulus" #menambahkan key baru dengan value baru
print(siswa_siswa)
for key,value in siswa_siswa.items():#gunanya item adalah untuk mengambil dari nilai  siswa_siwa yang merupakan dectionary
    print(f"key: {key}, value: {value}")

siswa_pertama={"nama":"revan kurniawan","tingal di":"perumahan komplek teguh permai duo"}
for keyi,valuei in siswa_pertama.items():
    print(f"perkenalkan nama saya {keyi} dan saya tinggal di {valuei}")
p="perkenalan"