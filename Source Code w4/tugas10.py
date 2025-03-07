class Orang:
    def __init__(self, nama_depan, nama_belakang, usia):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.usia = usia

    def perkenalan(self):
        return f"Nama: {self.nama_depan} {self.nama_belakang}, Usia: {self.usia}"

class Pelajar:
    def __init__(self, jurusan):
        self.jurusan = jurusan

    def info_jurusan(self):
        return f"Jurusan: {self.jurusan}"

    def enrol(self, mata_kuliah):
        self.mata_kuliah = mata_kuliah
        return f"{self.nama_depan} telah mendaftar di mata kuliah: {self.mata_kuliah}"

class Pengajar:
    def __init__(self, mata_pelajaran):
        self.mata_pelajaran = mata_pelajaran

    def info_mata_pelajaran(self):
        return f"Mata Pelajaran: {self.mata_pelajaran}"

    def mengajar(self, mata_kuliah):
        return f"{self.nama_depan} sedang mengajar mata kuliah: {mata_kuliah}"

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, usia, jurusan, mata_pelajaran):
        Orang.__init__(self, nama_depan, nama_belakang, usia)
        Pelajar.__init__(self, jurusan)
        Pengajar.__init__(self, mata_pelajaran)

    def info_asdos(self):
        return f"{self.perkenalan()}, {self.info_jurusan()}, {self.info_mata_pelajaran()}"

uswatun = Asdos("Uswatun", "Hasanah", 21, "Teknik Informatika", "Kecerdasan Artifisial")
print(uswatun.enrol("Big Data"))
print(uswatun.mengajar("Kecerdasan Artifisial"))
