from individuals.StateIndividual import StateIndividual


class Resistant(StateIndividual):
    def handle_health_check(self):
        print("Jednostka jest odporna na chorobę.")

    def get_color(self):
        return (0, 0, 255)