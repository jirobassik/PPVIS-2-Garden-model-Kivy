import random
from model.plants import Plants
from utility.write_in_file import write_in_file
from utility.collect_data import Data

class Cucumber(Plants):
    states = {0: 'отсутствует', 1: 'росток', 2: 'начался ветвиться', 3: 'выпускает части',
              4: 'созрел', 5: 'перезрел', 6: 'сгнил'}
    ills = {0: 'появился вредитель - тля', 1: 'появилась болезнь - корневая гниль'}

    def __init__(self) -> None:
        self.num_harvest = None
        self.can_harvest = True
        self.name = "Огурец"
        self.state_grow = 0
        self.state = 0
        self.weather_cond = 0
        self.limit_weather_cond_w = 1
        self.limit_weather_cond_d = -1
        self.ills = None

    def __repr__(self):
        return str(self.__dict__)

    def grow(self) -> None:
        if self.state < 6:
            self.state += 0.25
        self.print_state()

    def get_state(self) -> int:
        return self.state

    def change_state(self) -> None:
        if 0.25 <= self.state <= 1:
            self.state_grow = 1
        if 1 < self.state <= 2:
            self.state_grow = 2
        if 2 < self.state <= 3:
            self.state_grow = 3
        if 3 < self.state <= 4:
            self.state_grow = 4
        if 4 < self.state <= 5:
            self.state_grow = 5
        if 5 < self.state <= 7:
            self.state_grow = 6

    def set_state(self, states) -> None:
        self.state += states

    def is_ripe(self) -> bool:
        if 3 <= self.state <= 5:
            return True
        return False

    def is_rotten(self) -> bool:
        if 5 < self.state <= 7:
            return True
        return False

    def get_weather_cond(self) -> int:
        return self.weather_cond

    def get_can_harvest(self) -> bool:
        return self.can_harvest

    def get_limit_weather_cond_w(self) -> int:
        return self.limit_weather_cond_w

    def get_limit_weather_cond_d(self) -> int:
        return self.limit_weather_cond_d

    def get_name(self) -> str:
        return self.name

    def watering(self) -> None:
        self.weather_cond += 0.25

    def drought(self) -> None:
        self.weather_cond -= 0.25

    def set_weather_cond(self, num: float) -> None:
        if self.weather_cond > 0:
            self.weather_cond -= num

    def ill(self) -> None:
        print(f"У огурца {Cucumber.ills[self.ills]}")
        write_in_file(f"У огурца {Cucumber.ills[self.ills]}")
        Data.set_string(f"У огурца {Cucumber.ills[self.ills]}")
        self.state -= 0.2

    def set_ill(self, ills: int) -> None:
        self.ills = ills

    def get_ill(self):
        return self.ills

    def print_state(self) -> None:
        Cucumber.change_state(self)
        print(f'Огурец сейчас {Cucumber.states[self.state_grow]}')
        write_in_file(f'Огурец сейчас {Cucumber.states[self.state_grow]}')
        Data.set_string(f'Огурец сейчас {Cucumber.states[self.state_grow]}')

    def max_harvest(self) -> int:
        harvest = random.randint(3, 6)
        return harvest

    def get_num_harvest(self) -> int:
        return self.num_harvest
