class Karyawan:
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id
        self.status_karyawan = status_karyawan

    def __str__(self):
        return (f"Karyawan: {self.nama_depan} {self.nama_belakang}, "
                f"Nomer ID: {self.nomer_id}, "
                f"Status: {self.status_karyawan}")


class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        """Menambahkan mata kuliah yang diajar ke dalam list matkul_diajar."""
        self.matkul_diajar.append(mata_kuliah)

    def __str__(self):
        matkul = ', '.join(self.matkul_diajar) if self.matkul_diajar else "Tidak ada mata kuliah yang diajar"
        return (f"Dosen: {self.nama_depan} {self.nama_belakang}, "
                f"Nomer ID: {self.nomer_id}, "
                f"Status: {self.status_karyawan}, "
                f"Mata Kuliah: {matkul}")


rizki = Dosen("Rizki", "Setiabudi", "456789", Dosen.TETAP)
rizki.mengajar("Statistik")
print(rizki)
