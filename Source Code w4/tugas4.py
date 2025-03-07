class Karyawan:
    def __init__(self, nama, nip, usia, jabatan):
        self.nama = nama
        self.nip = nip
        self.usia = usia
        self.jabatan = jabatan

    def info_karyawan(self):
        return f"Nama: {self.nama}, NIP: {self.nip}, Usia: {self.usia}, Jabatan: {self.jabatan}"

class Dosen(Karyawan):
    def __init__(self, nama, nip, usia, jabatan):
        super().__init__(nama, nip, usia, jabatan)
        self.matkul_diajar = [] 
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
        return f"{self.nama} sekarang mengajar mata kuliah: {mata_kuliah}"

    def daftar_matkul_diajar(self):
        return f"Mata kuliah yang diajar oleh {self.nama}: {', '.join(self.matkul_diajar)}"

dosen1 = Dosen("Dr. Gadungan", "464646", 57, "Dosen Tetap")
print(dosen1.info_karyawan())
print(dosen1.mengajar("Sastra Mesin"))
print(dosen1.mengajar("Pemrograman Motor"))
print(dosen1.daftar_matkul_diajar())
