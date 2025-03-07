class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

    def tampilkan_info(self):
        print(f"Nama Depan: {self.nama_depan}")
        print(f"Nama Belakang: {self.nama_belakang}")
        print(f"Nomor ID: {self.nomor_id}")

orang1 = Orang("Ujang", "Kedu", "123456")
orang1.tampilkan_info()
        