from .monster import Monster
from new_struct.weapons.sword import Sword
from new_struct.events.playerdead import PlayerDead

class Player(Monster):
    
    def _init_(self, nombre: str):
        super()._init_(10, Sword(), nombre)

    def cureHimself(self) -> None:
        self.Heatlh += 4
        if self.Heatlh > self.HealthMax:
            self.Heatlh = self.HealthMax

    def dead(self) -> None:
        self.eventObersabable.on_next(playerDead())
        self.eventObersabable.on_completed()
