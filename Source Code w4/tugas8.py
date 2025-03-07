class Pengajar:
    def __init__(self):
        """Constructor tanpa argumen yang menginisialisasi list matkul_diajar."""
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        """Menambahkan mata kuliah yang diajar ke dalam list matkul_diajar."""
        self.matkul_diajar.append(mata_kuliah)

    def __str__(self):
        """Mengembalikan representasi string dari objek Pengajar."""
        return f"Mata kuliah yang diajar: {', '.join(self.matkul_diajar) 
        if self.matkul_diajar 
        else 'Tidak ada mata kuliah yang diajar'}"

pengajar1 = Pengajar()
pengajar1.mengajar("Statistik")
pengajar1.mengajar("Pemrograman")

print(pengajar1)
