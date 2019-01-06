from Statement import Statement


class PrintStatement(Statement):
   
    
    def __init__(self, expr):
        if expr is None:
            raise ValueError('null arithmetic expression')
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())
