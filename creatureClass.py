from sortClass import SortClass
from armeClass import ArmeClass

class CreatureClass:
    def __init__(self, nom, armure, pv, regeneration, vitesse, armes, sorts):
        self.nom = nom
        self.armure = armure
        self.pv = pv
        self.regeneration = regeneration
        self.vitesse = vitesse
        self.armes = armes
        self.sorts = sorts
        
    #Getteur nom créature
    def get_nom(self):
        return self.nom

    #Setteur nom créature
    def set_nom(self, nomAChoisir):
        self.nom = nomAChoisir   

    #Getteur armure créature
    def get_armure(self):
        return self.nom

    #Setteur armure créature
    def set_armure(self, armureCreature):
        self.armure = armureCreature   
        
    #Getteur pv créature
    def get_pv(self):
        return self.pv

    #Setteur pv créature
    def set_pv(self, nouveauPV):
        self.pv = nouveauPV

    #Getteur regeneration créature
    def get_regeneration(self):
        return self.regeneration

    #Setteur regeneration créature
    def set_regeneration(self, regenerationPV):
        self.regeneration = regenerationPV

    #Getteur vitesse créature
    def get_vitesse(self):
        return self.vitesse

    #Setteur vitesse créature
    def set_vitesse(self, vitesseCreature):
        self.vitesse = vitesseCreature
        
    #Getteur armes créature
    def get_armes(self):
        return self.armes

    #Setteur armes créature
    def add_armes(self, arme):
        self.armes.append(arme)

    #Getteur sorts créature
    def get_sorts(self):
        return self.sorts

    #Setteur vitesse créature
    def add_sorts(self, sort):
        self.sorts.append(sort)