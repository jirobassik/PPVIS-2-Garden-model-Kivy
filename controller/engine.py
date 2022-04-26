class EngineController:
    def __init__(self, model):
        self.model = model

    def press_main_button(self):
        if not self.model.check_length():
            self.model.change_week()
            self.model.long_watering_drought()
            self.model.check_weather_cond()
            self.model.grow_all()
            self.model.grow_weed()
            self.model.are_all_ripe(2)

    def collect_harvest(self):
        self.model.choice_collect_harvest()

    def reset_notify(self):
        self.model.set_check_notify(False)

    def clear_notify_model(self):
        self.model.clear_notify_data()

    def clear_notify_model_harvest(self):
        self.model.clear_notify_data_harvest()

    def reset_notify_harvest(self):
        self.model.set_check_notify_harvest(False)

    def clear_screen(self):
        self.model.clear_data()

    def weeding(self):
        self.model.weeding()

    def fertilizer(self):
        self.model.fertilizer()

    def watering(self):
        self.model.watering()

    def notify(self, view):
        self.model.notify(view)

    def notify_harvest(self, view):
        self.model.notify_harvest(view)

    def add_plants(self):
        self.model.add_new_rand_plants(3)

    def set_string(self, string):
        self.model.set_strings(string)

    def clear_history(self):
        self.model.clear_old_history()

    def set_pop_el(self):
        self.model.set_pop_el()

    def set_pop_el_for_image(self):
        self.model.set_pop_el_for_image()




