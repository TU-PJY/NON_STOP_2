from ui_manager.ingame_manager import *


class Ingame:
    def __init__(self, weapon, p):
        self.weapon = weapon
        self.p = p
        self.x = 0
        self.y = 0
        self.r = 255
        self.g = 255
        self.b = 255
        load_resource(self)

        self.get_y = 0

    def update(self):
        update_ammo_ind(self)

    def draw(self):
        render_ammo_ind(self)

    def handle_event(self):
        pass
