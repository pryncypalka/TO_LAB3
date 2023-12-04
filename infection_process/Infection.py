import random

from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant

class Infection:
    config = None


    def __init__(self):
        pass
    @classmethod
    def set_config(cls, config):
        cls.config = config

    def get_resistant(self, list_potencial_resistant):
        for symptom in list_potencial_resistant:
            symptom.get_health_state().increment_points()
            if symptom.get_health_state().get_points() >= (random.randint(20, 30) * self.config.frames_per_second):
                symptom.set_health_state(Resistant.Resistant())


    def check_distance(self, individual1, individual2):
        distance = ((individual1.get_x() - individual2.get_x()) ** 2 + (
                    individual1.get_y() - individual2.get_y()) ** 2) ** 0.5
        if distance <= self.config.infection_radius:
            return True
        else:
            return False

    def set_random_state(self, individual):
        if random.random() > 0.5:
            individual.set_health_state(HasSymptoms.HasSymptoms())
        else:
            individual.set_health_state(NoSymptoms.NoSymptoms())

    def infect(self, population):
        list_no_symptoms = []
        list_has_symptoms = []
        list_healthy = []
        list_resistant = []

        for i in population.get_individuals():
            if isinstance(i.get_health_state(), NoSymptoms.NoSymptoms):
                list_no_symptoms.append(i)
            elif isinstance(i.get_health_state(), HasSymptoms.HasSymptoms):
                list_has_symptoms.append(i)
            elif isinstance(i.get_health_state(), Healthy.Healthy):
                list_healthy.append(i)
            else:
                list_resistant.append(i)

        list_healthy_copy = list_healthy.copy()


        for k in list_no_symptoms:
            for l in list_healthy:
                if self.check_distance(k, l) and isinstance(l.get_health_state(), Healthy.Healthy):
                    l.get_health_state().increment_points_no_symptoms()
                    list_healthy.remove(l)

                    if l.get_health_state().get_points_no_symptoms() >= self.config.infection_points:
                        l.get_health_state().reset_points_no_symptoms()
                        if random.random() < 0.5:
                            self.set_random_state(l)

        for heal in list_healthy:
            if isinstance(heal.get_health_state(), Healthy.Healthy):
                heal.get_health_state().reset_points_no_symptoms()

        for sym in list_has_symptoms:
            for heal in list_healthy_copy:
                if self.check_distance(sym, heal) and isinstance(heal.get_health_state(), Healthy.Healthy):
                    heal.get_health_state().increment_points_symptoms()
                    list_healthy_copy.remove(heal)

                    if heal.get_health_state().get_points_symptoms() >= self.config.infection_points:
                        heal.get_health_state().reset_points_symptoms()
                        self.set_random_state(heal)

        for heal in list_healthy_copy:
            if isinstance(heal.get_health_state(), Healthy.Healthy):
                heal.get_health_state().reset_points_symptoms()

        self.get_resistant(list_no_symptoms)
        self.get_resistant(list_has_symptoms)











