from creatureClass import CreatureClass

class EquipeClass:
    def __init__(self, creatures):
        self.creatures = creatures

    def nombreCreatureVivantesRestantes(self):
        sommeCreatures = 0
        for creature in self.creatures:
            if creature.pv > 0 :
                sommeCreatures+=1
        return sommeCreatures

    def nombreCreaturesMorte(self):
        return self.creatures.count - self.nombreCreatureVivantesRestantes()

    def addCreature(self,creature):
        self.creatures.append(creature)

    def removeCreature(self,creature):
        self.creatures.remove(creature)



                