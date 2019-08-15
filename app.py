from tkinter import *

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu d'awalé")
        self.resizable(0,0)
        canvas = Canvas(self, width=555, height=350)
        plateau = Plateau(canvas)
        canvas.pack(side=LEFT, padx=3, pady=3)
        entree = Entry(self)

class Plateau(object):
    def __init__(self, canvas):
        self.canvas = canvas
        canvas.create_rectangle(0, 70, 555, 280, fill='black')
        liste_lettres1 = ["a","b","c","d","e","f"]
        liste_lettres2 = ["A","B","C","D","E","F"]
        for i in range(6):
            print(self.canvas.create_oval(i*90+15, 85, i*90+90, 160, fill='brown'))
            self.canvas.create_text(i*90+15, 85, text=liste_lettres1[i], font=('serif', 13), fill="green")
            self.canvas.create_oval(i*90+15, 190, i*90+90, 265, fill='brown')
            self.canvas.create_text(i*90+15, 190, text=liste_lettres2[i], font=('serif', 11), fill="green")
        self.canvas.create_line(10, 175, 540, 175, fill='brown')
        
    def ecrire_nombres():
        pass
    
Application().mainloop()