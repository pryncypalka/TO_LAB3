import pygame
import sys
import random
from individuals.Individual import Individual
from movement.Movement import Movement
from infection_process.Infection import Infection
from individuals.Population import Population

class PyGameSimulation:
    config = None
    def __init__(self):
        self.n = self.config.n
        self.m = self.config.m
        self.speed_limit = self.config.speed_limit
        self.initial_population_size = self.config.initial_population_size
        self.width = self.m * self.config.pixels_per_meters
        self.height = self.n * self.config.pixels_per_meters + self.config.gap_for_buttons
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.simulation_paused = False
        self.population = Population()
        self.movement = Movement(self.population)



    @classmethod
    def set_config(cls, config):
        cls.config = config

    def draw_buttons(self):
        # Rysuj przyciski na ekranie
        font = pygame.font.Font(None, 36)

        # Przycisk zatrzymywania/wznawiania
        pause_resume_button = pygame.Rect(10, 10, 200, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), pause_resume_button)
        text = font.render("Pause/Resume", True, (0, 0, 0))
        self.screen.blit(text, (20, 20))

        # Przycisk zapisywania stanu
        save_state_button = pygame.Rect(220, 10, 200, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), save_state_button)
        text = font.render("Save State", True, (255, 255, 255))
        self.screen.blit(text, (230, 20))


        load_state_button = pygame.Rect(430, 10, 200, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), load_state_button)
        text = font.render("Load State", True, (255, 255, 255))
        self.screen.blit(text, (440, 20))

        line = pygame.Rect(0, 65, self.width, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), line)


    def handle_button_clicks(self, event):
        # Obsłuż kliknięcia przycisków
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Przycisk zatrzymywania/wznawiania
            if 10 <= x <= 210 and 10 <= y <= 60:
                self.toggle_simulation_pause()

            # Przycisk zapisywania stanu
            elif 220 <= x <= 420 and 10 <= y <= 60:
                self.save_simulation_state()

            elif 430 <= x <= 630 and 10 <= y <= 60:
                self.load_simulation_state()

    def toggle_simulation_pause(self):
        # Zatrzymaj lub wznow symulację
        self.simulation_paused = not self.simulation_paused



    def draw(self):
        for Individual in self.population.get_individuals():
            color = Individual.get_health_state().get_color()
            pygame.draw.circle(self.screen, color, (Individual.get_x(), Individual.get_y() + self.config.gap_for_buttons), 4)


    def run(self):
        running = True
        self.simulation_paused = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_button_clicks(event)

            self.screen.fill((255, 255, 255))
            self.draw_buttons()  # Dodaj rysowanie przycisków

            self.draw()
            if not self.simulation_paused:
                for Individual in self.population.get_individuals():
                    self.movement.move_individual(Individual)
                    population_difference = (self.config.initial_population_size
                                             - self.population.get_individuals_count())

                    if population_difference > 0:
                        self.population.generate_individuals(population_difference, self.config.rate_symptom,
                                                             self.config.rate_no_symptom, self.config.rate_resistant)
                    Infection(self.population).infect()




            pygame.display.flip()
            self.clock.tick(25)  # 25 kroków na sekundę



        pygame.quit()
        sys.exit()
    #



