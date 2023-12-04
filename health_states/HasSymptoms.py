from individuals.StateIndividual import StateIndividual


class HasSymptoms(StateIndividual):

    def __init__(self):
        self._points = 0

    def handle_health_check(self):
        print("Jednostka ma objawy choroby.")

    def get_color(self):
        return (255, 0, 0)


    def increment_points(self):
        self._points += 1

    def get_points(self):
        return self._points

