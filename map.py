import pygame

""" 
TRAVAIL VACANCES OCTOBRE

Changer les tiles pour ajouter une texture -> changer la création de Tiles
Ajouter un système de Zoom Dezoom 
Minimap, event ('onmouse click --> change coordonnées de la caméra avec celle clique sur la minimap')
Ajout unité qui avance de manière random

"""


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
OFFSET_Y = H /4
VITESSE_CAM = 10

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
    pygame.draw.polygon(screen, (50, 105, 19), points)
    #Pour séparer les tuiles
    pygame.draw.polygon(screen, (0, 0, 0), points, 1)
while game:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    eventpress = pygame.key.get_pressed()
    if eventpress[pygame.K_LEFT]:
        OFFSET_X += VITESSE_CAM
    if eventpress[pygame.K_RIGHT]:
        OFFSET_X -= VITESSE_CAM
    if eventpress[pygame.K_UP]:
        OFFSET_Y += VITESSE_CAM
    if eventpress[pygame.K_DOWN]:
        OFFSET_Y -= VITESSE_CAM
    for i in range(120):
        for j in range(120):
            creation_tuile(i, j)


    pygame.display.flip()

    clock.tick(100)
pygame.quit()