from enum import Enum
from ArithmeticExpression import ArithmeticExpression


class ArithmeticOperator(Enum):
    ADD_OP = 38
    SUB_OP = 39
    MUL_OP = 40
    DIV_OP = 41
    MOD_OP = 42
    EXP_OP = 43


class BinaryExpression(ArithmeticExpression):

    def __init__(self, op, expr1, expr2):
        if op == None:
            raise ValueError('null arithmetic operator argument')
        if expr1 == None or expr2 == None:
            raise ValueError('null arithmetic expression argument')
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        value = 0
        if self.op == ArithmeticOperator.ADD_OP:
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == ArithmeticOperator.SUB_OP:
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op == ArithmeticOperator.MUL_OP:
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == ArithmeticOperator.DIV_OP:
            value = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op == ArithmeticOperator.MOD_OP:
            value = self.expr1.evaluate() % self.expr2.evaluate()
        elif self.op == ArithmeticOperator.EXP_OP:
            value = self.expr1.evaluate() ** self.expr2.evaluate()
        return value

