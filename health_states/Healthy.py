from individuals.StateIndividual import StateIndividual


class Healthy(StateIndividual):


    def __init__(self):
        self._points_symptoms = 0
        self._points_no_symptoms = 0

    def handle_health_check(self):
        print("Jednostka jest zdrowa.")

    def increment_points_symptoms(self):
        self._points_symptoms += 1

    def increment_points_no_symptoms(self):
        self._points_no_symptoms += 1

    def reset_points_no_symptoms(self):
        self._points_no_symptoms = 0

    def reset_points_symptoms(self):
        self._points_symptoms = 0

    def get_points_symptoms(self):
        return self._points_symptoms

    def get_points_no_symptoms(self):
        return self._points_no_symptoms

    def get_color(self):
        return (0, 255, 0)



