
from Statement import Statement


class IfStatement(Statement):

    def __init__(self, expr, blk1, blk2):
        if expr == None:
            raise ValueError('null boolean expression')
        if blk1 == None or blk2 == None:
            raise ValueError('null block argument')
        self.expr = expr
        self.blk1 = blk1
        self.blk2 = blk2

    def execute(self):        
        if self.expr.evaluate():
            self.blk1.execute()
        else:
            self.blk2.execute()