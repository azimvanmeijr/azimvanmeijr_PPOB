class Angka:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __add__(self, other):
        return Angka(self.nilai + other.nilai)
    
    def __sub__(self, other):
        return Angka(self.nilai - other.nilai)
    
    def __mul__(self, other):
        return Angka(self.nilai * other.nilai)
    
    def __str__(self):
        return str(self.nilai)

a = Angka(10)
b = Angka(5)

c = a + b
d = a - b
e = a * b

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {c}")
print(f"a - b = {d}")
print(f"a * b = {e}")