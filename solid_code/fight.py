import random
from abc import ABC, abstractmethod


class Fight(ABC):  # Абстрактный класс атаки героя.
    def __init__(self):
        self.attack_list = (self.fight_one, self.fight_two)

    def attack(self):  # Метод для всех наследуемых классов. Герой выбирает рандомную атаку из доступных.
        my_attack = random.choice(self.attack_list)
        return my_attack()

    @abstractmethod
    def fight_one(self):  # Первый переопределяемый для наследуемых классов метод боя.
        pass

    @abstractmethod  # Второй переопределяемый для наследуемых классов метод боя.
    def fight_two(self):
        pass


class Karate(Fight):  # Наследуемый класс атаки героя. Рукопашный бой.
    def __init__(self):
        super(Karate, self).__init__()

    def fight_one(self):  # Удар ногой.
        print('Bump')

    def fight_two(self):  # Удар рукой.
        print('Ajjjja')


class Gun(Fight):  # Наследуемый класс атаки героя. Огнестрельное оружие.
    def __init__(self):
        super(Gun, self).__init__()

    def fight_one(self):  # Выстрел из пистолета.
        print('PIU PIU')

    def fight_two(self):  # Автоматная очередь.
        print('Tratatatata')


class Superpowers(Fight):  # Наследуемый класс атаки героя. Суперсилы.
    def __init__(self):
        super(Superpowers, self).__init__()

    def fight_one(self):  # Стрельба лазером.
        print('Wzzzuuuup!')

    def fight_two(self):  # Заморозка.
        print('Freeeeze!')


karate = Karate()
makarov = Gun()
laser = Superpowers()
