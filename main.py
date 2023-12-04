from py_game_simulation.PyGameSimulation import PyGameSimulation
import pygame

def main():

    # Parametry symulacji
    n = 20  # liczba wierszy obszaru
    m = 20  # liczba kolumn obszaru
    speed_limit = 2.5 # górny limit szybkości
    infection_rate = 0.1  # prawdopodobieństwo zakażenia
    initial_population_size = 100

    # Inicjalizacja Pygame
    pygame.init()

    # Inicjalizacja symulacji
    simulation = PyGameSimulation(n, m, speed_limit, infection_rate, initial_population_size)

    # Uruchomienie symulacji
    simulation.run()

if __name__ == "__main__":
    main()