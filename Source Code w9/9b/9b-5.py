from collections import namedtuple

MU = namedtuple("PemainMU", ["nama", "no_punggung", "posisi"])

pemain1 = MU(nama="Christiano Ronaldo", no_punggung="7", posisi="Sayap")
pemain2 = MU(nama="Wayne Rooney", no_punggung="10", posisi="Striker")
pemain3 = MU(nama="Rio Ferdinand", no_punggung="5", posisi="Bek")

daftar_pemain = [pemain1, pemain2, pemain3]

print("Daftar Pemain Manchester United:")
print("=" * 30)
for MU in daftar_pemain:
    print(f"Nama: {MU.nama}")
    print(f"No Punggung: {MU.no_punggung}")
    print(f"Posisi: {MU.posisi}")
    print("-" *30)
