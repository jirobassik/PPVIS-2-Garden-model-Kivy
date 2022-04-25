from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from controller.engine import EngineController
from model.engine import Garden

controller = EngineController(Garden)

Window.size = (500, 600)


class CreateItem(Screen):
    text = StringProperty()
    text_2 = StringProperty()
    text_3 = StringProperty()
    source = StringProperty()


class MyMainApp(MDApp):
    dialog = None
    dialog_harvest = None
    controller.clear_history()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_widget = Builder.load_file("engine.kv")
        self.check = False
        self.snackbar = None
        self.i = 0
        self.dat = -1
        self.source_mas = ['Plants/Яблоня.png', 'Plants/Огурец.png', 'Plants/Мандарины.png',
                           'Plants/Груша.png', 'Plants/Картофель.png', 'Plants/Помидор.png']
        self.source_image = ['Яблоня', 'Огурец', 'Мандарины', 'Груша', 'Картофель', 'Помидор']
        self.mas = ["5", "4", "3", "2", "1"]
        self.mas_coord = [{"x": 0.713, 'y': 0.165}, {"x": 0.713, 'y': 0.17}, {"x": 0.713, 'y': 0.176},
                          {"x": 0.713, 'y': 0.183}, {"x": 0.713, 'y': 0.195}]

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return self.root_widget

    def main_press(self):
        controller.press_main_button()
        self.change_gif()
        controller.notify(self)
        controller.notify_harvest(self)
        controller.reset_notify()
        controller.clear_notify_model()
        self.root.ids.label_add1.text = Garden.get_data()
        controller.clear_screen()
        self.change_history()

    def set_check(self, check: bool):
        self.check = check

    def notify_garden(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                text="",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def notify_harvest(self, *args):
        if not self.dialog_harvest:
            self.dialog_harvest = MDDialog(
                text="Вы хотите собрать урожай?",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="Да",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.accept
                    ),
                    MDFlatButton(
                        text="Нет",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog_harvest
                    ),
                ],
            )
        self.dialog_harvest.open()

    def close_dialog(self, *args):
        self.dialog.dismiss(force=True)

    def close_dialog_harvest(self, *args):
        controller.set_string("Нет")
        controller.collect_harvest()
        controller.reset_notify_harvest()
        controller.clear_notify_model_harvest()
        self.dialog_harvest.dismiss(force=True)
        self.snackbar = Snackbar(text="Урожай был не собран!")
        self.snackbar.open()
        self.snackbar.duration = 0.2

    def accept(self, *args):
        controller.set_string("Да")
        controller.collect_harvest()
        controller.reset_notify_harvest()
        controller.clear_notify_model_harvest()
        self.dialog_harvest.dismiss(force=True)
        self.snackbar = Snackbar(text="Урожай был собран!")
        self.snackbar.open()
        self.snackbar.duration = 0.2
        self.build_card()

    def callback(self, instance):
        if instance.icon == 'seed-outline':
            controller.add_plants()
            controller.notify(self)
            controller.reset_notify()
            controller.clear_notify_model()
        elif instance.icon == 'watering-can-outline':
            self.snackbar = Snackbar(text="Грядка была полита!")
            controller.watering()
            self.snackbar.open()
            self.snackbar.duration = 0.1
        elif instance.icon == 'spray':
            self.snackbar = Snackbar(text="Грядка была удобрена!")
            controller.fertilizer()
            self.snackbar.open()
            self.snackbar.duration = 0.1
        elif instance.icon == 'rake':
            self.snackbar = Snackbar(text="Грядка была прополена!")
            controller.weeding()
            self.change_image_grass()
            self.snackbar.open()
            self.snackbar.duration = 0.1
            controller.notify(self)
            controller.reset_notify()
            controller.clear_notify_model()

    def change_dialog_text(self, *args):
        self.dialog.text = Garden.notify_data

    def build_card(self, *args):
        self.root_widget.ids.md_list.add_widget(CreateItem(text=self.build_data_card(),
                                                           text_2=self.build_data_card_2(),
                                                           text_3=self.build_data_card_3(),
                                                           source=self.choose_image(Garden.get_image_for_plants())))

    def build_data_card(self, *args):
        dat = f"{str(Garden.build_data_card(self.dat)[0])}"
        return dat

    def build_data_card_2(self, *args):
        dat = f"Количество: {str(Garden.build_data_card(self.dat)[1][0])}"
        return dat

    def choose_image(self, text):
        if text in self.source_image:
            source = self.source_mas[self.source_image.index(text)]
        return source

    @staticmethod
    def build_data_card_3(*args):
        dat = f"Неделя: {str(Garden.get_week())}"
        return dat

    def change_history(self):
        self.root.ids.history.text = str(Garden.get_history())

    def change_week(self):
        self.root.ids.label_week.text = str(Garden.get_week())

    def clear_screen(self):
        controller.clear_screen()
        self.root.ids.label_add1.text = Garden.get_data()

    def change_image_grass(self):
        if 0 <= Garden.get_grow_weed() < 20:
            self.i = 0
        elif 20 <= Garden.get_grow_weed() < 40:
            self.i = 1
        elif 40 <= Garden.get_grow_weed() < 60:
            self.i = 2
        elif 60 <= Garden.get_grow_weed() < 80:
            self.i = 3
        elif 80 <= Garden.get_grow_weed() < 100:
            self.i = 4
        elif Garden.get_grow_weed() > 100:
            self.i = 4

        self.root.ids.grass_image.source = f'Grass/Grass{self.mas[self.i]}.png'
        self.root.ids.grass_image.pos_hint = self.mas_coord[self.i]

    def gif_drought(self):
        self.root.ids.loading_animation_gif.source = 'Gif/Drought.zip'
        self.root.ids.loading_animation_gif.anim_delay = 0.2

    def gif_rain(self):
        self.root.ids.loading_animation_gif.source = 'Gif/Rain.zip'
        self.root.ids.loading_animation_gif.anim_delay = 0.1

    def gif_silence(self):
        self.root.ids.loading_animation_gif.source = 'Gif/Silence.zip'
        self.root.ids.loading_animation_gif.anim_delay = 0.03

    def gif_sun(self):
        self.root.ids.loading_animation_gif2.source = 'Gif/Sun.zip'
        self.root.ids.loading_animation_gif2.anim_delay = 0.15

    def gif_cloudy(self):
        self.root.ids.loading_animation_gif2.source = 'Gif/Cloudy.zip'
        self.root.ids.loading_animation_gif2.anim_delay = 0.175

    def change_gif(self):
        if Garden.get_weather_cond() == "Ливень":
            self.gif_rain()
            self.gif_cloudy()
        if Garden.get_weather_cond() == "Засуха":
            self.gif_drought()
            self.gif_sun()
        if Garden.get_weather_cond() == "Нет":
            self.gif_silence()
            if Garden.get_weather() == "Ясная":
                self.gif_sun()
            elif Garden.get_weather() == "Пасмурная":
                self.gif_cloudy()


if __name__ == "__main__":
    MyMainApp().run()
