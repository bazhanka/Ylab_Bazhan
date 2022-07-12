import random


class Fight:  # Основной класс атаки героя. Рукопашный бой.
    def __init__(self):
        self.attack_list = (self.roundhouse_kick, self.punch)

    def roundhouse_kick(self):  # Удар ногой.
        print('Bump')

    def punch(self):  # Удар рукой.
        print('Ajjjja')

    def attack(self):  # Герой выбирает рандомную атаку из доступных.
        my_attack = random.choice(self.attack_list)
        return my_attack()


class Gun(Fight):  # Наследуемый класс атаки героя. Огнестрельное оружие.
    def __init__(self):
        super(Gun, self).__init__()
        self.attack_list = (self.fire_ak47, self.fire_a_gun, self.punch, self.roundhouse_kick)

    def fire_a_gun(self):  # Выстрел из пистолета.
        print('PIU PIU')

    def fire_ak47(self):  # Автоматная очередь.
        print('Tratatatata')


class Superpowers(Fight): # Наследуемый класс атаки героя. Суперсилы.
    def __init__(self):
        super(Superpowers, self).__init__()
        self.attack_list = (self.punch, self.roundhouse_kick, self.incinerate_with_lasers)

    def incinerate_with_lasers(self): # Стрельба лазером.
        print('Wzzzuuuup!')


karate = Fight()
makarov = Gun()
laser = Superpowers()
