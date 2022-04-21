import random
from model.plants import Plants
from utility.write_in_file import write_in_file
from utility.collect_data import Data

class Mandarin(Plants):
    states = {0: 'отсутствует', 1: 'саженец', 2: 'рост', 3: 'набухание почек', 4: 'распускание почек',
              5: 'цветение', 6: 'созревание', 7: 'созрела', 8: 'опадание'}
    ills = {0: 'появился вредитель - зеленая тля', 1: 'появилась болезнь - черный рак'}

    def __init__(self) -> None:
        self.num_harvest = None
        self.can_harvest = True
        self.name = "Мандарины"
        self.state_grow = 0
        self.state = 0
        self.weather_cond = 0
        self.limit_weather_cond_w = 10
        self.limit_weather_cond_d = -10
        self.ills = None

    def __repr__(self):
        return str(self.__dict__)

    def get_name(self) -> str:
        return self.name

    def grow(self) -> None:
        if self.state < 7:
            self.state += 0.20
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
        if 5 < self.state <= 6:
            self.state_grow = 6
        if 6 < self.state <= 7:
            self.state_grow = 7
        if self.state > 7:
            self.state_grow = 8

    def set_state(self, states) -> None:
        self.state += states

    def is_ripe(self) -> bool:
        if 6 < self.state <= 7:
            return True
        return False

    def is_rotten(self) -> bool:
        if 40 <= self.state <= 90:
            return True
        return False

    def get_weather_cond(self) -> int:
        return self.weather_cond

    def get_can_harvest(self) -> bool:
        return self.can_harvest

    def get_limit_weather_cond_w(self) -> float:
        return self.limit_weather_cond_w

    def get_limit_weather_cond_d(self) -> float:
        return self.limit_weather_cond_d

    def watering(self) -> None:
        self.weather_cond += 0.25

    def drought(self) -> None:
        self.weather_cond -= 0.25

    def set_weather_cond(self, num: float) -> None:
        if self.weather_cond > 0:
            self.weather_cond -= num

    def ill(self) -> None:
        print("У мандаринов {}".format(Mandarin.ills[self.ills]))
        write_in_file("У мандаринов {}".format(Mandarin.ills[self.ills]))
        Data.set_string("У мандаринов {}".format(Mandarin.ills[self.ills]))
        self.state -= 0.2

    def set_ill(self, ills: int) -> None:
        self.ills = ills

    def get_ill(self):
        return self.ills

    def print_state(self) -> None:
        Mandarin.change_state(self)
        print(f'Мандарины сейчас {Mandarin.states[self.state_grow]}')
        write_in_file(f'Мандарины сейчас {Mandarin.states[self.state_grow]}')
        Data.set_string(f'Мандарины сейчас {Mandarin.states[self.state_grow]}')

    def max_harvest(self) -> int:
        harvest = random.randint(50, 75)
        return harvest

    def get_num_harvest(self) -> int:
        return self.num_harvest
