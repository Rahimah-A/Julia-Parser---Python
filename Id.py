from ArithmeticExpression import ArithmeticExpression
from Memory import Memory


class Id (ArithmeticExpression):

    def __init__(self, ch):
        if not ch.isalpha():
            raise ValueError ('invalid identifier argument')
        self.ch = ch

    def getchar(self):
        return self.ch

    def evaluate(self):
        memory = Memory()
        return memory.fetch(self.ch)