class Program:
    def __init__(self, blk):
        if blk == None:
            raise ValueError('null block argument')
        self.blk = blk
    
    def execute(self):
        self.blk.execute()
