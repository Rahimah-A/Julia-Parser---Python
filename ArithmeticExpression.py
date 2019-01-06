from abc import ABC, abstractmethod


class ArithmeticExpression (ABC):

    @abstractmethod
    def evaluate(self):
        pass
