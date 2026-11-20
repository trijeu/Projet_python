import pygame

from Battlefield import Battlefield
from UniteRomaine import Legionnaire
from SimpleIA import SimpleIA



"""
Correctif à implémenter

Ajout d'aléatoire dans la rotation des images pour éviter que ce soit moche
"""
pygame.init()

# Paramètres fenêtre et initialisation fenêtre
W = 1280
H = 720

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Projet Python 3a AOE")
clock = pygame.time.Clock()

game = True

# Taille des tuiles
TUILE_W = 64
TUILE_H = 32

ZOOM = 1.5
ZOOM_MIN = 1.0
ZOOM_MAX = 2.0

# Taille de la carte (120 x 120)
NB_TUILES = 120

# Paramètres Caméra
OFFSET_X = W / 2
OFFSET_Y = H / 4
VITESSE_CAM = 400

# Paramètres minimap
MINI_TAILLE = 175
MINI_X = W - MINI_TAILLE - 20
MINI_Y = 20

# Application des textures d'hebre
herbe = pygame.image.load("herbe.png").convert_alpha()
herbe = pygame.transform.scale(herbe, (int(TUILE_W), int(TUILE_H)))
chateau_base = pygame.image.load("chateau.png").convert_alpha()
# Découpage en polygon
masque = pygame.Surface((int(TUILE_W), int(TUILE_H)), pygame.SRCALPHA)

pygame.draw.polygon(masque, (255, 255, 255), [
    (int(TUILE_W) // 2, 0),
    (int(TUILE_W), int(TUILE_H) // 2),
    (int(TUILE_W) // 2, int(TUILE_H)),
    (0, int(TUILE_H) // 2)
])

herbe.blit(masque, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
herbe_base = herbe.copy()

class PetitArbitre:
    def deplacer_unite(self, unite, dx, dy):
        unite.destination = (unite.x + dx, unite.y + dy)


champ_bataille = Battlefield()
champ_bataille.largeur = NB_TUILES
champ_bataille.hauteur = NB_TUILES

unite_test = Legionnaire(1, 55.0, 55.0)
champ_bataille.ajouter_unite(unite_test)

ia_test = SimpleIA("romain", {"legionnaire_1": unite_test})
arbitre_test = PetitArbitre()

intervalle_ms = 500
dernier_changement_ms = pygame.time.get_ticks()



# Conversion des coordonées de la carte vers l'écran
def convertisseur_iso(x, y):
    sx = (x - y) * TUILE_W / 2 + OFFSET_X
    sy = (x + y) * TUILE_H / 2 + OFFSET_Y

    return sx, sy


# Conversion des coordonnées de l'écran vers la carte
def convertisseur_inverse(sx, sy):
    x = (sx - OFFSET_X) / (TUILE_W / 2)
    y = (sy - OFFSET_Y) / (TUILE_H / 2)

    coord_x = (x + y) / 2
    coord_y = (y - x) / 2

    return coord_x, coord_y


# Affichage de la tuile
def creation_tuile(x, y):
    sx, sy = convertisseur_iso(x, y)

    # Positionnement de l'image
    position = (sx - TUILE_W / 2, sy - TUILE_H / 2)

    # Affichage de l'herbe sans bordure
    screen.blit(herbe, position)


def afficher_chateau():
    x, y = convertisseur_iso(NB_TUILES // 2, NB_TUILES // 2)

    largeur = max(1, int(chateau_base.get_width() * ZOOM / 2))
    hauteur = max(1, int(chateau_base.get_height() * ZOOM / 2))

    chateau = pygame.transform.scale(chateau_base, (largeur, hauteur))

    # Position du chateau
    position = (x - largeur // 2, y - hauteur)

    screen.blit(chateau, position)


def afficher_unite(unite):
    sx, sy = convertisseur_iso(unite.x, unite.y)
    rayon = max(4, int(6 * ZOOM))
    pygame.draw.circle(screen, (220, 40, 40), (int(sx), int(sy)), rayon)



mini_map = pygame.Surface((MINI_TAILLE, MINI_TAILLE), pygame.SRCALPHA)

# Fond vert pour éviter les bugs graphiques moches lors du zoom
pygame.draw.polygon(mini_map, (70, 130, 50), [
    (MINI_TAILLE // 2, 0),
    (MINI_TAILLE, MINI_TAILLE // 2),
    (MINI_TAILLE // 2, MINI_TAILLE),
    (0, MINI_TAILLE // 2)
])

# Texture d'herbe
mini_herbe = pygame.transform.scale(herbe, (16, 8))

for i in range(0, MINI_TAILLE, 8):
    for j in range(0, MINI_TAILLE, 8):
        mini_map.blit(mini_herbe, (i, j))

# Application du masque sur les polygons
mini_masque = pygame.Surface((MINI_TAILLE, MINI_TAILLE), pygame.SRCALPHA)

pygame.draw.polygon(mini_masque, (255, 255, 255), [
    (MINI_TAILLE // 2, 0),
    (MINI_TAILLE, MINI_TAILLE // 2),
    (MINI_TAILLE // 2, MINI_TAILLE),
    (0, MINI_TAILLE // 2)
])

mini_map.blit(mini_masque, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


# Conversion vers la mini-carte 2.5d
def convertisseur_mini(x, y):
    mx = MINI_TAILLE / 2 + (x - y) * MINI_TAILLE / (2 * NB_TUILES)
    my = (x + y) * MINI_TAILLE / (2 * NB_TUILES)

    return mx, my


def afficher_minimap():
    screen.blit(mini_map, (MINI_X, MINI_Y))

    # Coins de la fenêtre
    coins = [
        (0, 0),
        (W, 0),
        (W, H),
        (0, H)
    ]

    points_camera = []

    for sx, sy in coins:
        x, y = convertisseur_inverse(sx, sy)
        mx, my = convertisseur_mini(x, y)

        points_camera.append((MINI_X + mx, MINI_Y + my))

    # Zone caméra
    pygame.draw.polygon(screen, (255, 255, 255), points_camera, 2)

    # Bordure minimap
    pygame.draw.polygon(screen, (255, 255, 255), [
        (MINI_X + MINI_TAILLE / 2, MINI_Y),
        (MINI_X + MINI_TAILLE, MINI_Y + MINI_TAILLE / 2),
        (MINI_X + MINI_TAILLE / 2, MINI_Y + MINI_TAILLE),
        (MINI_X, MINI_Y + MINI_TAILLE / 2)
    ], 2)


while game:

    temps = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        # Clic gauche
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mx, my = event.pos

            # Position du clic dans la minimap
            mini_x = mx - MINI_X
            mini_y = my - MINI_Y

            # On vérifie que le clic est dans le losange
            distance = abs(mini_x - MINI_TAILLE / 2) + abs(mini_y - MINI_TAILLE / 2)

            if distance <= MINI_TAILLE / 2:

                # Conversion en coordonnées de la map
                difference = (mini_x - MINI_TAILLE / 2) * 2 * NB_TUILES / MINI_TAILLE
                somme = mini_y * 2 * NB_TUILES / MINI_TAILLE

                nouvelle_x = (difference + somme) / 2
                nouvelle_y = (somme - difference) / 2

                # La caméra se place au centre de l'endroit cliqué
                OFFSET_X = W / 2 - (nouvelle_x - nouvelle_y) * TUILE_W / 2
                OFFSET_Y = H / 2 - (nouvelle_x + nouvelle_y) * TUILE_H / 2

        # Ajout du Zoom / Dézoom et d'un système de zoom maximal et minimal sinon il y avait des bugs
        # Zoom avec la molette
        if event.type == pygame.MOUSEWHEEL:

            if event.y > 0:
                ZOOM += 0.05

            if event.y < 0:
                ZOOM -= 0.05

            # Zoom min et Max pour éviter les bugs
            if ZOOM < ZOOM_MIN:
                ZOOM = ZOOM_MIN

            if ZOOM > ZOOM_MAX:
                ZOOM = ZOOM_MAX

            # Modification de la taille des tuiles
            TUILE_W = 64 * ZOOM
            TUILE_H = 32 * ZOOM

            # Modification de la texture
            herbe = pygame.transform.scale(
                herbe_base,
                (int(TUILE_W), int(TUILE_H))
            )

    # Déplacements caméra zoom dézoom et déplacements cam
    touches = pygame.key.get_pressed()

    if touches[pygame.K_LEFT]:
        OFFSET_X += VITESSE_CAM * temps

    if touches[pygame.K_RIGHT]:
        OFFSET_X -= VITESSE_CAM * temps

    if touches[pygame.K_UP]:
        OFFSET_Y += VITESSE_CAM * temps

    if touches[pygame.K_DOWN]:
        OFFSET_Y -= VITESSE_CAM * temps

    maintenant_ms = pygame.time.get_ticks()
    if maintenant_ms - dernier_changement_ms >= intervalle_ms:
        ia_test.jouer_tour(arbitre_test)
        dernier_changement_ms = maintenant_ms

    for unite in champ_bataille.get_alive_units():
        unite.update(temps)


    # Affichage
    screen.fill("black")

    for i in range(NB_TUILES):
        for j in range(NB_TUILES):

            sx, sy = convertisseur_iso(i, j)

            # On affiche uniquement les tuiles visibles
            if -TUILE_W < sx < W + TUILE_W and -TUILE_H < sy < H + TUILE_H:
                creation_tuile(i, j)

    afficher_chateau()


    for unite in champ_bataille.get_alive_units():
        afficher_unite(unite)


    afficher_minimap()

    pygame.display.flip()


pygame.quit()