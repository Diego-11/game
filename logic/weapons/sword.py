from logic.weapons.weapon import Weapon


class Sword(Weapon):
    
    def getAttackPoints(self) -> int:
        return 3

    
    def _str_(self) -> str:
        return "Sword"  

