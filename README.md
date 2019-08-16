# Jeu d'Awalé
Ce script python contient tout ce qu'il faut pour jouer au jeu d'awalé tel que décrit [ici](https://fr.wikipedia.org/wiki/Awalé).

Il est constitué des classes `Partie` et `Application`, la première gérant les données du jeu et la seconde l'interface  graphique. La classe `Partie` fournit une **API** et une méthode pour jouer en console. Il y a donc 3 manières d'utiliser ce programme : graphiquement, en console ou avec l'API.

## En mode graphique

Il n'y a presque rien à faire sinon executer le script d'une des manières suivantes :

```shell
python3 awale.py
```

```````
./awale.py
```````

Sous Windows (à condition que Python soit installé), il n'y a qu'à cliquer sur le fichier.

## En console

L'interface en console est nettement moins conviviale. If faut d'abord importer le script dans python comme suit :

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

On notera que les trous sont représentés par une une liste qui s'affiche après chaque coup. Le sens de lecture est le sens anti-horaire et la liste commence sur la première case du premier joueur.

## Avec l'API

La référence de l'API est à venir...