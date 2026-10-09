import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Projet Python 3a AOE")
clock = pygame.time.Clock()

game = True
#Création d'une tuile de 64x32 choix standard en vue iso

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    screen.fill("black")
    pygame.display.flip()

    clock.tick(100)
pygame.quit()