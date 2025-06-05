class MangroveEcosystem:
    def __init__(self, nama_lokasi, status_ancaman):
        self.nama_lokasi = nama_lokasi
        self.status_ancaman = status_ancaman.lower()
        self.spesies_flora = []
        self.spesies_fauna = []
        self.luas_area = 0  # dalam hektar
        self.karbon_per_hektar = 150  # ton karbon per hektar (rata-rata mangrove)

    def tambah_spesies_flora(self, spesies):
        self.spesies_flora.append(spesies)
        print(f"Spesies flora '{spesies}' berhasil ditambahkan di {self.nama_lokasi}.")

    def tambah_spesies_fauna(self, spesies):
        self.spesies_fauna.append(spesies)
        print(f"Spesies fauna '{spesies}' berhasil ditambahkan di {self.nama_lokasi}.")

    def set_luas_area(self, luas):
        if luas <= 0:
            print("Luas area harus lebih dari 0 hektar!")
        else:
            self.luas_area = luas
            print(f"Luas area {self.nama_lokasi} berhasil diatur menjadi {self.luas_area} hektar.")

    def hitung_potential_karbon(self):
        total_karbon = self.luas_area * self.karbon_per_hektar
        return total_karbon

    def hitung_indeks_biodiversitas(self):
        total_spesies = len(self.spesies_flora) + len(self.spesies_fauna)
        return total_spesies

    def pesan_edukasi(self):
        if self.status_ancaman == "kritis":
            return ("Mangrove di lokasi ini dalam kondisi kritis! Mangrove sangat penting untuk melindungi pesisir dari erosi, menyerap karbon, dan menyediakan habitat bagi spesies seperti kepiting bakau dan burung migran. Ayo, kita selamatkan bersama dengan menanam mangrove baru dan mengurangi polusi!")
        elif self.status_ancaman == "rawan":
            return ("Mangrove di lokasi ini rawan terancam. Tahukah kamu, mangrove bisa menyerap karbon 4 kali lebih banyak dibanding hutan tropis? Mari kita jaga dengan membersihkan sampah dan melibatkan masyarakat dalam pelestarian!")
        else:
            return ("Mangrove di lokasi ini masih sehat! Mari kita terus pelihara dengan monitoring rutin dan edukasi masyarakat. Mangrove adalah rumah bagi banyak spesies dan membantu menjaga kualitas air pesisir!")

    def rekomendasi_aksi(self):
        indeks_biodiversitas = self.hitung_indeks_biodiversitas()
        if indeks_biodiversitas < 5:
            return "Segera lakukan penanaman mangrove tambahan dan survey biodiversitas untuk meningkatkan keanekaragaman hayati!"
        elif self.luas_area < 10:
            return "Perluas area mangrove untuk meningkatkan penyerapan karbon dan mendukung lebih banyak spesies."
        elif self.status_ancaman in ["kritis", "rawan"]:
            return "Lakukan aksi darurat: bersihkan sampah, tanam mangrove baru, dan edukasi masyarakat sekitar!"
        else:
            return "Ekosistem mangrove sehat, lanjutkan monitoring dan libatkan masyarakat dalam pelestarian jangka panjang!"

# Input dari user
print("=== Sistem Pemantauan dan Edukasi Biodiversitas Mangrove oleh BioMac ===")
nama_lokasi = input("Masukkan nama lokasi mangrove (contoh: Hutan Bakau Desa Makmur): ")
status_ancaman = input("Masukkan status ancaman mangrove (kritis/rawan/aman, contoh: rawan): ")
mangrove = MangroveEcosystem(nama_lokasi, status_ancaman)

# Input luas area
luas = float(input("Masukkan luas area mangrove (dalam hektar, contoh: 20): "))
mangrove.set_luas_area(luas)

# Input spesies flora
print("Masukkan 3 spesies flora yang ada di lokasi (contoh: Rhizophora, Avicennia, Sonneratia):")
for i in range(3):
    spesies = input(f"Spesies flora ke-{i+1}: ")
    mangrove.tambah_spesies_flora(spesies)

# Input spesies fauna
print("Masukkan 3 spesies fauna yang ada di lokasi (contoh: Kepiting Bakau, Burung Migran, Ikan):")
for i in range(3):
    spesies = input(f"Spesies fauna ke-{i+1}: ")
    mangrove.tambah_spesies_fauna(spesies)

# Menampilkan hasil
print("\n=== Laporan Biodiversitas Mangrove ===")
print(f"Lokasi: {mangrove.nama_lokasi}")
print(f"Status Ancaman: {mangrove.status_ancaman}")
print(f"Luas Area: {mangrove.luas_area} hektar")
print(f"Spesies Flora: {mangrove.spesies_flora}")
print(f"Spesies Fauna: {mangrove.spesies_fauna}")
print(f"Indeks Biodiversitas: {mangrove.hitung_indeks_biodiversitas()} spesies")
print(f"Potensi Karbon Diserap: {mangrove.hitung_potential_karbon()} ton")
print(f"Pesan Edukasi: {mangrove.pesan_edukasi()}")
print(f"Rekomendasi Aksi: {mangrove.rekomendasi_aksi()}")
            