from abc import ABC, abstractmethod

class Takjil(ABC):  
    @abstractmethod
    def rasa(self):
        pass
    @abstractmethod
    def bahan_utama(self):
        pass

class Kolak(Takjil):
    def rasa(self):
        return "Manis dan gurih"
    def bahan_utama(self):
        return "Pisang, santan, dan gula merah"

class EsBuah(Takjil):
    def rasa(self):
        return "Segar dan manis"
    def bahan_utama(self):
        return "Aneka buah, sirup, dan susu"

class Kurma(Takjil):
    def rasa(self):
        return "Manis alami"
    def bahan_utama(self):
        return "Buah kurma"

kolak = Kolak()
es_buah = EsBuah()
kurma = Kurma()

print(f"Kolak: Rasa {kolak.rasa()}, bahan utama: {kolak.bahan_utama()}")
print(f"Es Buah: Rasa {es_buah.rasa()}, bahan utama: {es_buah.bahan_utama()}")
print(f"Kurma: Rasa {kurma.rasa()}, bahan utama: {kurma.bahan_utama()}")
