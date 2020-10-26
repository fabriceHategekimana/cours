class Pile():

    def __init__(self, liste):
        #code
        self.liste= liste

    def push(self, element):
        self.liste.append(element)

    def pop(self):
        if len(self.liste) == 0:
            return None
        else:
            return self.liste.pop()

    def isEmpty(self):
        if len(self.liste) == 0:
            return True
        else:
            return False

    def peak(self):
        if len(self.liste) == 0:
            return None
        else:
            return self.liste[len(self.liste)-1]

    def length(self):
        return len(self.liste)

    def state(self):
        return self.liste
