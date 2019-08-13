#!/usr/bin/env python3

from termcolor import *

print(" "*15+colored("Jeu d'awalé", "red", "on_yellow", ["bold"]))

class Partie:
    def __init__(self):
        self.liste = [4,4,4,1,1,1,1,4,4,4,4,4]
        self.joueur1 = True
        self.graines_joueur1 = 0
        self.graines_joueur2 = 0
    
    def coup(self, lettre):
        r = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "f":6, "e":7, "d":8, "c":9, "b":10, "a":11}[lettre]      # On associe à la lettre son rang
        graines = self.liste[r]     # On récupère le nombre de graines dans le trou
        self.liste[r] = 0       # On vide la case que l'on choisit
        i = r
        while graines>0:
            i+=1
            if i%12!=r: # Si on n'est pas au départ
                self.liste[i%12] += 1   # On sème
                graines-=1
        prises = []                 # Liste des prises (avant de savoir si on affame)
        while (self.liste[i%12]==2 or self.liste[i%12]==3) and ((self.joueur1 and i%12>5) or (not self.joueur1 and i%12<6)):        # On calcule les prises
            prises.append(i%12)
            i-=1
        if ((self.joueur1 and len([i for i in self.liste[6:] if i==0])+len(prises)==6) or (not self.joueur1 and len([i for i in self.liste[:6] if i==0])+len(prises)==6)) or len(prises)==0: #On ne prend rien
            pass
        else:                       # Prise(s) normale(s)
            for i in prises:
                self.liste[i] = 0
            if self.joueur1:
                self.graines_joueur1 += len(prises)
            else:
                self.graines_joueur2 += len(prises)
        
#    def tour(self):
#        self.coup(input("Quelle case jouez-vous ?"))
#        self.joueur1 = !self.joueur1