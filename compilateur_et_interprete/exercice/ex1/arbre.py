

class Pile():

    def __init__(self):
        self.laPile= []  

    def isEmpty(self):
        if len(laPile) == 0:
            return True
        else:
            return False

    def size(self):
        return len(laPile)

    def push(self, element):
        laPile.insert(0,element)

    def pop(self):
        laPile.pop(0)

    def peak(self):
        return laPile[0]



myPile= Pile()

print(myPile.size())
