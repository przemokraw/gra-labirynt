import pygame
from obiekty.pola.powierzchnia import Powierzchnia


class Trawa(Powierzchnia):

    def __init__(self, wiersz, kolumna):
        super().__init__(wiersz, kolumna)  # Wywołuję konstruktor klasy Powierzchnia
        self.obrazek = pygame.image.load("img/grass.png")
        self.polozenie = self.obrazek.get_rect()

        self.polozenie = self.polozenie.move([
            self.kolumna * self.polozenie.width,  # Przesuwamy pole w poziome o odpowiednią liczbę kolumn
            self.wiersz * self.polozenie.height  # Przesuwamy pole w pione o odpowiednią liczbę wierszy
        ])

    def rysuj(self, screen):
        screen.blit(self.obrazek, self.polozenie)