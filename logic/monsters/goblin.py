from logic.weapons.sword import Sword
from logic.monsters.monster import Monster

class Goblin(Monster):

    def _init_(self):
        super()._init_(5, Sword(), "Goblin")
