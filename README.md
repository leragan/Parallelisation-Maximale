# Parallelisation-Maximale
Projet L3 Python (TRAN VALENTIN, SZPUNAR BARTHELEMI)

## Les "imports" nécessaires

-threading : Pour le paralellisme 

-Digraph : Pour dessiner les graphes (arbres de taches)

-time : Pour utiliser le temps 

-statistics : Pour faire des opérations sur les listes

## Les class

### Task
Classe fourni dans le sujet qui permet de créer une tâche

- name : le nom de la tâche, unique dans un système de tâche donné ;

- reads : le domaine de lecture de la tâche ;

- writes : le domaine d’écriture de la tâche ;

- run : la fonction qui déterminera le comportement de la tâche (ici None)

### TaskSystem
Classe qui contient la liste des tâches dans tasks 
et les dépendances (les parents) des tâches dans dictionary

## Constructeur

### __init__
Constructeur qui va créer tasks et dictionary

Il permet de vérifier la validité des arguments (tasks et dictionary)

On créer une liste "names" qui va contenir tous les noms des tâches et on vérifie si chaque tâche est dans la liste,
si le nom d'une tâche est déja dans la liste "names" on renvoi une erreur sinon on la rajoute.

On parcours ensuite chaque objet dans le dictionnaire "dictionnary" et on vérifie que chaque parent d'une tâche appartient à la liste "names".

On termine par ajouter les arguments à l'instance.

## Explication des fonctions

### recdep
Fonction utilisée : append, recdep


Entrée : name, res


Sortie: Aucune



Fonction recursive qui contient l'algo pour la fonction getDependencies.

Pour chaque dépendance dans le dictionnaire, si la dépendance n'est pas dans la liste des dépendances "res", 
on l'ajoute dans la liste "res".

### getDependencies
Fonction utilisée : recdep


Entrée : name


Sortie : res



Fonction qui renvoi la liste ("res") des tâches qui doivent être executé avec une tâche donnée.

On crée la liste vide "res" qu'on va remplir avec les dépendances grâce à la fonction recdep.

### depth
Fonction utilisée : append, max

Entrée : name

Sortie : res

Fonction qui calcule la profondeur de la tâche dans l'arbre de dépendances.

On crée une liste "T" qui va contenir le nom des parents d'une tâche.

Pour chaque dépendance dans le dictionnaire de la tâche pour laquelle on a pas vu le parent avant
on ajoute le parent dans la liste "T" et on calcul ça profondeur.

On finit par renvoyer la profondeur "res".

### runSeq
Fonction utilisée : depth, append, run


Entrée : Aucune


Sortie : Aucune



Fonction qui va réaliser les taches de façon séquentielle mais sans réaliser de manière parallele celles qui peuvent l'etre.

On crée un dictionnaire "depths".

Calcul de la profondeur de chaque tâche et ajout dans le dictionnaire.

Exécutes les tâches qui sont à la même profondeur.

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


Fonction qui permet de récupérer et dessiner le graphe


### parCost 
Fonction utlisée : range, time, run, append, runSeq, mean, print


Entrée : Aucune


Sortie : Aucune


Fonction qui calcule la moyenne du temps d'éxécution du système en para et seq.


Créer 2 listes de temps pour para et seq.


Repétition de 10 fois : sauvegarde de l'heure actuel, lancement des taches en parallèles, soustraction de l'heure actuel au temps sauvegardé et ajout du résultat. De même pour le séquentiel.


Affichage des moyennes de temps d'éxécutions.



