from py_game_simulation.PyGameSimulation import PyGameSimulation
from individuals.Individual import Individual
from movement.Movement import Movement
from infection_process.Infection import Infection
from individuals.Population import Population
import pygame
from py_game_simulation.AppConfig import AppConfig

def main():

    # Parametry symulacji
    config = AppConfig()
    PyGameSimulation.set_config(config)
    Individual.set_config(config)
    Movement.set_config(config)
    Infection.set_config(config)
    Population.set_config(config)











    # Inicjalizacja Pygame
    pygame.init()
    # Inicjalizacja symulacji
    simulation = PyGameSimulation()
    # Uruchomienie symulacji
    simulation.run()

if __name__ == "__main__":
    main()