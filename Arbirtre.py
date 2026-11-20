import UniteRomaine
import UniteParthes

class Arbirtre:
    def __init__(self,battlefield, ia_romaine = 0, ia_parthe = 0):
        self.battlefield = battlefield
        self.taille_carte = battlefield.largeur
        self.ia_romaine = ia_romaine
        self.ia_parthe = ia_parthe
        self.tour = 0
    
    
    def deplacer_unite(self, unite , dx , dy):
        nx = unite.x +dx
        ny = unite.y +dy
        if 0 <= nx < self.taille_carte and 0 <= ny < self.taille_carte:
            unite.x = nx
            unite.y = ny
            return True
        return False

    def update(self, dt): # Méthode principale: fait un tour du jeu
        ordres_r = self.ia_romaine.decider(self.battlefield.unites)
        ordres_p = self.ia_parthe.decider(self.battlefield.unites)
        ordres = ordres_p + ordres_r

        self.executer_ordres(ordres)

        for u in self.battlefield.unites:
            u.update
        


    def executer_ordres(self, ordres: list): # éxecute la liste d'ordre de l'ia [{}, {}]
        for ordre in ordres:
            unite = next((u for u in self.battlefield.unites if u.uid == ordre["unit_id"]), None)
            if unite == None or not unite.is_alive:
                continue

        if ordre["type"] == "move":
            unite.destination = ordre["dst"]
        if ordre["type"] == "attack":
            cible = next((u for u in self.battlefield.unites if u.uid == ordre["target_id"]),None)
            if cible is not None:
                unite.attaquer(cible)


    def verifier_victoire(self):
        """Détermine le vainqueur ou le match nul."""

    
    def partie_terminee(self):
        romains_vivants = [ u for u in self.battlefield.get_units_by_team("romain") if u.is_alive]
        parthes_vivants = [ u for u in self.battlefield.get_units_by_team("parthes") if u.is_alive]
        if not parthes_vivants:
            return "Romains"
        if not romains_vivants:
            return "Parthes"
        return None