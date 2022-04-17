from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu

Window.size = (500, 600)

class MDScreen(Screen):
    pass

class CreateItem(Screen):
    text = StringProperty()

class ContentForNewWindow(BoxLayout):
    pass



class MyMainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_widget = Builder.load_file("main.kv")

    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return self.root_widget



    def callback(self, instance):
        if instance.icon == 'seed-outline':
            self.create_new_window()
        elif instance.icon == 'watering-can-outline':
            self.snackbar = Snackbar(text="Грядка была полита!")
            self.snackbar.open()
            self.snackbar.duration = 0.1
        elif instance.icon == 'spray':
            self.snackbar = Snackbar(text="Грядка была удобрена!")
            self.snackbar.open()
            self.snackbar.duration = 0.1
        elif instance.icon == 'rake':
            self.snackbar = Snackbar(text="Грядка была прополена!")
            self.snackbar.open()
            self.snackbar.duration = 0.1

    def create_new_window(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                type="custom",
                content_cls=ContentForNewWindow(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def build_card(self):
        self.root_widget.ids.md_list.add_widget(CreateItem(text="Dsada"))

    def presss(self):
        self.root.ids.label_add1.text = "Pojuy"

    def gif_rain(self):
        self.root.ids.loading_animation_gif.source = 'Rain.zip'
        self.root.ids.loading_animation_gif.anim_delay = 0.1

    def gif_sun(self):
        self.root.ids.loading_animation_gif2.source = 'Sun.zip'
        self.root.ids.loading_animation_gif2.anim_delay = 0.15

    def gif_cloudy(self):
        self.root.ids.loading_animation_gif2.source = 'Cloudy.zip'
        self.root.ids.loading_animation_gif2.anim_delay = 0.175

if __name__ == "__main__":
    MyMainApp().run()


