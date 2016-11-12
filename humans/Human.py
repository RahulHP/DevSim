from random import randint


class Human(object):

    def __init__(self, world):
        self.maxAge = 50
        self.age = randint(0, 30)
        self.alive = True
        self.world = world

    def update(self):
        self.age += 1
        if self.age > self.maxAge:
            self.alive = False
