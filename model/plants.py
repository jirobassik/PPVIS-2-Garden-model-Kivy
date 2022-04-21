from abc import ABC, abstractmethod


class Plants(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass

    @abstractmethod
    def watering(self):
        pass

    @abstractmethod
    def drought(self):
        pass

    @abstractmethod
    def ill(self):
        pass

    @abstractmethod
    def print_state(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def max_harvest(self):
        pass

    @abstractmethod
    def get_num_harvest(self):
        pass

    @abstractmethod
    def is_rotten(self):
        pass

    @abstractmethod
    def get_weather_cond(self):
        pass

    @abstractmethod
    def set_state(self, states):
        pass

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def change_state(self):
        pass

    @abstractmethod
    def set_weather_cond(self, num: float):
        pass

    @abstractmethod
    def get_limit_weather_cond_w(self):
        pass

    @abstractmethod
    def get_limit_weather_cond_d(self):
        pass

    @abstractmethod
    def get_can_harvest(self):
        pass

    @abstractmethod
    def set_ill(self, ills: int):
        pass

    @abstractmethod
    def get_ill(self):
        pass




