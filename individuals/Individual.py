from abc import ABC, abstractmethod
from individuals.StateIndividual import StateIndividual
from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant
from memento.Memento import Memento

class Individual:
    def __init__(self, x, y, health_status = Healthy.Healthy()):
        self._health_state = health_status
        self.mementos = []
        self._x = x
        self._y = y

    def change_state(self, new_state):
        self._health_state = new_state

    def change_position(self, x, y, width = 1000, height = 1000):
        self._x += x
        self._y += y
        if self._x > width or self._x < 0:
            self._x -= x
        if self._y > height or self._y < 0:
            self._y -= y




    def create_memento(self):
        # Tworzenie migawki
        memento = Memento(self._x, self._y, self._health_state)
        self.mementos.append(memento)
        print(self._x , self._y, self._health_state)

    def restore_from_memento(self, memento):
        self._health_state = memento.health_status
        self._x = memento.x
        self._y = memento.y

    def display_state(self):
        print(f"Aktualny stan: {self._health_state}")

    def get_health_state(self):
        return self._health_state

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y


