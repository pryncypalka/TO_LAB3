from individuals.StateIndividual import StateIndividual


class NoSymptoms(StateIndividual):
    def handle_health_check(self):
        print("Jednostka nie ma objawów choroby.")

    def get_color(self):
        return (255, 192, 203)

    def get_name(self):
        return "NoSymptoms"