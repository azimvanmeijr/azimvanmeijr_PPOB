class wapres:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    @property
    def umur_gangaruh(self):
        return "LULUS" if self.umur >= 40 else "TETAP LULUS"
    
wapres1 = wapres("syahrul", 45)
wapres2 = wapres("GeebRun", 36)

print(f"{wapres1.nama}: {wapres1.umur_gangaruh}")
print(f"{wapres2.nama}: {wapres2.umur_gangaruh}")