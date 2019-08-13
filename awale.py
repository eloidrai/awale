#!/usr/bin/env python3

from termcolor import *

print(" "*15+colored("Jeu d'awalé", "red", "on_yellow", ["bold"]))

class Partie:
    def __init__(self):
        self.liste = [4,4,4,1,1,1,1,4,4,4,4,4]
        self.joueur1 = True
    
    def coup(self, lettre):
        r = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "f":6, "e":7, "d":8, "c":9, "b":10, "a":11}[lettre]      # On associe à la lettre son rang
        graines = self.liste[r]     # On récupère le nombre de graines dans le trou
        self.liste[r] = 0       # On vide la case que l'on choisit
        for i in range(r+1, r+graines+1):
            self.liste[i%12] += 1   # On sème
        prises = []                 # Liste des prises (avant de savoir si on affame)
        while (self.liste[i%12]==2 or self.liste[i%12]==3) and ((self.joueur1 and i%12>5) or (not self.joueur1 and i%12<6)):        # On calcule les prises
            prises.append(i%12)
            i-=1
        if (self.joueur1 and len([i for i in self.liste[6:] if i==0])+len(prises)==6) or (not self.joueur1 and len([i for i in self.liste[:6] if i==0])+len(prises)==6):    # On affamerait
            pass
        else:                       # Prise(s) normale(s)
            for i in prises:
                self.liste[i] = 0
        return self.liste
        
#    def tour(self):
#        self.coup(input("Quelle case jouez-vous ?"))
#        self.joueur1 = !self.joueur1
        