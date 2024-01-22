class Kniha:
    def __init__(self, nazov, autor, isbn, rok):
        self.nazov = nazov
        self.nazov = autor
        self.isbn = isbn
        self.rok = rok
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




kniha1 = Kniha("Harry Potter","Rowlingova",  1, 2010)
kniha2 = Kniha("Pan Prstenov", "Tolkien", 10, 2003)
kniha3 = Kniha("Vkladna Knizka", "Slovenska Sporitelna", 11, 2000)




kniznica = Kniznica()
kniznica.pridaj_knihu(kniha1)
kniznica.pridaj_knihu(kniha2)



print(kniha1)
print(kniha2)

