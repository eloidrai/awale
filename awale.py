#!/usr/bin/env python3

from termcolor import *

print(" "*15+colored("Jeu d'awalé", "red", "on_yellow", ["bold"]))

class Partie(object):
    def __init__(self):
        self.liste = [4,4,0,0,0,0,0,0,0,0,0,0]
        self.joueur1 = True
        self.graines_joueur1 = 0
        self.graines_joueur2 = 0
    
    def fin(self):
        if self.joueur1 and sum(self.liste[6:])==0:
            for i in range(0,6):
                if self.liste[i]>5-i:
                    return False
            return True
        elif not self.joueur1 and sum(self.liste[:12])==0:
            for i in range(6,12):
                if self.liste[i]>11-i:
                    return False
            return True
        else:
            return False
    
    def coup(self, trou_depart):
        graines = self.liste[trou_depart]     # On récupère le nombre de graines dans le trou
        self.liste[trou_depart] = 0       # On vide la case que l'on choisit
        trou = trou_depart
        while graines>0:
            trou+=1
            if trou%12!=trou_depart: # Si on n'est pas au départ
                self.liste[trou%12] += 1   # On sème
                graines-=1
        prises = []                 # Liste des prises (avant de savoir si on affame)
        while (self.liste[trou%12]==2 or self.liste[trou%12]==3) and ((self.joueur1 and trou%12>5) or (not self.joueur1 and trou%12<6)):        # On calcule les prises
            prises.append(trou%12)
            trou-=1
        if ((self.joueur1 and len([i for i in self.liste[6:] if i==0])+len(prises)==6) or (not self.joueur1 and len([i for i in self.liste[:6] if i==0])+len(prises)==6)): # On ne prend rien (famine)
            pass
        else:                       # Prise(s) normale(s)
            for i in prises:
                self.liste[i] = 0
            if self.joueur1:
                self.graines_joueur1 += len(prises)
            else:
                self.graines_joueur2 += len(prises)
    
    def tour(self):
        t = int(input("Choisir un numéro de case : "))
        while not ((self.joueur1 and 0<=t<6) or (not self.joueur1 and 5<t<=11)) or self.liste[t]==0:
            t = int(input("Choisir un numéro de case %s : " %(colored("valide", on_color='on_red'))))
        self.coup(t)
        print(self.liste)
        self.joueur1 = not self.joueur1