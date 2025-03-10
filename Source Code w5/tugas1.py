class Transportasi:
    def berjalan(self):
        raise NotImplementedError(
            "Metode ini harus diimplementasikan oleh kelas turunan")

class Sepeda(Transportasi):
    def berjalan(self):
        return "Dikayuh"

class Skuter(Transportasi):
    def berjalan(self):
        return "Menendang tanah"

class Bus(Transportasi):
    def berjalan(self):
        return "Gas Kopling"

def main():
    # Membuat objek dari kelas Sepeda, Skuter, dan Bus
    transportasi1 = Sepeda()
    transportasi2 = Skuter()
    transportasi3 = Bus()

    # Menggunakan polimorfisme
    for transportasi in (transportasi1, transportasi2, transportasi3):
        print(f"Transportasi ini berjalan dengan cara: {transportasi.berjalan()}")

if __name__ == "__main__":
    main()