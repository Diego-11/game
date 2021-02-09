import abc
import typing
from rx.subject import Subject 

    from logic.events.monsterdead import MonsterDead

if typing.TYPE_CHECKING:
    from logic.weapons.weapon import Weapon
    from logic.events.event import Event


class Monster(metaclass=abc.ABCMeta):
 
    def _init_(self,
               HealthMax: int,
               Weapon: 'Weapon',
               Name: str):
        self.HealthMax = HealthMax
        self.Weapon = Weapon
        self.Name = Name
        self.Health = HealthMax
        self.eventObersabable: Subject['Event'] = Subject()

    def getAttackPoints(self) -> int:
        return self.Weapon.getAttackPoints

    def takeDamage(self, monster: 'Monster') -> none:
        self.Health -= monster.getAttackPoints()
        if self.Health < 0:
            self.Health = 0
            self.dead()

    def attack(self, monsterTakeDamage: 'Monster') -> None:
    monsterTakeDamage.takeDamage(self)

    def dead(self) -> None:
        self.eventObersabable.on_next(MonsterDead())
        self.eventObersabable.on_completed()
