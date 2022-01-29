from abc import ABC, abstractmethod
import numpy as np


class Excavator_Base(ABC):
    def __init__(self, field):
        self.field = field

        self.x, self.y = 0, 0
        self.sediment = 0.0
        self.capacity = 1.0

        self.xt, self.yt = self.find_target()

    @abstractmethod
    def find_target(self):
        pass

    def next(self):
        if self.x == self.xt and self.y == self.yt:
            if self.sediment > 0.0:
                self.fill()
            else:
                self.dig()

            try:
                self.xt, self.yt = self.find_target()
            finally:
                return

        self.move()

    def move(self):
        dx = self.xt - self.x
        dy = self.yt - self.y

        if dx != 0:
            if dx > 0:
                self.x += 1
            else:
                self.x -= 1
            return

        if dy != 0:
            if dy > 0:
                self.y += 1
            else:
                self.y -= 1
            return

    def dig(self):
        q = self.field.sediment[self.x][self.y] - self.field.mean

        if q >= self.capacity:
            self.field.dig(self.x, self.y, self.capacity)
            self.sediment = self.capacity
        else:
            self.field.dig(self.x, self.y, q)
            self.sediment = q

    def fill(self):
        q = self.field.mean - self.field.sediment[self.x][self.y]

        if q >= self.sediment:
            self.field.fill(self.x, self.y, self.sediment)
            self.sediment = 0.0
        else:
            self.field.fill(self.x, self.y, q)
            self.sediment -= q


class Excavator_V1(Excavator_Base):
    def find_target(self):
        if self.sediment > 0.0:
            condition = self.field.sediment == np.min(self.field.sediment)
        else:
            condition = self.field.sediment == np.max(self.field.sediment)

        return self.field.find_target(self.x, self.y, condition)


class Excavator_V2(Excavator_Base):
    def find_target(self):
        if self.sediment > 0.0:
            condition = self.field.sediment < self.field.mean
        else:
            condition = self.field.sediment > self.field.mean

        return self.field.find_target(self.x, self.y, condition)


class Excavator_V3(Excavator_V2):
    def __init__(self, field):
        super().__init__(field)

        self.capacity = 2.0
