class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def __init__(self, nama, no_rekening, saldo):
        # Memanggil konstruktor
        super().__init__(nama, no_rekening, saldo)
    
    def data_nasabah(self):
        print(f"Nama Nasabah: {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo: Rp {self.saldo:,.2f}")

# Membuat objek
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

# Memanggil method
print("Data Nasabah Bank:")
nasabah1.data_nasabah()
nasabah2.data_nasabah()