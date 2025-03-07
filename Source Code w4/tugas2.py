class Orang:
    def __init__(self, namadepan, namabelakang, nomer_id):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print(f"Nama: {self.namadepan} {self.namabelakang}")
        print(f"Nomer ID: {self.nomer_id}")


class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"

    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matakuliah):
        self.matkul.append(matakuliah)

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenjang: {self.jenjang}")
        print(f"Mata Kuliah: {', '.join(self.matkul) if self.matkul else 'Belum mengambil mata kuliah'}")


# Contoh penggunaan
mahasiswa1 = Mahasiswa(Mahasiswa.SARJANA, "Rahmat", "Knalpot", "987456")
mahasiswa1.enrol("Matek")
mahasiswa1.tampilkan_info()