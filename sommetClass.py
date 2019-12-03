from positionClass import PositionClass
from creatureClass import CreatureClass

class SommetClass:
    def __init__(self, id, creature, position):
        self.id = id
        self.creature = creature
        self.position = position

    def toString(self):
        return "id : " + self.id + "Nom : " + self.creature.nom + " position : (" + self.position.x + "," + self.position.y + "," + self.position.z + ")"