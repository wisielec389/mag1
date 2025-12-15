class Towar:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def __str__(self):
        return f"{self.nazwa} | Cena: {self.cena} PLN | Ilość: {self.ilosc}"

class Magazyn:
    def __init__(self):
        self.towary = {}

    def dodaj_towar(self, towar: Towar):
        if towar.nazwa in self.towary:
            self.towary[towar.nazwa].ilosc += towar.ilosc
        else:
            self.towary[towar.nazwa] = towar

    def usun_towar(self, nazwa, ilosc):
        if nazwa in self.towary:
            if self.towary[nazwa].ilosc >= ilosc:
                self.towary[nazwa].ilosc -= ilosc
                if self.towary[nazwa].ilosc == 0:
                    del self.towary[nazwa]
            else:
                print(f"Nie ma wystarczającej ilości {nazwa} w magazynie!")
        else:
            print(f"Towar o nazwie {nazwa} nie istnieje w magazynie!")

    def wyswietl_magazyn(self):
        if not self.towary:
            print("Magazyn jest pusty!")
        else:
            for towar in self.towary.values():
                print(towar)

def menu():
    magazyn = Magazyn()

    while True:
        print("\n--- MENU ---")
        print("1. Dodaj towar")
        print("2. Usuń towar")
        print("3. Wyświetl magazyn")
        print("4. Zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę towaru: ")
            cena = float(input("Podaj cenę towaru: "))
            ilosc = int(input("Podaj ilość towaru: "))
            towar = Towar(nazwa, cena, ilosc)
            magazyn.dodaj_towar(towar)
            print(f"Dodano {towar.nazwa} do magazynu.")

        elif wybor == "2":
            nazwa = input("Podaj nazwę towaru do usunięcia: ")
            ilosc = int(input("Podaj ilość do usunięcia: "))
            magazyn.usun_towar(nazwa, ilosc)

        elif wybor == "3":
            magazyn.wyswietl_magazyn()

        elif wybor == "4":
            print("Zakończono program.")
            break

        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    menu()
