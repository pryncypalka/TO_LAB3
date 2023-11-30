from individuals.StateIndividual import StateIndividual


class NoSymptoms(StateIndividual):
    def handle_health_check(self):
        print("Jednostka nie ma objawów choroby.")