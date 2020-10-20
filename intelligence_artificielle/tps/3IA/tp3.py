#Implémentation de l'algorithme Best first first

class Graphe():

    def __init__(self, sommets, arcs):
        #code
        self.sommets= sommets
        self.arcs= arcs

    def getVoisins(self, sommet):
        voisins= []
        for arc in self.arcs:
            if arc[0] == sommet:
                voisins.append([arc[1], arc[2]])
        return voisins.copy()

    def getSommets(self):
        return self.sommets

    def getArcs(self): #renvoie un couple [sommet, cout]
        return self.arcs

def f(arcs):
    if len(arcs) > 0:
        arcChoisi= arcs[0][0]
        minimum= arcs[0][1]
        #trouver le minimum
        for arc in arcs:
            if arc[1] < minimum:
                arcChoisi= arc[0]
                minimum= arc[1]
    else:
        arcChoisi= "Null"
    return arcChoisi
            
         
    
s= "S,A,F,C,D,G,H".split(",")
a= [["S","A", 2], ["A","C", 4], ["C", "D", 3], ["D", "G", 3], ["C", "G", 5], ["S", "F", 7], ["F","A", 8], ["F", "H", 2], ["F", "A", 8], ["A","F", 8]]
g= Graphe(s,a)

#algorithme
etatInitial= "S"
etatFinal= "G"
chemin= [etatInitial]
recherche= True

while recherche:
   actuel= chemin[len(chemin)-1] 
   if actuel == etatFinal:
       recherche= False
   suivant= f(g.getVoisins(actuel))
   if suivant != "Null":
       chemin.append(suivant)

print(chemin)
