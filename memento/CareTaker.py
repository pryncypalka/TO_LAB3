
class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        if 0 <= index < len(self.mementos):
            return self.mementos[index]
        else:
            print("Nieprawidłowy indeks migawki")

    def get_last_memento(self):
        if self.mementos:
            return self.mementos[-1]
        else:
            print("Brak migawek")
