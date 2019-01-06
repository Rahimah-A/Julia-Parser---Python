from LexicalException import LexicalException
from Token import Token
from TokenType import TokenType


class LexicalAnalyzer:
    global tokenlist
    tokenlist = []

    def __init__(self, filename):
        self.filename = filename
        if filename is None:
            raise ValueError('null file name argument')
        with open(filename, "r") as f:
            for linenumber, line in enumerate(f, 1):
                contents = line.strip()
                self.processline(contents, linenumber)
        tokenlist.append(Token(TokenType.EOS_TOK, "EOS", linenumber, 1))

    def processline(self, line, linenumber):
        if line is None:
            raise ValueError ('null line argument')
        if linenumber <= 0:
            raise ValueError('invalid line number argument')
        index = self.skipwhitespace(line, 0)
        while index < len(line) :
            lexeme = self.getlexeme(line, index)
            toktype = self.gettokentype(lexeme, linenumber, index + 1)
            tokenlist.append(Token(toktype, lexeme, linenumber, index+1))
            index += len(lexeme)
            index = self.skipwhitespace(line, index)

    def gettokentype(self, lexeme, rownumber, columnnumber):
        if lexeme is None or len(lexeme) == 0:
            raise ValueError('invalid string argument')
        toktype = TokenType.EOS_TOK
        if lexeme[0].isdigit():
            if self.alldigits(lexeme):
                toktype = TokenType.LITERAL_INTEGER_TOK
            else:
                raise LexicalException('literal integer expected' + 'at row' + rownumber + 'and column ' + columnnumber)
        elif lexeme[0].isalpha():
            if len(lexeme) == 1:
                toktype = TokenType.ID_TOK
            elif lexeme == "if":
                toktype = TokenType.IF_TOK
            elif lexeme == "function":
                toktype = TokenType.FUNCTION_TOK
            elif lexeme == "then":
                toktype = TokenType.THEN_TOK
            elif lexeme == "end":
                toktype = TokenType.END_TOK
            elif lexeme == "else":
                toktype = TokenType.ELSE_TOK
            elif lexeme == "while":
                toktype = TokenType.WHILE_TOK
            elif lexeme == "do":
                toktype = TokenType.DO_TOK
            elif lexeme == "print":
                toktype = TokenType.PRINT_TOK
            elif lexeme == "repeat":
                toktype = TokenType.REPEAT_TOK
            elif lexeme == "until":
                toktype = TokenType.UNTIL_TOK
            elif lexeme == "for":
                toktype = TokenType.FOR_TOK
            else:
                raise LexicalException ('invalid lexeme ' + ' at row ' + rownumber + ' and column' + columnnumber)
        elif lexeme == "(":
            toktype = TokenType.LEFT_PAREN_TOK
        elif lexeme == ")":
            toktype = TokenType.RIGHT_PAREN_TOK
        elif lexeme == ">=":
            toktype = TokenType.GE_TOK
        elif lexeme == ">":
            toktype = TokenType.GT_TOK
        elif lexeme == "<=":
            toktype = TokenType.LE_TOK
        elif lexeme == "<":
            toktype = TokenType.LT_TOK
        elif lexeme == "==":
            toktype = TokenType.EQ_TOK
        elif lexeme == "!=":
            toktype = TokenType.NE_TOK
        elif lexeme == "+":
            toktype = TokenType.ADD_TOK
        elif lexeme == "-":
            toktype = TokenType.SUB_TOK
        elif lexeme == "*":
            toktype = TokenType.MUL_TOK
        elif lexeme == "/":
            toktype = TokenType.DIV_TOK
        elif lexeme == "=":
            toktype = TokenType.ASSIGN_TOK
        elif lexeme == "^":
            toktype = TokenType.EXP_TOK
        elif lexeme == "%":
            toktype = TokenType.MOD_TOK
        elif lexeme == "\\":
            toktype = TokenType.REV_DIV_TOK
        elif lexeme == ":":
            toktype = TokenType.COL_TOK
        else:
            raise LexicalException ('invalid lexeme at row ' + rownumber + ' and column ' + columnnumber)
        print(toktype)
        return toktype

    def alldigits (self, lexeme):
        if lexeme is None:
            raise ValueError ('null string argument')
        i = 0
        while i < len(lexeme) and lexeme[i].isdigit:
            i += 1
        return i == len(lexeme)

    def getlexeme(self, line, index):
        if line is None:
            raise ValueError('null string argument')
        if index < 0:
            raise ValueError('invalid index argument')

        i = index
        while i < len(line) and not line[i].isspace():
            i += 1
        return line[index:i]

    def skipwhitespace(self, line, index):
        while index < len(line) and line[index].isspace():
            index += 1
        return index

    def getlookaheadtoken(self):
        if not tokenlist:
            raise ValueError('no more tokens')
        return tokenlist[0]

    def getnexttoken(self):
        if not tokenlist:
            raise ValueError('no more tokens')
        return tokenlist.pop(0)


