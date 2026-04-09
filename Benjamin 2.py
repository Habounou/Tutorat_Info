import numpy as np
from abc import ABC, abstractmethod


class Forme(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def nom(self):
        pass


class Polygone(Forme):

    def __init__(self, c, a, n):
        super().__init__()
        self.liste_arguments = [c, a, n]

    def aire(self):
        aire = np.prod(self.liste_arguments) / 2
        return aire

    def nom(self):
        return "Polygone"

    @classmethod
    def modif(cls):
        return cls(3, 4, 6)


polygone_1 = Polygone(3, 4, 5)
print(polygone_1.aire())
polygone_1 = polygone_1.modif()
print(polygone_1.aire())
