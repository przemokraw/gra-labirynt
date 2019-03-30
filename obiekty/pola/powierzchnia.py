from obiekty.pola.bazowe import PoleBazowe


class Powierzchnia(PoleBazowe):

    def __init__(self, wiersz, kolumna):
        super().__init__(wiersz, kolumna) # Uruchamiamy konstruktor klasy PoleBazowe
        self.ruch_mozliwy = True