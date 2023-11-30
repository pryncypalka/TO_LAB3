from abc import ABC, abstractmethod
from individuals.StateIndividual import StateIndividual
from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant
import copy
from memento.Memento import Memento

class Individual:
    def __init__(self, x, y, health_status):
        self.state = health_status
        self.mementos = []
        self._x = x
        self._y = y

    def change_state(self, new_state):
        self.state = new_state



    def create_memento(self):
        # Tworzenie migawki
        memento = Memento(copy.deepcopy(self.state))
        self.mementos.append(memento)

    def restore_from_memento(self, memento):
        # Przywracanie stanu z migawki
        self.state = copy.deepcopy(memento.state)

    def display_state(self):
        print(f"Aktualny stan: {self.state.health_status}")


