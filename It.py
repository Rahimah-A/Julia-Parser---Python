

class It:
    global it
    it = []
    

    def __init__(self, expr1, expr2):
        if expr1 is None or expr2 is None:
            raise ValueError('null arithmetic expression argument')
        self.expr1 = expr1
        self.expr2 = expr2
        it.append(self.expr1)
        it.append(self.expr2)
                
    def getbegin(self):
        return it[0]

    def getend(self):
        return it[1] 