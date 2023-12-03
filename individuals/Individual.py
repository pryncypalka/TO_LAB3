from abc import ABC, abstractmethod
from individuals.StateIndividual import StateIndividual
from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant
from memento.Memento import Memento

class Individual:
    def __init__(self, x, y, health_status):
        self._health_state = health_status
        self.mementos = []
        self._x = x
        self._y = y

    def change_state(self, new_state):
        self._health_state = new_state

    def change_position(self, x, y):
        self._x += x
        self._y += y




    def create_memento(self):
        # Tworzenie migawki
        memento = Memento(self._x, self._y, self._health_state)
        self.mementos.append(memento)

    def restore_from_memento(self, memento):
        self._health_state = memento.health_status
        self._x = memento.x
        self._y = memento.y

    def display_state(self):
        print(f"Aktualny stan: {self._health_state}")


