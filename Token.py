

class Token:

    lexeme = ''
    rownumber = 0
    columnnumber = 0

    def __init__(self, toktype, lexeme, rownumber, columnnumber):
        if toktype is None:
            raise ValueError('null TokenType argument')
        if lexeme is None:
            raise ValueError('invalid lexeme error')
        if rownumber is None:
            raise ValueError('invalid row number argument')
        if columnnumber is None:
            raise ValueError('invalid column number argument')
        self.toktype = toktype
        self.lexeme = lexeme
        self.rownumber = rownumber
        self.columnnumber = columnnumber

    def gettoktype(self):
        return self.toktype

    def getlexeme(self):
        return self.lexeme

    def getrownumber(self):
        return self.rownumber

    def getcolumnnumber(self):
        return self.columnnumber
