from individuals.StateIndividual import StateIndividual


class HasSymptoms(StateIndividual):
    def handle_health_check(self):
        print("Jednostka ma objawy choroby.")

    def get_color(self):
        return (255, 0, 0)