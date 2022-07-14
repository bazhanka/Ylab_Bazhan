from fight import laser, karate, makarov
from abc import ABC, abstractmethod


class SuperHero(ABC):  # Абстрактный класс супергероя.

    @abstractmethod  # Обязательный метод атаки.
    def attack(self):
        pass


class KarateMan(SuperHero):  # Наследуемый класс супергероя, владеющего ближним боем.
    def __init__(self, name):
        self.name = name

    def attack(self):
        karate.attack()


class SuperMan(SuperHero):  # Наследуемый класс супергероя со суперспособностями.
    def __init__(self, name):
        self.name = name

    def attack(self):
        laser.attack()


class SuperGunMan(SuperHero):  # Наследуемый класс супергероя с оружием.
    def __init__(self, name):
        self.name = name

    def attack(self):
        makarov.attack()


Superman = SuperMan('Superman')
Jackie = KarateMan('Jackie Chan')
Chuck = SuperGunMan('Chuck Norris')
Clark = KarateMan('Clark Kent')
