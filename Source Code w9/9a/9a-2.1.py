class Anomali:
    jumlah_anomali = 0

    def __init__(self, nama):
        self.nama = nama
        Anomali.jumlah_anomali += 1

    @classmethod
    def tampilkan_jumlah(cls):
        print(f"Jumlah total anomali: {cls.jumlah_anomali}")

k1 = Anomali("PRR PRRR PATAPING")
k2 = Anomali("BOMBARDIRO CROCODILO")

Anomali.tampilkan_jumlah()
