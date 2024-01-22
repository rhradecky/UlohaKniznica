class Kniha:
    def __init__(self, nazov, autor, isbn, rok):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.rok = rok
        self.dostupna = True

    def vypozicaj(self):
            self.dostupna = False
            print("Kniha ", self.nazov, " nie je dostupna")

    def vratit(self):
            self.dostupna = True
            print("Kniha ", self.nazov, " je dostupna")




class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)
        print("Kniha ", kniha.nazov, "bola pridana do kniznice.")


    def vyhladat_podla_nazvu(self, nazov):
        for kniha in self.zoznam_knih:
            if kniha.nazov == nazov:
                return kniha
        return None


    def vyhliadat_podla_isbn(self, isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                return kniha
        return None


    def vypozicaj_knihu(self, isbn):
        for kniha in self.zoznam_knih:
            if (kniha.isbn == isbn):
                kniha.vypozicaj()


    def vratit_knihu(self, isbn):
        kniha = self.vyhliadat_podla_isbn(isbn)
        if kniha:
            kniha.vratit()
        else:
            print("Kniha s daným ISBN neexistuje.")


    def zobraz_dostupne_knihy(self):
        dostupne_knihy = [kniha for kniha in self.zoznam_knih if kniha.dostupna]
        if dostupne_knihy:
            print("Dostupné knihy:")
            for kniha in dostupne_knihy:
                print(kniha.nazov)
        else:
            print("Ziadne knihy nie su dostupne.")







kniha1 = Kniha("Harry Potter","Rowlingova",  1001, 2010)
kniha2 = Kniha("Pan Prstenov", "Tolkien", 1002, 2003)
kniha3 = Kniha("Vkladna Knizka", "Slovenska Sporitelna", 1103, 2000)



kniznica = Kniznica()
kniznica.pridaj_knihu(kniha1)
kniznica.pridaj_knihu(kniha2)
kniznica.pridaj_knihu(kniha3)
print("******************")
kniznica.vypozicaj_knihu(1001)
kniznica.zobraz_dostupne_knihy()
print("******************")
kniznica.vratit_knihu(1001)
kniznica.zobraz_dostupne_knihy()


