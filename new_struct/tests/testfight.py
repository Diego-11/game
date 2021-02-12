import typing
from new_struct.monsters.goblin import Goblin

if typing.TYPE_CHECKING:
    from logic.monsters.monster import Monster

def takeDamageTest(monsterAttack: 'Monster'):
    goblin = Goblin()
    HealthInitial = goblin.Health
    goblin.eventObservable.suscribe(
        lambda event: print(event)
        )

    for _ in range(3):
        monsterAttack.attack(goblin)

    assert goblin.Health < HealthInitial
    assert goblin.Health == 0
 
def tests():
    takeDamageTest(Goblin())

if __name__ == '__main__':
	tests()