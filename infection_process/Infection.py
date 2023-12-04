import random

from health_states import HasSymptoms, NoSymptoms, Healthy, Resistant

class Infection:
    config = None

    def __init__(self):
        pass
    @classmethod
    def set_config(cls, config):
        cls.config = config

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
        for i in population.get_individuals():
            # if isinstance(i.get_health_state(), NoSymptoms.NoSymptoms):
            #     self.list_no_symptoms.append(i)
            # elif isinstance(i.get_health_state(), HasSymptoms.HasSymptoms):
            #     self.list_has_symptoms.append(i)
            # elif isinstance(i.get_health_state(), Healthy.Healthy):
            #     self.list_healthy.append(i)
            # else:
            #     self.list_resistant.append(i)

            if i.get_health_state() == Healthy.Healthy:
                print('działa')
                for other in population.get_individuals():
                    if self.check_distance(i, other) and i != other and other.get_health_state() == HasSymptoms.HasSymptoms:
                        self.set_random_state(i)
                        print("wywołano")


        # print(self.list_no_symptoms)

        # for k in self.list_no_symptoms:
        #     for l in self.list_healthy:
        #         if self.check_distance(k , l):
        #             pass

                #     j.get_health_state().increment_infection_progress()
                #     if j.get_health_state().get_infection_progress() >= self.config.infection_points:
                #         self.set_random_state(j)
                # else:
                #     j.get_health_state().reset_infection_progress()





