from individuals.StateIndividual import StateIndividual


class Healthy(StateIndividual):
    def handle_health_check(self):
        print("Jednostka jest zdrowa.")