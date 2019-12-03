from sommetClass import SommetClass
from equipeClass import EquipeClass
from creatureClass import CreatureClass
from positionClass import PositionClass
import random
from pyspark import SparkContext, SparkConf

#Utilité : Foncion permettant de générer un nombre de lancé de dé
#           Exemple : genererLancerDe(1,8) correspondra au lancé
#           d'1d8
#
#param : nbDeLancer : nombre de lancés de dé à réaliser
#        nbFaceDe : Nombre de face sur le dé
#
#retour : tableau de lancé de dé
def genererLancerDe(nbDeLancer, nbFaceDe):
    De = []
    for nbALancer in range(0,nbDeLancer):
        print(nbALancer)
        De.append(random.randint(0,nbFaceDe))
    return De

#Utilité : Foncion somme des lancés de dé
#
#param : tab de dé
#        indice debut
#        indice fin
#
#retour : somme des faces
def sommeFaceDe(tabDe, dIndice,fIndice):
    somme=0
    for lancer in range(dIndice,fIndice):
        somme+=lancer
    return somme

#Utilité : Foncion somme des lancés de dé
#
#param : tab de dé
#
#retour : somme des faces
def sommeFaceDeTotal(tabDe):
    sommeFaceDe(tabDe,0,len(tabDe)-1)

#IA
def Creaturia():
    print("LE FUTUUUR !!")

#Utilité : Permet de choisir si on utilise un sort ou une attaque
#          sur une créature ciblée (alliée ou ennemie)

#param : creature : sommet de la créature principale
#        creatureCible : sommet de la créature cible du sort
#def ChoisirAction(creature, creatureCible):
    #Si rangeCreature > outOfRangeMob ALORS
        #SI medic nécessaire et possible ALORS
            #SORT PV
        #SINON
            #Si mana > 0 OU rangeSort > outOfRangeMob ALORS 
                #changer position
            #SINON
                #SORT
            #FIN SI
        #FIN SI
    #SINON
        #SI medic nécessaire ALORS
            #SORT PV
        #SINON
            #ATTAQUE CAC
        #FIN SI
    #FIN SI


#CODE DU JEU

CreatureA = CreatureClass("Solar", 160, 3000, 45, 4, 2, 2)
CreatureB = CreatureClass("Vilain", 45, 100, 15, 3, 1, 1)
tabA = [CreatureA]
tabB = [CreatureB,CreatureB,CreatureB,CreatureB,CreatureB]
equipeGentils = EquipeClass(tabA)
equipeMechant = EquipeClass(tabB)
listeAdj = []

i = 0
id = 0
for creatureGentil in equipeGentils.creatures:
    print(id)
    sommet = SommetClass(id, creatureGentil, PositionClass(i,0,0))
    listeAdj.append(id)
    i+=2
    id += 1 

i = 0
for creatureMechante in equipeMechant.creatures:
    print(id)
    sommet = SommetClass(id, creatureGentil, PositionClass(i,2,0))
    listeAdj.append(id)
    i+=2
    id += 1 

conf = SparkConf().setAppName("battaille").setMaster("local[2]")
sc = SparkContext(conf = conf)
sc.setLogLevel("OFF")
print(listeAdj)
b = sc.broadcast(listeAdj)
test = sc.parallelize([0,0]).flatMap(lambda x: b.value).cache()


#sc.parallelize([0,0]).flatMap(lambda x: range(1,x)).collect()
#manually remove RDD
#b.unpersist()

#broadcast (=tabmessages)

#début tour chaque créature 
#tri par clé = reduceByKey

#appliquer créature





