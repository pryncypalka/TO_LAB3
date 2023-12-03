import pygame
import sys
import random
from movement.Vector2D import Vector2D
class PyGameSimulation:
    def __init__(self, n, m, speed_limit, infection_rate, initial_population_size, cell_size = 5):
        self.n = n
        self.m = m
        self.speed_limit = speed_limit
        self.infection_rate = infection_rate
        self.initial_population_size = initial_population_size
        self.width, self.height = m * cell_size, n * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.population = self.generate_population()

    def generate_population(self):
        return [Person(random.uniform(0, self.width), random.uniform(0, self.height),
                       random.uniform(0, self.speed_limit)) for _ in range(self.initial_population_size)]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))

            for person in self.population:
                person.move()
                person.infect()
                person.draw()

            pygame.display.flip()
            self.clock.tick(25)  # 25 kroków na sekundę

        pygame.quit()
        sys.exit()