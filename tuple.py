koordinat_desa_makmur = (107.1234, -6.1234)  # Tuple untuk koordinat desa makmur
latitude= koordinat_desa_makmur[0]
logitude= koordinat_desa_makmur[1]
print(f"latitude: {latitude}, logitude: {logitude}")
for nama in koordinat_desa_makmur:
    print("koordinat:", nama)
    
list_nama=(
    ("ravi armanza",(-107.098,78),50),
    ("revan",(009.123,789),80),
    ("reza",(009.567,709),80),   
)
for daftar in list_nama:
    nama,(bulan,tanggal),umur = daftar
    print("perkenalkan nama saya {nama}, saya lahir pada bulan {bulan} tanggal {tanggal} dan umur saya sekarang adalah {umur} tahun")   
