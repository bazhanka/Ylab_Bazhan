import random
from abc import ABC, abstractmethod


class Place(ABC):  # Абстрактный класс места.

    @abstractmethod
    def get_danger(self):  # Обязательный метод, переопределяемый для наследуемых классов.
        pass


class City(Place):  # Наследуемый класс места, инициирующий объект город.
    def __init__(self, name):
        self.name = name

    def get_danger(self):  # Рандомно выбираем опасность. Переопределенный метод для городов.
        list_of_dangers = ('Orcs hid in the forest',
                           'Godzilla stands near a skyscraper',
                           'Villains are robbing a bank')
        current_danger = random.choice(list_of_dangers)
        print(f'{current_danger} in {self.name}')


class Planet(Place):  # Наследуемый класс места, принимающий аргумент координаты вместо имени.
    def __init__(self, coordinates: tuple):
        self.name = coordinates

    def get_danger(self):  # Рандомно выбираем опасность. Переопределенный метод для планет.
        list_of_dangers = ('Aliens landed',
                           'Dart Waider attacks',
                           'Meteor is coming')
        current_danger = random.choice(list_of_dangers)
        print(f'{current_danger} in {self.name}')


Kostroma = City('Kostroma')
Tokyo = City('Tokyo')
London = City('London')
Jupiter = Planet((23.09089898, 476.02928286625))
