class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo
    
    def setor_tunai(self, nominal):
        self.saldo += nominal
        print(f"{self.nama} setor tunai Rp {nominal:,}")
    
    def tarik_tunai(self, nominal):
        if self.saldo >= nominal:
            self.saldo -= nominal
            print(f"{self.nama} tarik tunai Rp {nominal:,}")
        else:
            print(f"{self.nama} gagal tarik tunai. Saldo tidak cukup.")

class Nasabah(Rekening):
    def __init__(self, nama, no_rekening, saldo):
        super().__init__(nama, no_rekening, saldo)
    
    def data_nasabah(self):
        print(f"Nama: {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo: Rp {self.saldo:,}")

#membuat objek
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

#data awal
print("DATA AWAL:")
nasabah1.data_nasabah()
nasabah2.data_nasabah()
#transaksi
print("\nTRANSAKSI:")
nasabah1.setor_tunai(1000000)
nasabah2.tarik_tunai(1000000)
#data setelah transaksi
print("\nDATA SETELAH TRANSAKSI:")
nasabah1.data_nasabah()
nasabah2.data_nasabah()