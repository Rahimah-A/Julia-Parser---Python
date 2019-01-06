from ArithmeticExpression import ArithmeticExpression


class LiteralInteger(ArithmeticExpression):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value