energi_listrik= 0
for hari in range(1,8):
    print("hari ke", hari)
    energi_listrik -= 100
    print("energi listrik yang tersisa adalah", energi_listrik, "kwh")
    if energi_listrik <= 0:
        print("energi listrik sudah habis")
        break
    
    
energi_listrik_1=1000
for hari in range(1,20):
    print("sekarang hari ke", hari)
    energi_listrik_1 +=100
    print(f"maka energi listrik yang tersisa adalah {energi_listrik_1} ")
    if energi_listrik_1 >= 2000:
        print("energi listrik sudah penuh")
        break
    
    
nilai =0
for hari in range(1,20):
    print("hari ke", hari)
    nilai += 10
    print(f"nilai yang saya dapatkan hari ini adalah {nilai}")
    if nilai >= 100:
        print("nilai sudah tercapai")
        break  
    
nilai_a=0
hari_a= 1
while nilai <= 100:
    print("hari ke", hari_a)
    nilai_a += 10
    print(f"nilai yang saya dapatkan hari ini adalah {nilai_a}")
    hari_a += 1
    if nilai_a >=100:
        print("nilai sudah tercapai")
        break
    
    
energi_harian=[5000,4500,5500,6000,3500,3000]
batas_energi= 3500
true='listrik memenuhi batas energi yang ditentukan'
false='listrik tidak memenuhi batas energi yang ditentukan'
for hari,energi in enumerate(energi_harian, start=1):#jadi fungsi dari enumarate adalah untuk mengembalikan nilai dari iterable yang kita gunakan, jadi kita bisa mendapatkan nilai index dan nilai dari iterable tersebut
    if energi < batas_energi:
        print(f"energi pada hari ke-{hari} adalah {energi} kwh, kurang dari batas energi maka hasinya adalah {energi > batas_energi and true or false}")
        break
    print(f"hari ke-{hari} energinya adalah {energi} kwh maka hasilnya adalah {energi >= batas_energi and true or false}")
else:
    print("seluruh energi harian sudah memenuhi batas energi")
 