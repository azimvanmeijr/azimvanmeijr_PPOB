class Orang:
    def __init__(self, nama_depan, nama_belakang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}"


class Karyawan(Orang):
    TETAP = "Tetap"
    TDK_TETAP = "Tidak Tetap"

    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang)
        self.nomer_id = nomer_id
        self.status_karyawan = status_karyawan

    def __str__(self):
        return (f"Karyawan: {super().__str__()}, "
                f"Nomer ID: {self.nomer_id}, "
                f"Status: {self.status_karyawan}")


karyawan1 = Karyawan("Gus", "Akira", "001", Karyawan.TDK_TETAP)
karyawan2 = Karyawan("Harvey", "Moeis", "002", Karyawan.TETAP)

print(karyawan1)
print(karyawan2)