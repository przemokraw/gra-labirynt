import sys, pygame
from obiekty.pola.trawa import Trawa


pygame.init()

wiersze, kolumny = 5, 10
rozmiar_pola = 32
size = width, height = kolumny * rozmiar_pola, wiersze * rozmiar_pola
black = 0, 0, 0  # RGB

screen = pygame.display.set_mode(size)

pole1 = Trawa(0, 0)
pole2 = Trawa(3, 4)
pole3 = Trawa(4, 5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    """
    pressed = pygame.key.get_pressed() 
    if pressed[pygame.K_UP] and ballrect.top > 0 and not czy_dotyka_od_dołu(ballrect, obstaclerect):
        ballrect = ballrect.move([0, -step])
    if pressed[pygame.K_DOWN] and ballrect.bottom < height:
        ballrect = ballrect.move([0, step])
    if pressed[pygame.K_LEFT] and ballrect.left > 0:
        ballrect = ballrect.move([-step, 0])
    if pressed[pygame.K_RIGHT] and ballrect.right < width:
        ballrect = ballrect.move([step, 0])
    """
    screen.fill(black)
    pole1.rysuj(screen)
    pole2.rysuj(screen)
    pole3.rysuj(screen)
    pygame.display.flip()