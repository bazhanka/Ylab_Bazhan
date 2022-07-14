from heroes import SuperHero, Chuck, Jackie, Superman, Clark
from mass_media import MassMedia, BBC, Times, Liberty, Bill
from places import Place, Kostroma, Tokyo, Jupiter, London


def save_the_place(hero: SuperHero, place: Place, media: MassMedia):
    # Функция спасения, принимающая на вход героя, место и медиа. Выводит опасность, атаку героя и новость.
    place.get_danger()
    hero.attack()
    media.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Chuck, Jupiter, Times)
    print('-' * 20)
    save_the_place(Jackie, Tokyo, Liberty)
    print('-' * 20)
    save_the_place(Superman, Kostroma, BBC)
    print('-' * 20)
    save_the_place(Clark, London, Bill)
