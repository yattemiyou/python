import numpy as np
import math


class Field:
    ROW = 5
    COLUMN = 5
    RANGE = 5

    def __init__(self, field=None):
        if field is None:
            self.sediment = np.random.rand(Field.ROW, Field.COLUMN)
            self.sediment *= Field.RANGE
        else:
            self.sediment = np.copy(field.sediment)

        self.mean = self.sediment.mean()

    def dig(self, x, y, quantity):
        self.sediment[x][y] -= quantity

    def fill(self, x, y, quantity):
        self.sediment[x][y] += quantity

    def find_target(self, x, y, condition):
        candidate = list(zip(*np.where(condition)))

        candidate.sort(key=lambda c: self.get_distance(c[0], c[1], x, y))

        return candidate[0]

    def get_distance(self, xt, yt, x, y):
        return math.sqrt((xt - x) ** 2 + (yt - y) ** 2)
