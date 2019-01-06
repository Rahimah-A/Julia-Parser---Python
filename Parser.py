
from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression, ArithmeticOperator
from Block import Block
from BooleanExpression import BooleanExpression, RelationalOperator
from Id import Id
from It import It
from PrintStatement import PrintStatement
from LexicalAnalyzer import LexicalAnalyzer
from LexicalException import LexicalException
from ParserException import ParserException
from Program import Program
from RepeatStatement import RepeatStatement
from Token import Token
from TokenType import TokenType
from IfStatement import IfStatement
from WhileStatement import WhileStatement


class Parser:
    global token
    token = Token
    
    def __init__(self, filename):
        global l1
        l1 = LexicalAnalyzer(filename)

    def parse(self):
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.FUNCTION_TOK)
        functionname = self.getid()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.LEFT_PAREN_TOK)
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.RIGHT_PAREN_TOK)
        blk = self.getblock()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.END_TOK)
        tok = self.getnexttoken()
        if tok.gettoktype() != TokenType.EOS_TOK:
            raise ParserException('garbage at end of file')
        return Program(blk)

    def getblock(self):
        blk = Block()
        tok = self.getlookaheadtoken()
        while self.isvalidstartofstatement(tok):
            stmt = self.getstatement()
            blk.addin(stmt)
            tok = self.getlookaheadtoken()

        return blk

    def getstatement(self):       
        tok = self.getlookaheadtoken()
        if tok.gettoktype() == TokenType.IF_TOK:
            stmt = self.getifstatement()
        elif tok.gettoktype() == TokenType.WHILE_TOK:
            stmt = self.getwhilestatement()
        elif tok.gettoktype() == TokenType.PRINT_TOK:
            stmt = self.getprintstatement()
        elif tok.gettoktype() == TokenType.REPEAT_TOK:
            stmt = self.getrepeatstatement()
        elif tok.gettoktype() == TokenType.ID_TOK:
            stmt = self.getassignmentstatement()
        elif tok.gettoktype() == TokenType.FOR_TOK:
            stmt = self.getforstatement()
        else:
            raise ParserException('got ', tok.gettoktype(), 'invalid statement at row ', tok.getrownumber(),' and column ', tok.getcolumnnumber())
        return stmt

    def getassignmentstatement(self):
        var = self.getid()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.ASSIGN_TOK)
        expr = self.getarithmeticexpression()
        return AssignmentStatement(var, expr)

    def getrepeatstatement(self):
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.REPEAT_TOK)
        blk = Block()
        blk = self.getblock()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.UNTIL_TOK)
        expr = self.getbooleanexpression()
        return RepeatStatement(blk, expr)

    def getprintstatement(self):
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.PRINT_TOK)
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.getarithmeticexpression()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expr)

    def getwhilestatement(self):
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.WHILE_TOK)
        expr = self.getbooleanexpression()
        blk = Block()
        blk = self.getblock()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.END_TOK)
        return WhileStatement(expr, blk)

    def getforstatement(self):
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.FOR_TOK)
        id1 = self.getid()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.ASSIGN_TOK)
        it = self.getiterstataement()
        blk = Block()
        blk = self.getblock()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.END_TOK)
        from ForStatement import ForStatement
        return ForStatement(id1, it, blk)

    def getifstatement(self):
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.IF_TOK)
        expr = self.getbooleanexpression()
        blk1 = self.getblock()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.ELSE_TOK)
        blk2 = self.getblock()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.END_TOK)
        return IfStatement(expr, blk1, blk2)

    def isvalidstartofstatement(self, tok):
        assert (tok is not None)
        return (tok.gettoktype() == TokenType.ID_TOK or
                tok.gettoktype() == TokenType.IF_TOK or tok.gettoktype() == TokenType.WHILE_TOK or
                tok.gettoktype() == TokenType.PRINT_TOK or tok.gettoktype() == TokenType.REPEAT_TOK or
                tok.gettoktype() == TokenType.FOR_TOK)

    def getarithmeticexpression(self):
        tok = self.getlookaheadtoken()
        if tok.gettoktype() == TokenType.ID_TOK:
            expr = self.getid()
        elif tok.gettoktype() == TokenType.LITERAL_INTEGER_TOK:
            expr = self.getliteralinteger()
        else:
            expr = self.getbinaryexpression()
        return expr

    def getbinaryexpression(self):
        op = self.getarithmeticoperator()
        expr1 = self.getarithmeticexpression()
        expr2 = self.getarithmeticexpression()
        return BinaryExpression(op, expr1, expr2)

    def getarithmeticoperator(self):
        tok = self.getnexttoken()
        if tok.gettoktype() == TokenType.ADD_TOK:
            op = ArithmeticOperator.ADD_OP
        elif tok.gettoktype() == TokenType.SUB_TOK:
            op = ArithmeticOperator.SUB_OP
        elif tok.gettoktype() == TokenType.MUL_TOK:
            op = ArithmeticOperator.MUL_OP
        elif tok.gettoktype() == TokenType.DIV_TOK:
            op = ArithmeticOperator.DIV_OP
        else:
            raise ParserException('arithmetic operator expected at row ', tok.getrownumber, ' and column ', tok.getcolumnnumber)
        return op

    def getliteralinteger(self):
        tok = self.getnexttoken()
        if tok.gettoktype() != TokenType.LITERAL_INTEGER_TOK:
            raise ('literal integer expected at row ', tok.getrownumber(), 'and column ', tok.getcolumnnumber())
        value = int(tok.getlexeme())
        from LiteralInteger import LiteralInteger
        return LiteralInteger(value)

    def getid(self):
        tok = self.getnexttoken()
        if tok.gettoktype() != TokenType.ID_TOK:
            raise ParserException('identifier expected at row ', tok.getrownumber(), ' and column ', tok.getcolumnnumber())
        return Id(tok.getlexeme()[0])

    def getiterstataement(self):
        expr1 = self.getarithmeticexpression()
        tok = self.getnexttoken()
        self.matchthis(tok, TokenType.COL_TOK)
        expr2 = self.getarithmeticexpression()
        return It(expr1, expr2)

    def getbooleanexpression(self):
        op = self.getrelationaloperator()
        expr1 = self.getarithmeticexpression()
        expr2 = self.getarithmeticexpression()
        return BooleanExpression(op, expr1, expr2)

    def getrelationaloperator(self):
        tok = self.getnexttoken()
        if tok.gettoktype() == TokenType.EQ_TOK:
            op = RelationalOperator.EQ_OP
        elif tok.gettoktype() == TokenType.NE_TOK:
            op = RelationalOperator.NE_OP
        elif tok.gettoktype() == TokenType.GT_TOK:
            op = RelationalOperator.GT_OP
        elif tok.gettoktype() == TokenType.GE_TOK:
            op = RelationalOperator.GE_OP
        elif tok.gettoktype() == TokenType.LT_TOK:
            op = RelationalOperator.LT_OP
        elif tok.gettoktype() == TokenType.LE_TOK:
            op = RelationalOperator.LE_OP
        else:
            raise ParserException('relational operator expected at  ', tok.getrownumber(), ' and column ', tok.getcolumnnumber())
        return op

    def matchthis(self, tok, toktype):
        assert(tok is not None)
        assert (toktype is not None)
        if tok.gettoktype() is not toktype:
            raise ParserException(toktype, 'expected at row ', tok.getrownumber(), ' and column ', tok.getcolumnnumber())

    def getlookaheadtoken(self):
        try:
            tok = l1.getlookaheadtoken()
        except LexicalException:
            raise ParserException('no more tokens')
        return tok

    def getnexttoken(self):
        
        try:
            tok = l1.getnexttoken()
        except LexicalException:
            raise ParserException('no more tokens')
        return tok
