from individuals.StateIndividual import StateIndividual


class NoSymptoms(StateIndividual):

    def __init__(self):
        self._points = 0
    def handle_health_check(self):
        print("Jednostka nie ma objawów choroby.")

    def get_color(self):
        return (255, 192, 203)

    def increment_points(self):
        self._points += 1

    def get_points(self):
        return self._points