from Statement import Statement


class RepeatStatement(Statement):

    def __init__(self, blk, expr):
        if blk == None:
            raise ValueError('null block argument')
        if expr == None:
            raise ValueError('null boolean expression argument')
        self.blk = blk
        self.expr = expr

    def execute(self):
        condition = True
        while condition:
            condition = False
            self.blk.execute()

