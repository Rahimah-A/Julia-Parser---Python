from Statement import Statement


class WhileStatement(Statement):

    def __init__(self, expr, blk):
        if expr == None:
            raise ValueError('null boolean expression argument')
        if blk == None:
            raise ValueError('null block argument')
        self.expr = expr
        self.blk = blk

    def execute(self):

        while self.expr.evaluate():
            self.blk.execute()
