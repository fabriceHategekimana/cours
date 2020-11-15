class Fenetre():

    def __init__(self, chaine):
        #code
        self.liste= chaine.split()
        self.pointeur= 0

    def actuel(self):
        #si on est au bout de l'expression
        if len(self.liste) <= self.pointeur:
            return None
        else:
            return self.liste[self.pointeur]

    def suivant(self):
        self.pointeur= self.pointeur+1
