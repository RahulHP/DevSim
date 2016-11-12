class Human(object):

    def __init__(self, world=None, age=20):
        self.maxAge = 50
        self.age = age
        self.alive = True
        self.world = world

    def update(self):
        self.age += 1
        if self.age > self.maxAge:
            self.alive = False

    def get_age(self):
        return self.age

    def is_alive(self):
        return self.alive