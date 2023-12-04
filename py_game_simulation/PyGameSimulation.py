import pygame
import sys
import random
from individuals.Individual import Individual
from movement.Vector2D import Vector2D
from movement.Movement import Movement
class PyGameSimulation:
    def __init__(self, n, m, speed_limit, infection_rate, initial_population_size, cell_size = 30):
        self.n = n
        self.m = m
        self.speed_limit = speed_limit
        self.infection_rate = infection_rate
        self.initial_population_size = initial_population_size
        self.width, self.height = 500, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.population = self.generate_population()

    def generate_population(self):
        return [Individual(random.uniform(0, self.width), random.uniform(0, self.height)) for _ in range(self.initial_population_size)]

    def draw(self):
        for Individual in self.population:
            color = (255, 0, 0)
            pygame.draw.circle(self.screen, color, (Individual.get_x(), Individual.get_y()), 2)
    def create_movement(self):
        return Movement(self.population)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))

            self.draw()
            self.create_movement().move_individuals()

            pygame.display.flip()
            self.clock.tick(25)  # 25 kroków na sekundę

        pygame.quit()
        sys.exit()