class Makanan:
    def deskripsi(self):
        raise NotImplementedError("Metode ini harus diimplementasikan oleh kelas turunan")

class Rendang(Makanan):
    def deskripsi(self):
        return "Rendang adalah hidangan daging yang dimasak dengan rempah-rempah khas Minangkabau."

class Gulai(Makanan):
    def deskripsi(self):
        return "Gulai adalah hidangan berkuah yang terbuat dari daging atau sayuran dengan bumbu rempah."

class Sate(Makanan):
    def deskripsi(self):
        return "Sate adalah daging yang ditusuk dan dibakar, biasanya disajikan dengan bumbu kacang."

def main():
    makanan1 = Rendang()
    makanan2 = Gulai()
    makanan3 = Sate()
    
    for makanan in (makanan1, makanan2, makanan3):
        print(f"Deskripsi hidangan: {makanan.deskripsi()}")

if __name__ == "__main__":
    main()