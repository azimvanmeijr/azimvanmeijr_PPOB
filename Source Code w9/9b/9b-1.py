from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])
titik1 = Koordinat(x=2, y=4)

#indeks elemen
print(titik1[0])

#field
print(titik1.x)

#getattr()
print(getattr(titik1, 'y'))