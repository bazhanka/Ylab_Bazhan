import random


class Place:  # Базовый класс места.
    def __init__(self, name):
        self.name = name

    def get_danger(self):  # Рандомно выбираем опасность.
        list_of_dangers = ('Orcs hid in the forest',
                           'Godzilla stands near a skyscraper',
                           'Villains are robbing a bank')
        current_danger = random.choice(list_of_dangers)
        print(f'{current_danger} in {self.name}')


class Planet(Place):  # Наследуемый класс места, принимающий аргумент "координаты" вместо имени.
    def __init__(self, coordinates: tuple):
        super(Planet, self).__init__(name=coordinates)
        self.name = coordinates


Kostroma = Place('Kostroma')
Tokyo = Place('Tokyo')
London = Place('London')
Jupiter = Place('(23.09089898, 476.02928286625)')
