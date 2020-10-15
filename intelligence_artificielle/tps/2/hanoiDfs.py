class Pile():

    def __init__(self, tab):
        #code
        self.tab= tab

    def peek(self):
        return self.tab[0]

    def push(self, e):
        self.tab.insert(0, e)

    def pop(self):
        if len(self.tab) == 0:
            e= -1
        else:
            e= self.tab.pop(0)
        return e

    def state(self):
        return self.tab

class Hanoi():

    def __init__(self, liste):
        self.dic= {}
        self.dic["gauche"]= Pile(liste)
        self.dic["milieu"]= Pile([])
        self.dic["droite"]= Pile([])

    def transition(self, couple):
        e= self.dic[couple[0]].pop()
        self.dic[couple[1]].push(e)

    def state(self):
        return [self.dic["gauche"].state(), self.dic["milieu"].state(), self.dic["droite"].state()]
        
#fonction de l'algorithme

def test(hanoi, explore):
    hanoiSta= hanoi.state()
    #premier teste: valide?
    res= True
    for pile in hanoiSta:
        if -1 in pile:
            res= False
        elif len(pile) == 3:
            if pile[0] > pile[1] or pile[1] > pile[2]:
                res= False
        elif len(pile) == 2:
            if pile[0] > pile[1]:
                res= False
    #deuxième test: déjà traversé?
        for hanoiExp in explore:
            if hanoiSta == hanoiExp.state():
                res= False
    return res
         

h= Hanoi([1,2,3])
h1= Hanoi([4,2,3])

dej= [h1]

#h.transition(("gauche","droite"))

print(test(h,dej))

