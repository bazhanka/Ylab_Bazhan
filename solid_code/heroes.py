from fight import laser, karate, makarov


class SuperHero:  # Класс супергероя.
    def __init__(self, name):
        self.name = name
        self.weapon = karate

    def attack(self):
        return self.weapon.attack()


class SuperMan(SuperHero):  # Наследуемый класс супергероя со суперспособностями.
    def __init__(self, name):
        super(SuperMan, self).__init__(name)
        self.weapon = laser


class SuperGunMan(SuperHero):  # Наследуемый класс супергероя с оружием.
    def __init__(self, name):
        super(SuperGunMan, self).__init__(name)
        self.weapon = makarov


Superman = SuperMan('Superman')
Jackie = SuperHero('Jackie Chan')
Chuck = SuperGunMan('Chuck Norris')
Clark = SuperHero('Clark Kent')
