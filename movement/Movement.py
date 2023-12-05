from movement.Vector2D import Vector2D
from random import uniform, random

class Movement:
    config = None

    @classmethod
    def set_config(cls, config):
        cls.config = config

    def __init__(self, population):
        self.frames_per_second = self.config.frames_per_second
        self.max_speed = self.config.speed_limit
        self.population = population
        self._height = self.config.n * self.config.pixels_per_meters
        self._width = self.config.m * self.config.pixels_per_meters

    def set_population(self, population):
        self.population = population

    def move_individual(self, individual):
        angle = uniform(0, 360)  # Losowy kierunek w stopniach
        length = uniform((self.max_speed / self.frames_per_second/1.5), self.max_speed / self.frames_per_second) * self.config.pixels_per_meters  # Losowa długość wektora przemieszczenia



        # Tworzenie wektora przemieszczenia
        displacement_vector = Vector2D(angle, length)



        # Przesunięcie
        x = individual.get_x()
        y = individual.get_y()

        x += displacement_vector.getComponents()[0]
        y += displacement_vector.getComponents()[1]
        if x > self._width or x < 0:
            if random() < 0.5:
                x -= 2 * x
            else:
                return self.population.delete_invidual(individual)

        if y > self._height or y < 0:
            if random() < 0.5:
                y -= 2 * y
            else:
                return self.population.delete_invidual(individual)

        individual.change_position(x,y)





