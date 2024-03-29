from abc import ABC

from project.animals.animal import Animal


class Cat(Animal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "Meow meow!"
