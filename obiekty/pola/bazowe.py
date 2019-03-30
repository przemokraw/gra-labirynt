class PoleBazowe:
    """
    To jest klasa Pola, która będzie klasą bazową dla wszystkich innych pól.
    Na przykład pole Trawa będzie podklasą klasy Powierzchnia,
    klasa Powierzchnia będzie podklasą klasy PoleBazowe.
    """

    def __init__(self, wiersz, kolumna):
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.ruch_mozliwy = False

    def rysuj(self, screen):
        """
        Metoda rysuj będzie potrzeba w każdym polu, ale na tym etapie
        nie potrafimy jej stworzyć. Dlatego piszemy specjalny
        fragment kodu, który będzie powodował błąd, gfy ktoś
        uruchomi tę metodę w klasie PoleBazowe.
        """
        raise NotImplementedError("PoleBazowe to klasa abstrakcyjna. Musz zaimplementować tę metodę w podklasach.")