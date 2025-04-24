from collections import namedtuple

def add_method(cls):
    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak : ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")

    cls.tampilkan_info = tampilkan_info
    return cls

@add_method
class Orang(namedtuple("Orang", ["nama", "anak"] )):
    pass

john = Orang(nama = "John", anak = ["Tiny", "Jimmy", "Tina"])
john.tampilkan_info()