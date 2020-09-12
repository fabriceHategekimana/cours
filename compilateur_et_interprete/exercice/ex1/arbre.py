

class Pile():

    def __init__(self):
        self.laPile= []  

    def isEmpty(self):
        if len(self.laPile) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.laPile)

    def push(self, element):
        self.laPile.insert(0,element)

    def pop(self):
        self.laPile.pop(0)

    def peak(self):
        return self.laPile[0]

class Window():

    def __init__(self, sentence):
       self.sentence= sentence.split(" ")
       self.pointer= 0

    def next(self):
        self.pointer= self.pointer+1

    def view(self):
        return self.sentence[self.pointer]

    def regarder(self, position):
        return self.sentence[position]

class Grammar():

    def __init__(self, terminal, nterminal, start, transition):
        self.terminal= terminal
        self.nterminal= nterminal
        self.start= start
        self.transition= transition

    def isTerminal(self, symbol):
        self.terminal.count(symbol)

    def isNterminal(self, symbol):
        self.nterminal.count(symbol)

    def getTransition(self, symbol):
        return self.transition[symbol]


#Définition de la grammaire

t= { }

t["exp"]= [["digit", "num"]]
t["num"]= [["digit", "num"], [""]]
t["digit"]= [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]]

termin= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ntermin= ["exp", "digit", "num"]
