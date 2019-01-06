from Block import Block
from Memory import Memory
from Statement import Statement


class ForStatement(Statement):
    def __init__(self, var, it, blk):
        if it is  None:
            raise ValueError('null iterator argument')
        if blk is None:
            raise ValueError('null block argument')
        self.it = it
        self.var = var
        self.blk = blk

    def execute(self):
        begin = self.it.getbegin().evaluate()
        end = self.it.getend().evaluate()
        ch = self.var.getchar()
        memory = Memory()
        while begin <= end:
            memory.store(ch, begin)
            self.blk.execute()
            begin +=1