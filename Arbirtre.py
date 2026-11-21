import UniteParthes
import UniteRomaine
from Unite import Unite
from Battlefield import Battlefield

class Arbirtre:
    def __init__(self,battlefield, ia_romaine, ia_parthe):
        self.battlefield = battlefield
        self.ia_romaine = ia_romaine
        self.ia_parthe = ia_parthe
        self.tour = 0
        self.temps = 0
        self.resultat = None


    def update(self, dt): # Méthode principale: fait un tour du jeu et renvoie la cond de victoire self.resultat
        if self.resultat is not None:
            return self.resultat
        self.temps += dt #Compte le temps de jeu

        #Executer pour Romains:
        if self.ia_romaine is not None:
            ordres_r = self.ia_romaine.decider(self.battlefield.get_alive_units())
            self.executer_ordres(ordres_r, "romain")

        #Executer pour Parthes:
        if self.ia_parthe is not None:
            ordres_p = self.ia_parthe.decider(self.battlefield.get_alive_units())
            self.executer_ordres(ordres_p, "parthe")

        #Processus de update et deplacement des unites
        for u in self.battlefield.get_alive_units():
            deplacement = u.update(dt)
            
            if deplacement is not None:
                dx, dy = deplacement
                arrivee = self.battlefield.deplacer_unite(u, dx, dy)

                if arrivee and u.distance_point(*u.destination) <= 0.05:
                    u.x, u.y = u.destination
                    u.destination = None


        self.tour += 1 #Compte le nb de tours complets

        self.resultat = self.verifier_victoire()
        return self.resultat

        

    def executer_ordres(self, ordres: list, team): # éxecute la liste d'ordre de l'ia [{}, {}]
        for ordre in ordres:
            unite = self.battlefield.get_unite(ordre.get("unit_id"))
            if unite is None or not unite.is_alive:
                continue

            if unite.team != team:
                continue

            type_ordre = ordre.get("type")

            if type_ordre == "move":
                destination = ordre.get("destination")
                if destination is None or len(destination) != 2:
                    continue
                x, y = destination
                if self.battlefield.est_dans_limites(x, y, unite.radius):
                    unite.destination = (x, y)

            elif type_ordre == "attack":
                cible = self.battlefield.get_unite(ordre.get("target_id"))
                if (cible is not None and cible.is_alive and cible.team != team):
                    unite.attaquer(cible)


    def verifier_victoire(self):
        """Détermine le vainqueur et le match nul."""
        return None

    
    """def partie_terminee(self): 
        romains_vivants = [ u for u in self.battlefield.get_units_by_team("romain") if u.is_alive]
        parthes_vivants = [ u for u in self.battlefield.get_units_by_team("parthe") if u.is_alive]
        if not parthes_vivants:
            return "Romains"
        if not romains_vivants:
            return "Parthes"
        return None""" # A revoir dans verifier_victoire()