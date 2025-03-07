class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomer_id}"


class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "Master"
    DOKTOR = "Doktor"

    def __init__(self, nama_depan, nama_belakang, nomer_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        """Menambahkan mata kuliah yang diambil."""
        self.matkul.append(mata_kuliah)

    def __str__(self):
        matkul = ', '.join(self.matkul) if self.matkul else "Tidak ada mata kuliah yang diambil"
        return f"{super().__str__()}, Jenjang: {self.jenjang}, Mata Kuliah: {matkul}"


bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")
print(bowo)
