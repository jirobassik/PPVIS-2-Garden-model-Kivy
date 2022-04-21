import keyboard
from model.engine import Garden
from utility.write_in_file import write_in_file
from venv import logger

print('Для начала нажмите >')
f = open('D:\Programs\PyCharm Community Edition 2021.2.3\Project\PPVIS4\model\data history\history.txt', 'w')
f.close()
while True:
    b = input()
    match b:
        case ">":
            write_in_file(">")
            keyboard.send("ctrl+l")
            print('Номер недели, природные явления, состояние погоды:')
            write_in_file('Номер недели, природные явления, состояние погоды:')
            Garden.change_week()
            Garden.long_watering_drought()
            print()
            Garden.check_weather_cond()
            Garden.grow_all()
            Garden.grow_weed()
            Garden.are_all_ripe(1)
            Garden.choice_collect_harvest()
            print('\nВзаимодействия с грядкой:\nДля прополки грядки нажмите /\nДля удобрения грядки нажмите }'
                  '\nДля полива грядки нажмите {\nДля посадки нового растения нажмите *'
                  '\nДля просмотра урожая нажмите p\nДля просмотра истории нажмите h')
            write_in_file('\nВзаимодействия с грядкой:\nДля прополки грядки нажмите /\nДля удобрения грядки нажмите }'
                          '\nДля полива грядки нажмите {\nДля посадки нового растения нажмите *'
                          '\nДля просмотра урожая нажмите p\nДля просмотра истории нажмите h')
        case "/":
            write_in_file("/")
            Garden.weeding()
        case "}":
            write_in_file("}")
            Garden.fertilizer()
        case "{":
            write_in_file("{")
            Garden.watering()
        case "*":
            write_in_file("*")
            check = False
            try:
                num = int(input("Введите количество растений, которое вы хотите посадить, меньше 4: "))
            except ValueError:
                print("Вы ввели строку, а надо число")
                check = True
            if not check:
                write_in_file(f"Введите количество растений, которое вы хотите посадить, меньше 4: {num}")
                if 0 < num < 4:
                    Garden.add_new_rand_plants(num)
                else:
                    print("Вы ввели неверное количество растений")
                    write_in_file("Вы ввели неверное количество растений")
        case "p":
            if len(Garden.get_harvest()) == 0:
                print("Урожая пока нет")
                write_in_file("Урожая пока нет")
            else:
                print(Garden.get_harvest())
                write_in_file(Garden.get_harvest())
        case "h":
            f = open('D:\Programs\PyCharm Community Edition 2021.2.3\Project\PPVIS4\model\data history\history.txt')
            print(f.read())
            f.close()
        case "c":
            keyboard.send("ctrl+l")
        case _:
            logger.warning("Невалидный аргумент")
            write_in_file("Невалидный аргумент")