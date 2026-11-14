from Arbirtre import Arbirtre
from SimpleIA import SimpleIA
import Battlefield
TOURS_MAX = 500

arbitre = Arbirtre()

ia_romaine = SimpleIA("Romains",arbitre.unites_romaines)
ia_parthes = SimpleIA("Parthes",arbitre.unites_Parthe)
gagnant = None
while arbitre.tour < TOURS_MAX:
    arbitre.tour += 1
    ia_parthes.jouer_tour(arbitre)
    ia_parthes.jouer_tour(arbitre)
    gagnant = arbitre.partie_terminee()
    if gagnant:
        break
if gagnant:
    print(f"Les {gagnant} gagnent au tour {arbitre.tour} !")
else:
    print(f"Match nul : aucun vainqueur après {TOURS_MAX} tours.")

