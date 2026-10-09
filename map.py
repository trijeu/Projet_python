import pygame

pygame.init()
#Taille de la fenêtre
W = 1280
H = 720
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Projet Python 3a AOE")
clock = pygame.time.Clock()

game = True
#Création d'une tuile de 64x32 choix standard en vue iso
TUILE_W = 64
TUILE_H = 32

#Paramètres caméra
OFFSET_X = W / 2
OFFSET_Y = H / 2

def convertisseur_iso(x, y):
    affichagex = (x - y) * TUILE_W / 2 + OFFSET_X
    affichagey = (x + y) * TUILE_H / 2 + OFFSET_Y
    return affichagex, affichagey

def creation_tuile(x, y):
    ax, ay = convertisseur_iso(x, y)
    points = [
        (ax,ay - TUILE_H / 2),
        (ax + TUILE_W / 2, ay),
        (ax, ay + TUILE_H /2),
        (ax -TUILE_W /2, ay)
    ]
    pygame.draw.polygon(screen, (0, 0, 255), points)
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    screen.fill("black")
    pygame.display.flip()

    clock.tick(100)
pygame.quit()