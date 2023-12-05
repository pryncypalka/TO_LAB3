import copy
from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant
from memento.Memento import Memento
from memento.CareTaker import Caretaker
import random


class Individual:
    config = None

    def __init__(self, x, y, health_status=Healthy.Healthy()):
        self._health_state = health_status
        self._x = x
        self._y = y
        self._caretaker = Caretaker()

    @classmethod
    def set_config(cls, config):
        cls.config = config

    def set_health_state(self, health_state):
        self._health_state = health_state

    def handle_health_check(self):
        return self._health_state.handle_health_check()

    def change_position(self, x, y):
        self._x = x
        self._y = y

    def create_memento(self):
        print("Tworzenie migawki")
        # Tworzenie migawki
        #make a deep copy of the object

        memento = Memento(
            health_status = copy.deepcopy(self),
            x = self._x,
            y = self._y
        )
        self._caretaker.add_memento(memento)

    def restore_from_memento(self):
        memento = self._caretaker.get_last_memento()
        if memento:
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
