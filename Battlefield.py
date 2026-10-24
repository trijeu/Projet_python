from unite import Unite

class Battlefield :
    def __init__(self) :
        self.largeur= 120
        self.hauteur= 120
        self.unites= []

    def ajouter_unite(self,unite: Unite) :
        self.unites.append(unite)

    def supprimer_unite(self, unite: Unite) :
        if unite in self.unites :
            self.unites.remove(unite)


