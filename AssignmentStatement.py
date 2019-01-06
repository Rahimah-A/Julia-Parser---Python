from Memory import Memory
from Statement import Statement


class AssignmentStatement(Statement):

    def __init__(self, var, expr):
        if var == None:
            raise ValueError('null id argument')
        if expr == None:
            raise ValueError('null ArithmeticExpression argument')

        self.var = var
        self.expr = expr

    def execute(self):   
        memory = Memory()
        memory.store( self.var.getchar(), self.expr.evaluate())
