class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def perkenalan(self):
        return f"Nama: {self.nama}, Usia: {self.usia}"

class Pelajar:
    def __init__(self, jurusan):
        self.jurusan = jurusan

    def info_jurusan(self):
        return f"Jurusan: {self.jurusan}"

class Pengajar:
    def __init__(self, mata_pelajaran):
        self.mata_pelajaran = mata_pelajaran

    def info_mata_pelajaran(self):
        return f"Mata Pelajaran: {self.mata_pelajaran}"

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama, usia, jurusan, mata_pelajaran):
        Orang.__init__(self, nama, usia)
        Pelajar.__init__(self, jurusan)
        Pengajar.__init__(self, mata_pelajaran)

    def info_asdos(self):
        return f"{self.perkenalan()}, {self.info_jurusan()}, {self.info_mata_pelajaran()}"

asdos1 = Asdos("Asep", 20, "Teknik Jawa", "Jawa Kuno")
print(asdos1.info_asdos())
