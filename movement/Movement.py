from Vector2D import Vector2D
from random import uniform

class Movement:
    def __init__(self, individuals, frames_per_second=25, max_speed=2.5):
        self.individuals = individuals
        self.frames_per_second = frames_per_second
        self.max_speed = max_speed

    def move_individuals(self):
        for individual in self.individuals:
            angle = uniform(0, 360)  # Losowy kierunek w stopniach
            length = uniform(0, self.max_speed / self.frames_per_second)

            # Tworzenie wektora przemieszczenia
            displacement_vector = Vector2D(angle, length)

            # Zapisanie poprzedniego stanu przed ruchem
            individual.create_memento()

            # Zmiana pozycji z użyciem wektora przemieszczenia
            individual.change_position(displacement_vector.getComponents()[0], displacement_vector.getComponents()[1])


            # Ograniczenie pozycji do obszaru symulacji
            individual.position.x = max(0, min(individual.position.x, self.width - 1))
            individual.position.y = max(0, min(individual.position.y, self.height - 1))
