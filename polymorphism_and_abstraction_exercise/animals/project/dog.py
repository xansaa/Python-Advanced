from abc import ABC

from project.animals.animal import Animal


class Dog(Animal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "Woof!"
