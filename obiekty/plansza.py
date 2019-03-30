class Plansza:
    def __init__(self, wysokosc, szerokosc):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.plansza = []
        for _ in range(wysokosc):
            self.plansza.append([None] * szerokosc)