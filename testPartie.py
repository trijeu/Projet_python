from Arbirtre import Arbirtre
from SimpleIA import SimpleIA
import Battlefield
from UniteParthes import UniteArchers
from UniteRomaine import Legionnaire

TOURS_MAX = 500
battlefield = Battlefield.Battlefield()
battlefield.ajouter_unite(Legionnaire(uid=1,x=10,y=10))
battlefield.ajouter_unite(UniteArchers(uid=0,x=20,y=20))
arbitre = Arbirtre(battlefield = battlefield)

ia_romaine = SimpleIA("romain")
ia_parthes = SimpleIA("parthe")
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

