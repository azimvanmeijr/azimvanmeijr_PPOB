class Karakter:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi

    def tampilkan(self):
        print(f"Saya {self.nama}. {self.deskripsi}")

class KarakterFactory:
    @staticmethod
    def buat_karakter(nama):
        karakter_data = {
            "adit": Karakter("Adit", "Anak rajin dan pintar namun senang dimanfaatkan Dennis."),
            "sopo": Karakter("Sopo", "Orang dewasa yang suka membantu dan baik hati."),
            "jarwo": Karakter("Jarwo", "Partner Sopo yang agak malas dan sering merugikan orang."),
            "dennis": Karakter("Dennis", "Teman Adit yang sangat membebani hidup adit.")
        }
        return karakter_data.get(nama.lower(), None)

# Program utama
pilihan = input("Pilih karakter (Adit, Sopo, Jarwo, Dennis): ")

karakter = KarakterFactory.buat_karakter(pilihan)
if karakter:
    karakter.tampilkan()
else:
    print("Karakter tidak dikenal!")