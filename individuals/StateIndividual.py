from abc import ABC, abstractmethod

class StateIndividual(ABC):
    @abstractmethod
    def handle_health_check(self):
        pass