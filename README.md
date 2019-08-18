# Jeu d'Awalé
Ce script python contient tout ce qu'il faut pour jouer au jeu d'awalé tel que décrit [ici](https://fr.wikipedia.org/wiki/Awalé).

Il est constitué des classes `Partie` et `Application`, la première gérant les données du jeu et la seconde l'interface  graphique. La classe `Partie` fournit une **API** et une méthode pour jouer en console. Il y a donc 3 manières d'utiliser ce programme : graphiquement, en console ou avec l'API.

## En mode graphique

Il n'y a presque rien à faire sinon executer le script d'une des manières suivantes :

```sh
python3 awale.pyw
```

```````sh
./awale.pyw
```````

Sous Windows (à condition que Python soit installé), il n'y a qu'à cliquer sur le fichier.

## En console

L'interface en console est nettement moins conviviale et moins aboutie. Il faut renomer `awale.pyw` en `awale.py`. Puis, il faut importer le script dans python comme suit :

``````python
from awale import Partie
``````

Puis créer un instance  de `Partie`.

``````python
p = Partie()
``````

Enfin il faut executer la méthode jouer.

``````python
p.jouer()
``````

Le premier joueur est en bas et les cases sont numérotées (de 0 à 11) de la case de gauche du joueur du bas à celle de  gauche du joueur du haut.

## Avec l'API

### Commencer par instancier

Il faut commencer par instancier comme expliqué plus haut.

### Quelques attributs utiles de la classe `Partie`

* _Partie._**liste** - Contient la liste des valeurs dans les cases
* _Partie._**joueur1** - Contient un booléen indiquant si le tour en cours est celui du premier joueur ou non
* _Partie_.**score** - Liste de 2 éléments contenant le score de chaque joueur
* _Partie_.**jouables** - Tuple contenant les rangs des cases jouables
* _Partie_.**fin** - Booléen indiquant si c'est la fin
* _Partie_.**vainqueur** - Vaut `None` pendant la partie, puis prend la valeur `1` ou `2` à la fin (selon que c'est le premier ou le second joueur qui a gagné)

### La seule méthode utile de la classe `Partie`

* _Partie_.**coup(_trou_depart_)** - Cette méthode prend en argument le rang de la case à jouer et effectue toutes les opérations d'un tour (semaille, récolte, test de fin...)