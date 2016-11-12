from humans import Human
from random import randint


class World(object):

    def __init__(self,init_pop = 10):
        print "Creating World"
        self.population = list()
        self.popcount = 0
        self.year = 0
        self.populate(init_pop)

    def get_pop(self):
        return len(self.population)

    def update_pop(self):
        self.population = [x for x in self.population if x.alive]
        self.popcount = len(self.population)

    def add_human(self, human):
        self.population.append(human)

    def populate(self,init_pop):
        for i in xrange(init_pop):
            h = Human.Human(self,randint(0,30))
            self.add_human(h)

        self.update_pop()

    def increment_year(self):
        self.year += 1

    def run(self):
        print "Starting population: ", self.get_pop()
        while self.get_pop() != 0:
            self.increment_year()
            for h in self.population:
                h.update()
            self.update_pop()
            print "Year :", self.year, ", Population:", self.popcount

        print "Your nation is dead."
        return
