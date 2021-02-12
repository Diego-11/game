from new_struct.weapons.sword import Sword
from monster import Monster

class Goblin(Monster):

    def _init_(self):
        super()._init_(5, Sword(), "Goblin")
