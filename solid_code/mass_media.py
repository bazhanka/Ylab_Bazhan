from heroes import SuperHero
from places import Place


class MassMedia:  # Базовый класс прессы.
    def __init__(self, name):
        self.name = name

    def create_news(self, hero: SuperHero, place: Place):
        print(f'{self.name} informing! We are just shouting out loud: {hero.name} saved the {place.name}!')


class TV(MassMedia):  # Наследуемый класс прессы - телевидение.
    def __init__(self, name):
        super(TV, self).__init__(name)

    def create_news(self, hero: SuperHero, place: Place):
        print(f'Breaking news on {self.name}! {hero.name} saved the {place.name}!')


class Radio(MassMedia):  # Наследуемый класс прессы - радио.
    def __init__(self, name):
        super(Radio, self).__init__(name)

    def create_news(self, hero: SuperHero, place: Place):
        print(f'Attention! {self.name} in on air! {hero.name} saved the {place.name}!')


class Newspaper(MassMedia): # Наследуемый класс прессы - газета.
    def __init__(self, name):
        super(Newspaper, self).__init__(name)

    def create_news(self, hero: SuperHero, place: Place):
        print(f'What a fact! {self.name} leader page: {hero.name} saved the {place.name}!')


Times = Newspaper('Times')
BBC = TV('BBC')
Liberty = Radio('Liberty')
Bill = MassMedia('Bill')
