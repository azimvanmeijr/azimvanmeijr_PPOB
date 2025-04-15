#Khuluqin Azhim (24/535941/SV/24342)
#Program Anomali

from abc import ABC, abstractmethod

# Abstract Base Class
class Anomali(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def Panggilan(self):
        pass
    def info(self):
        return f"Saya {self.nama} dan saya dikenal dengan {self.Panggilan()}"

# Inheritance: AnomaliSahur mewarisi dari Anomali
class AnomaliSahur(Anomali):
    def __init__(self, nama):
        super().__init__(nama)
    # Polymorphism: panggilan Anomali Sahur
    def Panggilan(self):
        return "TUNG TUNG TUNG TUNG TUNG SAHUR"

# Inheritance: AnomaliHiu mewarisi Anomali
class AnomaliHiu(Anomali):
    def __init__(self, nama):
        super().__init__(nama)
    # Polymorphism: panggilan Anomali Hiu
    def Panggilan(self):
        return "TRALALELO TRALALA"

# Program utama
if __name__ == "__main__":
    # Membuat objek
    sahur = AnomaliSahur("Reza")
    hiu = AnomaliHiu("Arap")
    # daftar anomali
    anomali_kematian = [sahur, hiu]
    # Polymorphism: memanggil metode yang sama untuk objek berbeda
    print("ANOMALI TIKTOK:")
    for anomali in anomali_kematian:
        print(anomali.info())