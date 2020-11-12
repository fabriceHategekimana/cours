class Graphe():

    def __init__(self, sommets, cotes):
        #code
        self.vertex= sommets
        if isinstance(cotes, list):
            self.edge= cotes
        elif isinstance(cotes, str):
            self.edge= []
            cotes= cotes.split(" ")
            for i in cotes:
               self.edge.append(i.split(".")) 
            
    def getVoisins(self, element):
        voisins= []
        for c in self.edge: 
            if element in c[0]:
                voisins.append(c[1])
            elif element in c[1]:
                voisins.append(c[0])
        return voisins

    def getVertex(self): 
        return self.vertex

    def getEdge(self): 
       return self.edge
            
