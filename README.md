# Parallelisation-Maximale
Projet L3 Python (TRAN VALENTIN, SZPUNAR BARTHELEMI)

## Explication des fonctions

### run
Fonction utlisée : depth, append, start, join


Entrée : Aucune


Sortie : Aucune



Fonction qui permet d'éxécuter les tâches en même temps à une même profondeur.


Créaction d'un dictionnaire depths contenant la profondeur de chaque tache.


Calcul de la profondeur de chaque tache et ajout dans le dictionnaire.


Executes les taches qui sont à la même profondeur.


### getTree
Fonction utilisée :  node, edge


Entrée : Aucune


Sortie : graph


Fonction qui définit les propriétés du graphe.


Définition du sens du graphe en TB et format png.


Création d'un noeud à chaque tâche et liaison entre le parent de chaque tâche.


### draw
Fonction utilisée : getTree, render


Entreé : Aucune


Sortie : Aucune


Fonction qui permet de récupérer et déssiner le graphe


### parCost 
Entrée : Aucune


Sortie : Aucune


Fonction qui calcule la moyenne du tems d'éxécution du système en para et seq.


Créer 2 listes de temps pour para et seq.


Repétition de 10 fois : sauvegarde de l'heure actuel, lancement des taches en parallèles, soustraction de l'heure actuel au temps sauvegardé et ajout du résultat. De même pour le séquentiel.


Affichage des moyennes de temps d'éxécutions.



