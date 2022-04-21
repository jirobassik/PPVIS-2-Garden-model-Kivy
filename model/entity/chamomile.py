from model.plants import Plants
from utility.write_in_file import write_in_file
from utility.collect_data import Data

class Chamomile(Plants):
    states = {0: 'отсутствует', 1: 'росток', 2: 'распустилась', 3: 'опадает',
              4: 'сгнила', }
    ills = {0: 'появился вредитель - трипсы', 1: 'появилась болезнь - белая гниль'}

    def __init__(self) -> None:
        self.num_harvest = None
        self.can_harvest = False
        self.name = "Ромашка"
        self.state_grow = 0
        self.state = 0
        self.weather_cond = 0
        self.limit_weather_cond_w = 1
        self.limit_weather_cond_d = -1
        self.ills = None

    def __repr__(self):
        return str(self.__dict__)

    def get_name(self) -> str:
        return self.name

    def grow(self) -> None:
        if self.state < 4:
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

    def set_state(self, states) -> None:
        self.state += states

    def is_ripe(self) -> bool:
        if 2 < self.state <= 3:
            return True
        return False

    def is_rotten(self) -> bool:
        if 3 < self.state <= 4:
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
        print(f"У ромашки {Chamomile.ills[self.ills]}")
        write_in_file(f"У ромашки {Chamomile.ills[self.ills]}")
        Data.set_string(f"У ромашки {Chamomile.ills[self.ills]}")
        self.state -= 0.2

    def set_ill(self, ills: int) -> None:
        self.ills = ills

    def get_ill(self):
        return self.ills

    def print_state(self) -> None:
        Chamomile.change_state(self)
        print(f'Ромашка сейчас {Chamomile.states[self.state_grow]}')
        write_in_file(f'Ромашка сейчас {Chamomile.states[self.state_grow]}')
        Data.set_string(f'Ромашка сейчас {Chamomile.states[self.state_grow]}')

    def max_harvest(self) -> None:
        pass

    def get_num_harvest(self) -> int:
        return self.num_harvest
