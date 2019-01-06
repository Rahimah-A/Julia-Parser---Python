from enum import Enum


class RelationalOperator(Enum):
    EQ_OP = 32
    NE_OP = 33
    GT_OP = 34
    GE_OP = 35
    LT_OP = 36
    LE_OP = 37


class BooleanExpression:
    def __init__(self, op, expr1, expr2):
        if op is None:
            raise ValueError('null relational operator argument')
        if expr1 is None or expr2 is None:
            raise ValueError('null arithmetic expression argument')
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.op == RelationalOperator.EQ_OP: 
            result = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == RelationalOperator.NE_OP:
            result = self.expr1.evaluate() != self.expr2.evaluate()
        elif self.op == RelationalOperator.LT_OP:
            result = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == RelationalOperator.LE_OP:
            result = self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == RelationalOperator.GT_OP:
            result = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == RelationalOperator.GE_OP:
            result = self.expr1.evaluate() >= self.expr2.evaluate()

        return result

