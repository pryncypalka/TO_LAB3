from individuals.Individual import Individual
from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant
import random

class Population:
    config = None
    def __init__(self):
        self._individuals = []
        self.height = self.config.n * self.config.pixels_per_meters
        self.width = self.config.m * self.config.pixels_per_meters
        self.generate_individuals(self.config.initial_population_size)

    @classmethod
    def set_config(cls, config):
        cls.config = config
    def delete_invidual(self, Individual):
        self._individuals.remove(Individual)



    def generate_individuals(self, number_of_individuals, rate_symptom=0.0, rate_no_symptom=0.0,
                             rate_resistant=0.0):
        threshold_3 = rate_symptom + rate_no_symptom + rate_resistant
        threshold_2 = rate_symptom + rate_no_symptom
        threshold_1 = rate_symptom
        for i in range(number_of_individuals):
            infection_probability = random.random()


            if infection_probability < threshold_1:
                health_state = HasSymptoms.HasSymptoms()
            elif threshold_1 <= infection_probability < threshold_2:
                health_state = NoSymptoms.NoSymptoms()
            elif threshold_2 <= infection_probability < threshold_3:
                health_state = Resistant.Resistant()
            else:
                health_state = Healthy.Healthy()

            self._individuals.append(
                Individual(random.uniform(0, self.width), random.uniform(0, self.height), health_state))

    def get_individuals(self):
        return self._individuals

    def get_individuals_count(self):
        return len(self._individuals)


