def tambah_pengingat_berbuka(cls):
    def pengingat_berbuka(self):
        print(f"Jangan lupa berbuka puasa tepat waktu! - Salam dari {self.__class__.__name__}.")
    
    cls.pengingat_berbuka = pengingat_berbuka
    return cls

def tambah_pengingat_sholat(cls):
    def pengingat_sholat(self):
        print(f"Jangan tinggalkan sholat meski berpuasa! - Salam dari {self.__class__.__name__}.")    
    cls.pengingat_sholat = pengingat_sholat
    return cls
@tambah_pengingat_berbuka
class TakmirMasjid:
    def __init__(self, nama):
        self.nama = nama

@tambah_pengingat_sholat
class MalaikatMalik:
    def __init__(self, nama):
        self.nama = nama
orang = TakmirMasjid("Takmir Masjid Al-Ikhlas")
adminneraka = MalaikatMalik("Malaikat Malik")

orang.pengingat_berbuka()
adminneraka.pengingat_sholat()
