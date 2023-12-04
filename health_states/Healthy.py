from individuals.StateIndividual import StateIndividual


class Healthy(StateIndividual):


    def __init__(self):
        self._infection_progress = 0

    def handle_health_check(self):
        print("Jednostka jest zdrowa.")

    def increment_infection_progress(self):
        self._infection_progress += 1

    def reset_infection_progress(self):
        self._infection_progress = 0

    def get_infection_progress(self):
        return self._infection_progress

    def get_color(self):
        return (0, 255, 0)



