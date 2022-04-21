class Collect:
    def __init__(self):
        self.string = ""

    def set_string(self, in_string):
        self.string += in_string + "\n"

    def get_string(self):
        return self.string

    def clear_string(self):
        self.string = ""


Data = Collect()
