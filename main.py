class Kniha:
    def __init__(self, nazov, isbn):
        self.nazov = nazov
        self.isbn = isbn
        self.dostupna = True

    def vypozicaj(self):
        self.dostupna = False

class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def vypozicaj_knihu(self, isbn_knihy):
        for kniha in self.zoznam_knih:
            if (kniha.isbn == isbn_knihy):
                kniha.vypozicaj()

