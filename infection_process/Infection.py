

class Infection:
    config = None

    def __init__(self,population):
        self.population = population


    @classmethod
    def set_config(cls, config):
        cls.config = config

    def infect(self, individual):
