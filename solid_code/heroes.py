from fight import Fight, laser, karate, makarov


class SuperHero:  # Класс супергероя.
    def __init__(self, name, weapon: Fight):
        self.name = name
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()


Superman = SuperHero('Superman', laser)
Jackie = SuperHero('Jackie Chan', karate)
Chuck = SuperHero('Chuck Norris', makarov)
Clark = SuperHero('Clark Kent', karate)