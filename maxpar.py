import threading
from graphviz import Digraph
import time
import statistics

# Fourni dans le sujet
class Task:
    name = ""
    reads = []
    writes = []
    run = None

class TaskSystem:
    # Contient la liste des tâches à effectuer
    global tasks
    tasks = []
    # Contient les dépendences des tâches
    global dictionary
    dictionary = {}

    # Constructeur de la classe
    def __init__(self, _tasks, _dictionary):

        #Vérification de la validité des arguments (2.4)
        names = []
        for task in _tasks:
            if task.name in names:
                print("Il y a des tâches au nom dupliqué")
                return None
            else:
                names.append(task.name)

        for item in _dictionary:
            for parent in _dictionary[item]:
                if not (parent in names):
                    print("la liste de précédence contient le nom d'une tâche inexistente")

        # Ajout des arguments à l'instance
        self.tasks = _tasks
        self.dictionary = _dictionary

    # Fonction recursive qui contient l'algo pour la fonction getDependencies
    def recdep(self, name, res):
        for dep in self.dictionary[name]:
            if not dep in res:
                res.append(dep)
                self.recdep(dep, res)


    def getDependencies(self, name):
        res = []
        self.recdep(name, res)
        return res
    
    # Fonction supplémentaire qui calcule la profondeur de la tâche dans l'arbre de dépendances
    def depth(self, name):
        res = 0
        T = []
        depth = 0
        for dep in self.dictionary[name]:
            if not dep in T:
                T.append(dep)
                res = max(res, 1 + self.depth(dep))
        return res
    
    def runSeq(self):
        # Un dictionnaire qui va contenir des listes de tâches.
        # La clé de la liste correspond à sa profondeur.
        depths = {}
        # On parcourt chaque tâche pour calculer sa profondeur et la mettre au bon endroit dans le dictionnaire.
        for task in self.tasks:
            depth = self.depth(task.name)
            if (not depth in depths):
                depths[depth] = []
            depths[depth].append(task)
        for depth in depths:
            for task in depths[depth]:
                task.run()

    def run(self):
        depths = {}
        for task in self.tasks:
            depth = self.depth(task.name)
            if (not depth in depths):
                depths[depth] = []
            depths[depth].append(task)
        for depth in depths:
            ps = []
            for task in depths[depth]:
                if __name__ == '__main__' : 
                    p = threading.Thread(target=task.run)
                    ps.append(p)
                    p.start()
            for p in ps:
                p.join()


    # Cette fonction construit le graph de dépendances du systeme. Est appelé par draw().
    def getTree(self):
        graph = Digraph(name='tree', graph_attr={'rankdir':'TB'}, format='png')
        for task in self.tasks:
            graph.node(task.name, task.name, shape='circle')
        for task in self.dictionary:
            for edge in self.dictionary[task]:
                graph.edge(edge, task)
        return graph

    # Dessine le graph de dépendances du systeme.
    def draw(self):
        graph = self.getTree()
        graph.render('tree', view=True)

    # Cette fonction donne la moyenne du temps d'execution du systeme en parallele et en sequentiel.
    def parCost(self):
        par = []
        seq = []
        for count in range(10):
            startTime = time.time()
            self.run()
            par.append(time.time() - startTime)
            startTime = time.time()
            self.runSeq()
            seq.append(time.time() - startTime)
        print("En moyenne, sur 10 essais, le systme s'execute durant ", statistics.mean(seq), " en séquentiel, tandis qu'il s'execute durant ", statistics.mean(par), " en parallele.")
            
            
    


#-----------------------Test---------------------------#

X = None
Y = None
Z = None

def runT1():
    global X
    X = 60

def runT2():
    global Y
    Y = 40

def runTsomme():
    global X, Y, Z
    Z = X + Y
    print(Z)

t1 = Task()
t1.name = "T1"
t1.writes = ["X"]
t1.run = runT1
t2 = Task()
t2.name = "T2"
t2.writes = ["Y"]
t2.run = runT2
tSomme = Task()
tSomme.name = "somme"
tSomme.reads = ["X", "Y"]
tSomme.writes = ["Z"]
tSomme.run = runTsomme

s1 = TaskSystem([t1, t2, tSomme], {"T1": [], "T2": ["T1"], "somme": ["T1", "T2"]})

s1.run()
s1.draw()
s1.parCost()
