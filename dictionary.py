siswa={"nama":"Budi","umur":20,"nilai":85}
print("ini meupakan nama nama siwa :",siswa)

siswa_siswa={"nama":"ravi armanza","umur":20,"nilai":85}
print("nama siswanya adalah :", siswa_siswa["nama"])
siswa_siswa ["status"] = "lulus" #menambahkan key baru dengan value baru
print(siswa_siswa)
for key,value in siswa_siswa.items():
    print(f"key: {key}, value: {value}")