from tkinter import *
from awale import *

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu d'awalé")
        self.resizable(0,0)
        barre_menu = Menu(self)        # Menus
        menu_jeu = Menu(barre_menu, tearoff=0)
        barre_menu.add_cascade(label="Jeu", menu=menu_jeu)
        menu_jeu.add_command(label="Commencer une partie", command=self.debut_jeu)
        menu_jeu.add_separator()
        menu_jeu.add_command(label="Quitter", command=self.destroy)
        self.config(menu=barre_menu)
        self.canvas = Canvas(self, width=555, height=350)   # Grand canvas et plateau
        self.canvas.pack(side=LEFT, padx=3, pady=3)
        self.plateau = Plateau(self.canvas)
        self.zone = Frame(self)             # Cadre
        self.joueur = Canvas(self.zone, width=160, height=30, bg='yellow')  # Joueur
        self.joueur.pack()
        self.id_joueur = None
        self.entree = Entry(self.zone)      # Entrée
        self.entree.pack()
        self.correctif = Canvas(self.zone, width=160, height=20)   # Correctif
        self.correctif.pack()
        self.id_correctif = None
        btn = Button(self.zone, text="Valider", bg='grey', command=self.jouer) # Bouton
        btn.pack()
        
    def debut_jeu(self):
        self.p = Partie()
        self.plateau.ecrire_nombres(self.p.liste)
        self.plateau.ecrire_scores((self.p.graines_joueur1, self.p.graines_joueur2))
        self.zone.pack(side=RIGHT, padx=3)
        self.affiche_joueur()
        
    def jouer(self):
        try:
            t = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"f":6,"e":7,"d":8,"c":9,"b":10,"a":11}[self.entree.get()]
        except:
            self.correcteur("Mauvaise saisie")
            return None
        finally:
            self.entree.delete(0)
        if not t in self.p.jouables:
            self.correcteur("Tu ne peux pas jouer cela.")
            return None
        else:
            self.correcteur("")
            self.p.coup(t)
            self.p.joueur1 = not self.p.joueur1
            if self.p.jouables==():       # Fin (car le joueur ne peut plus nourrir son adversaire)
                if self.p.joueur1:
                    self.p.graines_joueur1+=sum(self.p.liste)
                else:
                    self.p.graines_joueur2+=sum(self.p.liste)
                self.p.liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.plateau.ecrire_scores((self.p.graines_joueur1, self.p.graines_joueur2))
            self.plateau.ecrire_nombres(self.p.liste)
            self.affiche_joueur()
            
            
    
    def affiche_joueur(self):
        if self.id_joueur!=None:
            self.joueur.delete(self.id_joueur)
        self.id_joueur = self.joueur.create_text(80, 15, text=("Joueur n°1" if self.p.joueur1 else "Joueur n°2"), font=('Arial', 15))

    def correcteur(self, message):
        if self.id_correctif!=None:
            self.correctif.delete(self.id_correctif)
        self.id_correctif = self.correctif.create_text(80, 10, text=message, font=('Courrier', 8), fill='red')

class Plateau(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.ids_nombres = []
        self.ids_joueurs = []
        canvas.create_rectangle(0, 70, 555, 280, fill='black')
        liste_lettres1 = ["a","b","c","d","e","f"]
        liste_lettres2 = ["A","B","C","D","E","F"]
        
        for i in range(6):
            self.canvas.create_oval(i*90+15, 85, i*90+90, 160, fill='brown')
            self.canvas.create_text(i*90+15, 85, text=liste_lettres1[i], font=('serif', 13), fill='green')
            self.canvas.create_oval(i*90+15, 190, i*90+90, 265, fill='brown')
            self.canvas.create_text(i*90+15, 190, text=liste_lettres2[i], font=('serif', 11), fill='green')
        self.canvas.create_line(10, 175, 540, 175, fill='brown')
        
    def ecrire_nombres(self, liste):
        for i in self.ids_nombres:
            self.canvas.delete(i)
        self.ids_nombres = []
        for i in range(6):
            self.ids_nombres.append(self.canvas.create_text(i*90+50, 225, text=str(liste[i]), fill='blue', font=('Arial',28,'bold')))
        for i in range(6):
            self.ids_nombres.append(self.canvas.create_text(555-(i*90+50), 120, text=str(liste[6+i]), fill='blue', font=('Arial',28,'bold')))
    
    def ecrire_scores(self, scores):
        for i in self.ids_joueurs:
            self.canvas.delete(i)
        self.ids_joueurs = []
        self.ids_joueurs.append(self.canvas.create_text(555/2, 315, text="Joueur n°1 (%s)" %(str(scores[0])+(" pts." if scores[0]>=2 else " pt.")), font=('Helvetica', 20)))
        self.ids_joueurs.append(self.canvas.create_text(555/2, 35, text="Joueur n°2 (%s)" %(str(scores[1])+(" pts." if scores[1]>=2 else " pt.")), font=('Helvetica', 20)))

Application().mainloop()