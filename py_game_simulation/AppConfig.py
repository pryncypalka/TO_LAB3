
class AppConfig:

    def __init__(self):
        self.__app_name = "PyGame Infection Simulation "
        self.__app_version = "1.0.0"
        self.__app_author = "Jacek Kamiński"

        # Parametry symulacji
        self.n = 20  # liczba wierszy obszaru
        self.m = 30  # liczba kolumn obszaru
        self.speed_limit = 10  # górny limit szybkości
        self.initial_population_size = 200
        self.pixels_per_meters = 30
        self.frames_per_second = 25
        self.gap_for_buttons = 80

        self.rate_symptom = 0.1
        self.rate_no_symptom = 0.1
        self.rate_resistant = 0.0


