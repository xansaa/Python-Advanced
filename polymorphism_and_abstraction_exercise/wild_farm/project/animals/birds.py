from project.food import Meat, Fruit, Vegetable, Seed
from project.animals.animal import Bird


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Cluck"

