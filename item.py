# TODO: make this stuff work

class Item:
    types = ["weapon", "boots", "helmet", "chestplate", "food", "healing", "storyitem"]
    def __init__(self, name, type, worth):
        self.name = name
        self.worth = worth

        if type in types:
            self.type = type
        else:
            raise TypeError("Type of item has to be one of these: " +  "".join(item + ", " for item in types))

    def get_name(self):
        return self.name

    def get_worth(self):
        return self.worth

    def get_type(self):
        return self.type

    def set_name(self, value):
        self.name = value

    def set_worth(self, value):
        self.worth = value

    def set_type(self, value):
        self.type = value
