class Block:
    def __init__(self):
        self.stmts = []
    
    def addin(self, stmt):
        if stmt is None:
            raise ValueError("null statement argument")
        self.stmts.append(stmt)
        
    def execute(self):
        for stmt in self.stmts:
            stmt.execute()