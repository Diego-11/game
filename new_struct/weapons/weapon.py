import abc

class Weapon(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAttackPoints(self) -> int:
        pass

    @abc.abstractmethod
    def _str_(self) -> str:
        pass
