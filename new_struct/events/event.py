import abc

class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def pinEvent(self):
        pass
