class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor(self, nominal):
        self.saldo += nominal

    def tarik(self, nominal):
        if self.saldo >= nominal:
            self.saldo -= nominal
            return True
        return False

    def transfer(self, tujuan, nominal):
        if self.tarik(nominal):
            tujuan.setor(nominal)
            print(f"Transfer Rp {nominal:,} ke {tujuan.no_rekening} BERHASIL.")
        else:
            print("Transfer GAGAL. Saldo tidak cukup.")

    def __str__(self):
        return f"{self.nama} (Rek: {self.no_rekening}) - Saldo: Rp {self.saldo:,}"

# Contoh penggunaan
budi = Rekening("Budi", 5555, 500_000)
wati = Rekening("Wati", 6666, 2_000_000)

print("Data Awal:")
print(budi)
print(wati)

print("\nTransaksi:")
budi.transfer(wati, 250_000)

print("\nData Akhir:")
print(budi)
print(wati)
