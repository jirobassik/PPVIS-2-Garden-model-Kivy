import random
import copy

from typing import List

from utility.write_in_file import write_in_file
from venv import logger

from model.plants import Plants
from model.entity.cucumber import Cucumber
from model.entity.potato import Potato
from model.entity.tomato import Tomato
from model.entity.chamomile import Chamomile
from model.entity.narcissus import Narcissus
from model.entity.rose import Rose
from model.entity.apple import Apple
from model.entity.pear import Pear
from model.entity.mandarin import Mandarin
from utility.collect_data import Data


def rand_list_plants() -> list:
    list_plants = []
    mas_plant = init_new_plants()
    for i in mas_plant:
        el1 = mas_plant.index(i)
        el2 = random.randint(0, 2)
        list_plants.append(mas_plant[el1][el2])
    return list_plants


def init_new_plants() -> list:
    potato = Potato()
    cucumber = Cucumber()
    tomato = Tomato()
    chamomile = Chamomile()
    narcissus = Narcissus()
    rose = Rose()
    apple = Apple()
    pear = Pear()
    mandarin = Mandarin()

    mas_plant = [[potato, cucumber, tomato], [chamomile, narcissus, rose], [apple, pear, mandarin]]
    return mas_plant


class EngineGarden:
    _plants: List[Plants] = []
    harvest: dict = {}
    week = 0
    weed = 0
    check_long_dur = 0
    die_status = 0
    lim_die_status = 0
    not_die_status = 0
    ill_die_status = 0
    chance_ill = 0
    choose_plant = 0
    plant_die = 0

    def __init__(self) -> None:
        self.list_of_plants = rand_list_plants()
        self.check_notify = False
        self.check_notify_harvest = False
        self.notify_data = ""
        self.notify_data_harvest = ""
        self.weather = ""
        self.weather_cond = ""
        self.chance = None
        self.duration = None
        self.strings = ""
        self.harv = ""
        self.name_image = ""

        for i in self.list_of_plants:
            self._plants.append(i)

    # -------------Методы для View--------------
    def get_week(self):
        return self.week

    def set_check_notify(self, check_notify: bool):
        self.check_notify = check_notify

    def set_check_notify_harvest(self, check_notify: bool):
        self.check_notify_harvest = check_notify

    def get_check_notify(self):
        return self.check_notify

    def get_check_notify_harvest(self):
        return self.check_notify_harvest

    def get_notify_data(self):
        return self.notify_data

    def get_notify_data_harvest(self):
        return self.notify_data_harvest

    def set_notify_data(self, notify_data: str):
        self.notify_data += notify_data + "\n"

    def set_notify_harvest(self, notify_data: str):
        self.notify_data_harvest += notify_data + "\n"

    def clear_notify_data(self):
        self.notify_data = ""

    def clear_notify_data_harvest(self):
        self.notify_data_harvest = ""

    def set_weather(self, weather):
        self.weather = weather

    def set_stat_weather_cond(self, weather_cond: str):
        self.weather_cond = weather_cond

    def get_weather(self):
        return self.weather

    def get_weather_cond(self):
        return self.weather_cond

    def set_strings(self, strings):
        self.strings = strings

    def set_image_for_plants(self, name):
        self.name_image = name

    def get_image_for_plants(self):
        return self.name_image

    @staticmethod
    def notify(view):
        if Garden.get_check_notify():
            view.notify_garden()
            view.change_dialog_text()

    @staticmethod
    def notify_harvest(view):
        if Garden.get_check_notify_harvest():
            view.notify_harvest()

    @staticmethod
    def get_data():
        return Data.get_string()

    @staticmethod
    def clear_data():
        Data.clear_string()

    @staticmethod
    def set_data(data):
        Data.set_string(data)

    @staticmethod
    def build_data_card(num):
        dat = list(Garden.get_harvest().items())[num]
        return dat

    @staticmethod
    def get_history():
        a_file = open('D:\Programs\PyCharm Community Edition 2021.2.3\Project'
                      '\PPVIS4\model\data history\history.txt', 'r')
        file_content = a_file.read()
        a = str(file_content)
        a += "\n"
        return a

    @staticmethod
    def clear_old_history():
        f = open('D:\Programs\PyCharm Community Edition 2021.2.3\Project\PPVIS4\model\data history\history.txt', 'w')
        f.close()

    # -------------Методы для View--------------

    def get_plants(self) -> list:
        return self._plants

    def collect_harvest(self, plants, num_harvest: int) -> dict:
        self.harvest.update({plants.get_name(): [num_harvest]})
        Garden.set_image_for_plants(plants.get_name())
        return self.harvest

    def get_harvest(self):
        return self.harvest

    @staticmethod
    def check_length():
        if len(Garden.get_plants()) == 0:
            print("Грядка пустая, посадите растение")
            Garden.set_notify_data("Грядка пустая, посадите растение")
            Garden.set_check_notify(True)
            return True
        else:
            return False

    def restart(self):
        print("Возобновление симуляции, будут посажены новые растени, а сорники уничтожены")
        write_in_file("Возобновление симуляции, будут посажены новые растени, а сорники уничтожены")
        Garden.set_notify_data("Возобновление симуляции, будут посажены новые растени, а сорники уничтожены")
        Garden.set_check_notify(True)
        self.weeding()
        self.add_new_rand_plants(3)

    @staticmethod
    def add_new_rand_plants(num_plants: int):
        mas_plants = init_new_plants()
        for i in range(0, num_plants):
            el1 = random.randint(0, 2)
            el2 = random.randint(0, 2)
            if len(Garden.get_plants()) > 0:
                for plants in Garden.get_plants():
                    if mas_plants[el1][el2].get_name() == plants.get_name():
                        print(f'{mas_plants[el1][el2].get_name()} нельзя посадить, так как оно уже есть на грядке')
                        write_in_file('Растение нельзя посадить, так как оно уже есть на грядке')
                        break
                    elif Garden.get_plants().index(plants) == len(Garden.get_plants()) - 1:
                        Garden.get_plants().append(mas_plants[el1][el2])
                        print(f"Посажено новое растение: "
                              f"{Garden.get_plants()[len(Garden.get_plants()) - 1].get_name()}")
                        write_in_file(
                            f"Посажено новое растение: {Garden.get_plants()[len(Garden.get_plants()) - 1].get_name()}")
                        Garden.set_notify_data(f"Посажено новое растение: "
                                               f"{Garden.get_plants()[len(Garden.get_plants()) - 1].get_name()}")
                        Garden.set_check_notify(True)
                        Garden.set_chance_ill(0)
                        break
            elif len(Garden.get_plants()) == 0:
                Garden.get_plants().append(mas_plants[el1][el2])
                print(f"Посажено новое растение: {Garden.get_plants()[len(Garden.get_plants()) - 1].get_name()}")
                write_in_file(
                    f"Посажено новое растение: {Garden.get_plants()[len(Garden.get_plants()) - 1].get_name()}")
                Garden.set_notify_data(f"Посажено новое растение: "
                                       f"{Garden.get_plants()[len(Garden.get_plants()) - 1].get_name()}")
                Garden.set_check_notify(True)
                Garden.set_chance_ill(0)

    @staticmethod
    def grow_all() -> None:
        for plants in Garden.get_plants():
            plants.grow()

    @staticmethod
    def check_rotten() -> None:
        list_plant = copy.copy(Garden.get_plants())
        for plants in list_plant:
            if plants.is_rotten():
                print(f'{plants.get_name()} сгнил. Растение выкапывается из грядки.')
                write_in_file(f'{plants.get_name()} сгнил. Растение выкапывается из грядки.')
                Garden.set_notify_data(f'{plants.get_name()} сгнил. Растение выкапывается из грядки.')
                Garden.set_check_notify(True)
                Garden.get_plants().remove(plants)

    @staticmethod
    def check_weather_cond() -> None:
        list_plant = copy.copy(Garden.get_plants())
        for plants in list_plant:
            if plants.get_weather_cond() >= plants.get_limit_weather_cond_w():
                print(f'{plants.get_name()} потребил слишком много воды, он погиб.\nРастение выкапывается из грядки')
                write_in_file(f'{plants.get_name()} потребил слишком много воды, он погиб.'
                              f'\nРастение выкапывается из грядки')
                Garden.set_notify_data(f'{plants.get_name()} потребил слишком много воды, он погиб.'
                                       f'\nРастение выкапывается из грядки')
                Garden.set_check_notify(True)
                Garden.get_plants().remove(plants)
            elif plants.get_weather_cond() <= plants.get_limit_weather_cond_d():
                print(f'{plants.get_name()} был слишком долго без воды, он погиб.\nРастение выкапывается из грядки')
                write_in_file(f'{plants.get_name()} был слишком долго без воды, он погиб.'
                              f'\nРастение выкапывается из грядки')
                Garden.set_notify_data(f'{plants.get_name()} был слишком долго без воды, он погиб.'
                                       f'\nРастение выкапывается из грядки')
                Garden.set_check_notify(True)
                Garden.get_plants().remove(plants)

    def get_grow_weed(self):
        return self.weed

    def set_grow_weed(self, weed: int) -> None:
        self.weed += weed

    def grow_weed(self) -> None:
        Garden.set_grow_weed(10)
        print(f'Количество сорников в процентах: {self.weed}')
        write_in_file(f'Количество сорников в процентах: {self.weed}')
        if self.weed >= 100:
            list_plant = copy.copy(Garden.get_plants())
            print('Грядка слишком сильно заросла, все растения погибают.')
            write_in_file('Грядка слишком сильно заросла, все растения погибают.')
            Garden.set_notify_data('Грядка слишком сильно заросла, все растения погибают.')
            Garden.set_check_notify(True)
            for plants in list_plant:
                Garden.get_plants().remove(plants)
            Garden.set_chance_ill(0)
            self.restart()

    def check_ill(self) -> None:  # Проблемы
        if self.ill_die_status == 0:
            if self.chance_ill > 30:
                if len(Garden.get_plants()) >= 2:
                    self.choose_plant = random.randint(0, len(Garden.get_plants()) - 1)
                elif len(Garden.get_plants()) == 1:
                    self.choose_plant = 0
                choose_ill = random.randint(0, 1)
                self.ill_die_status += 1
                if len(Garden.get_plants()) > 0:
                    Garden.get_plants()[self.choose_plant].set_ill(choose_ill)
                    Garden.get_plants()[self.choose_plant].ill()
                    self.plant_die = Garden.get_plants()[self.choose_plant]
        elif 1 <= self.ill_die_status < 3:
            self.ill_die_status += 1
        if self.plant_die not in Garden.get_plants():
            self.ill_die_status = 0
        elif self.ill_die_status >= 3:
            print(f'{self.plant_die.get_name()} погибает из-за болезни')
            write_in_file(f'{self.plant_die.get_name()} погибает из-за болезни')
            Garden.set_notify_data(f'{self.plant_die.get_name()} погибает из-за болезни')
            Garden.set_check_notify(True)
            Garden.get_plants().remove(self.plant_die)
            Garden.set_chance_ill(0)
            self.ill_die_status = 0

    def set_sum_chance_ill(self, chance_ill: int) -> None:
        self.chance_ill += chance_ill

    def set_chance_ill(self, chance_ill: int) -> None:
        self.chance_ill = chance_ill

    def set_ill_die_status(self, ill_die_status: int) -> None:
        self.ill_die_status = ill_die_status

    def weeding(self) -> None:
        if self.weed > 0:
            self.weed = 0
            print('Грядка была прополена')
            write_in_file('Грядка была прополена')
        else:
            list_plant = copy.copy(Garden.get_plants())
            print('Вы решили прополоть грядку без сорников, все растения погибают')
            write_in_file('Вы решили прополоть грядку без сорников, все растения погибают')
            Garden.set_notify_data('Вы решили прополоть грядку без сорников, все растения погибают')
            Garden.set_check_notify(True)
            Garden.set_chance_ill(0)
            for plants in list_plant:
                Garden.get_plants().remove(plants)

    def fertilizer(self) -> None:
        print('Грядка была удобрена')
        write_in_file('Грядка была удобрена')
        for plants in Garden.get_plants():
            plants.set_state(0.20)
        self.die_status += 1
        Garden.set_chance_ill(0)
        Garden.set_ill_die_status(0)
        self.lim_die_status = self.lim_die_status + 3
        if self.lim_die_status <= self.week and self.die_status < 3:
            self.die_status = 0
        elif self.die_status == 3:
            list_plant = copy.copy(Garden.get_plants())
            print('Вы чрезмерно использовали удобрение, все растения погибают')
            write_in_file('Вы чрезмерно использовали удобрение, все растения погибают')
            Garden.set_notify_data('Вы чрезмерно использовали удобрение, все растения погибают')
            Garden.set_check_notify(True)
            for plants in list_plant:
                Garden.get_plants().remove(plants)

    def change_week(self) -> None:
        self.week += 1
        print(f'Сейчас {self.week} неделя')
        write_in_file(f'Сейчас {self.week} неделя')

    @staticmethod
    def change_weather(rand: int, rule: int = None) -> None:
        if rand == 0:
            chance = random.randint(0, 1)
            match chance:
                case 0:
                    print('Ясная погода')
                    write_in_file('Ясная погода')
                    Garden.set_weather("Ясная")
                    Garden.set_grow_weed(5)
                    for plants in Garden.get_plants():
                        plants.set_state(0.10)
                        plants.set_weather_cond(0.15)
                case 1:
                    print('Пасмурная погода')
                    write_in_file('Пасмурная погода')
                    Garden.set_weather("Пасмурная")
                    Garden.set_sum_chance_ill(3)
        elif rand == 1:
            match rule:
                case 0:
                    print('Ясная погода')
                    write_in_file('Ясная погода')
                    Garden.set_weather("Ясная")
                    Garden.set_grow_weed(5)
                    for plants in Garden.get_plants():
                        plants.set_state(0.10)
                        plants.set_weather_cond(0.15)
                case 1:
                    print('Пасмурная погода')
                    write_in_file('Пасмурная погода')
                    Garden.set_weather("Пасмурная")

    def long_watering_drought(self) -> None:
        if self.check_long_dur == 0:
            Garden.watering_drought()
        elif self.check_long_dur == 1:
            self.check_long_dur = 0
            print("Ливень продолжает идти в течении 1 недели")
            write_in_file("Ливень продолжает идти в течении 1 недели")
            Garden.set_stat_weather_cond("Ливень")
            for plants in Garden.get_plants():
                plants.watering()
        elif self.check_long_dur == 2:
            self.check_long_dur = 0
            print("Засуха будет продолжатся в течении 1 недели")
            write_in_file("Засуха будет продолжатся в течении 1 недели")
            Garden.set_stat_weather_cond("Засуха")
            for plants in Garden.get_plants():
                plants.drought()

    def watering_drought(self) -> None:
        self.chance = random.randint(0, 3)
        match self.chance:
            case 0:
                print('Осадков и засухи нет')
                write_in_file('Осадков и засухи нет')
                Garden.set_stat_weather_cond("Нет")
                Garden.change_weather(0)
            case 1:
                print('Осадков и засухи нет')
                write_in_file('Осадков и засухи нет')
                Garden.set_stat_weather_cond("Нет")
                Garden.change_weather(0)
            case 2:
                self.duration = random.randint(1, 2)
                if self.duration == 2:
                    self.check_long_dur = 1
                print(f'Начался ливень, он будет идти в течении {self.duration} недель')
                write_in_file(f'Начался ливень, он будет идти в течении {self.duration} недель')
                Garden.set_stat_weather_cond("Ливень")
                Garden.set_grow_weed(10)
                Garden.set_sum_chance_ill(7)
                Garden.change_weather(1, 1)
                for plants in Garden.get_plants():
                    plants.watering()
            case 3:
                self.duration = random.randint(1, 2)
                if self.duration == 2:
                    self.check_long_dur = 2
                print(f'Началась засуха, она будет идти в течении {self.duration} недель')
                write_in_file(f'Началась засуха, она будет идти в течении {self.duration} недель')
                Garden.set_stat_weather_cond("Засуха")
                Garden.set_grow_weed(-10)
                Garden.set_sum_chance_ill(7)
                Garden.change_weather(1, 0)
                for plants in Garden.get_plants():
                    plants.drought()

    @staticmethod
    def watering() -> None:
        print("Грядка была полита")
        write_in_file("Грядка была полита")
        for plants in Garden.get_plants():
            plants.watering()

    def are_all_ripe(self, choice) -> None:
        list_plant = copy.copy(Garden.get_plants())
        Garden.check_rotten()
        Garden.check_ill()
        for plants in list_plant:
            if plants.is_ripe():
                if plants.get_can_harvest():
                    print(f'{plants.get_name()} созрел! Можно собирать!\n')
                    write_in_file(f'{plants.get_name()} созрел! Можно собирать!\n')
                    Garden.set_data(f'{plants.get_name()} созрел! Можно собирать!\n')
                    plants.num_harvest = plants.max_harvest()
                    if choice == 1:
                        self.strings = input("Вы хотите собрать урожай?\n")
                    elif choice == 2:
                        Garden.set_notify_harvest("Вы хотите собрать урожай?")
                        Garden.set_check_notify_harvest(True)

    def choice_collect_harvest(self):
        list_plant2 = copy.copy(Garden.get_plants())
        for plants in list_plant2:
            if plants.is_ripe():
                if plants.get_can_harvest():
                    check = False
                    while not check:
                        match self.strings:
                            case "Да":
                                check = True
                                write_in_file("Да")
                                EngineGarden.collect_harvest(self, plants, plants.num_harvest)
                                print(f"Урожай: {Garden.get_harvest()}")
                                write_in_file(f"Урожай: {Garden.get_harvest()}")
                                print("Урожай был собран")
                                write_in_file("Урожай был собран")
                                Garden.get_plants().remove(plants)
                            case "Нет":
                                check = True
                                print("Урожай был не собран")
                                write_in_file("Урожай был не собран")
                            case _:
                                check = True
                                logger.warning("Невалидный аргумент")
                                write_in_file("Невалидный аргумент")


Garden = EngineGarden()
