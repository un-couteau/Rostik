import math
from typing import NoReturn


class NumericalMethod:
    def __init__(self, a: float, b: float, e: float) -> NoReturn:
        self.__a = a
        self.__b = b
        self.__e = e

    def getF1(self, x: int | float) -> float:
        return math.log(x) + math.pow(x, 2) - 8

    def getF2(self, x: int | float) -> float:
        # return 1 / ((2 * x) * (math.sqrt(8 - math.log(x))))
        return 1 / (2 * x * math.sqrt(8 - math.log(x)))

    def dehotomia(self) -> float:
        x0: int = 0
        a = self.__a
        b = self.__b
        e = self.__e

        while abs(a - b) > e:
            x0 = (a + b) / 2

            if (self.getF1(x0) * self.getF1(b)) < 0:
                a = x0
            else:
                b = x0

        return x0

    def iteration(self) -> float:
        x1: int = 0
        x0: float = (self.__a + self.__b) / 2

        while (abs(x1 - x0)) > self.__e:
            x0 = x1
            x1 = self.getF2(x0)

        return x1
