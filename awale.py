#!/usr/bin/env python3

class Partie(object):
    def __init__(self):
        self.liste = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.joueur1 = True
        self.fin = False
        self.graines_joueur1 = 0
        self.graines_joueur2 = 0
    
    @property
    def jouables(self):
        j = tuple(i for i in list(range(0,6) if self.joueur1 else range(6,12)) if self.liste[i]!=0)
        if self.joueur1 and sum(self.liste[6:])==0:
            return tuple(i for i in j if self.liste[i]>5-i)
        elif not self.joueur1 and sum(self.liste[:6])==0:
            return tuple(i for i in j if self.liste[i]>11-i)
        else:
            return j
    
    def coup(self, trou_depart):
        graines = self.liste[trou_depart]
        self.liste[trou_depart] = 0
        trou = trou_depart
        while graines>0:
            trou+=1
            if trou%12!=trou_depart:
                self.liste[trou%12] += 1
                graines-=1
        prises = []
        while (self.liste[trou%12]==2 or self.liste[trou%12]==3) and ((self.joueur1 and trou%12>5) or (not self.joueur1 and trou%12<6)):
            prises.append(trou%12)
            trou-=1
        self.gain = len(prises)
        if ((self.joueur1 and len([i for i in self.liste[6:] if i==0])+self.gain==6) or (not self.joueur1 and len([i for i in self.liste[:6] if i==0])+self.gain==6)):
            pass
        else:
            for i in prises:
                self.liste[i] = 0
            if self.joueur1:
                self.graines_joueur1 += self.gain
            else:
                self.graines_joueur2 += self.gain
    
    def tour(self):
        print("--Joueur n°1 (%s pts)--" %self.graines_joueur1 if self.joueur1 else "--Joueur n°2 (%s pts)--" %self.graines_joueur2)
        t = int(input("Choisissez un nombre %s : " %str(self.jouables)))
        self.coup(t)
        print(self.liste)
        if self.gain!=0:
            print("+1 point" if self.gain==1 else "+ %s points" %str(self.gain))
        self.joueur1 = not self.joueur1
        if self.jouables==():
            if self.joueur1:
                self.graines_joueur1+=sum(self.liste)
            else:
                self.graines_joueur2+=sum(self.liste)
            self.fin = True
            print("Partie terminée.")
            print("Le joueur n° %s a gagné." %("1" if self.graines_joueur1>self.graines_joueur2 else "2"))

p = Partie()
while not p.fin:
    p.tour()
