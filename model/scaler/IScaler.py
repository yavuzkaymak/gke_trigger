from abc import ABC, abstractmethod


class Scaler(ABC):

    @property
    @abstractmethod
    def manifest(self):
        pass

