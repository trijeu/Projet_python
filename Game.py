import pygame
import time
import sys
def Carrhae(
        roman_ai,
        parthian_ai,
        n_legendaries = 60,
        n_cataphracts= 20,
        n_trebuchets = 3,
        roman_start_positions = "W",
        map_size=(120,120),
        headless = False,
        speed = 1,
):
    headless = False
    if not headless:
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Projet Python 3a AOE")
        clock = pygame.time.Clock()

    game = True
    #Création d'une tuile de 64x32 choix standard en vue iso

    while game:
        if not headless: #fermeture du jeu en mode non headless
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False












        screen.fill("black")
        pygame.display.flip()

        clock.tick(100)
    pygame.quit()

    def ajouter_unite(self,unite: Unite,type: str, team: str, x: int, y: int) :
            if team == "romain" :
                if type == "legionnaire" :
                    unite = UniteRomaine.Legionnaire(uid=self.id_counter, x=x, y=y)
                    self.id_counter += 1
                elif type == "trebuchet" :
                    unite = UniteRomaine.Trebuchet(uid=self.id_counter, x=x, y=y)
                    self.id_counter += 1
                else :
                    raise ValueError("Type d'unité romaine inconnu")
            elif team == "parthes" :
                if type == "archer" :
                    unite = UniteParthes.UniteArchers(uid=self.id_counter, x=x, y=y)
                    self.id_counter += 1
                elif type == "cataphract" :
                    unite = UniteParthes.UniteCataphract(uid=self.id_counter, x=x, y=y)
                    self.id_counter += 1
                else :
                    raise ValueError("Type d'unité parthe inconnu")
            else :
                raise ValueError("Équipe inconnue")
    
            self.unites.append(unite)