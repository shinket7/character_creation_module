"""Basics of the game."""
from random import randint
from typing import Callable

# Default attack and defence values.
DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    """
    General class of a Character.

    Methods:
    attack  -- Do all stuff with a character's attack.
    defence -- Do all stuff with a character's defence.
    special -- Do all stuff with a character's special.
    """

    BRIEF_DESC_CHAR_CLASS: str = 'Отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    SPECIAL_BUFF: int = 15
    SPECIAL_SKILL: str = 'Удача'

    def __init__(self, name: str) -> None:
        """
        Create a Character.

        name -- (str) The name of the character.
        """
        self.name: str = name

    def __str__(self) -> str:
        """Return character description string."""
        return self.BRIEF_DESC_CHAR_CLASS

    def attack(self) -> str:
        """
        Do all stuff with a character's attack.

        Return string with phrase with character's name
        and generated attack value based on range of attack values
        and default attack constant.
        """
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, '
                f'равный {value_attack}')

    def defence(self) -> str:
        """
        Do all stuff with a character's defence.

        Return string with phrase with character's name
        and generated defence value based on range of defence values
        and default defence constant.
        """
        value_defence: int = (
            DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        )
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self) -> str:
        """
        Do all stuff with a character's special.

        Return string with phrase with character's name, special name
        and special's value.
        """
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')


class Warrior(Character):
    """
    A melee combat Character.

    Specifies character's stats for warrior.
    """

    BRIEF_DESC_CHAR_CLASS: str = (
        'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.'
    )
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    """
    A distant combat Character.

    Specifies character's stats for mage.
    """

    BRIEF_DESC_CHAR_CLASS: str = (
        'Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.'
    )
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    """
    A support Character.

    Specifies character's stats for healer.
    """

    BRIEF_DESC_CHAR_CLASS: str = ('Лекарь — могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов.')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Return spesified Character class."""
    game_classes: dict = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = ''
    while approve_choice != 'y':
        selected_class = input(
            'Введи название персонажа, за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: '
        ).lower()
        if selected_class in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
        else:
            char_class = Character(char_name)
        print(selected_class)
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа '
        ).lower()
    return char_class


def start_training(character: Character) -> None:
    """Do training. Print phrases of training process."""
    cmd_dict: dict[str, Callable[[], str]] = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }

    # Printing code that uses dictionaries above.
    print(character)
    print(
        'Потренируйся управлять своими навыками.',
        'Введи одну из команд:',
        'attack — чтобы атаковать противника',
        'defence — чтобы блокировать атаку противника',
        'special — чтобы использовать свою суперсилу',
        'Если не хочешь тренироваться, введи команду skip.',
        sep='\n'
    )
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ').lower()
        if cmd in cmd_dict:
            print(cmd_dict[cmd]())
    print('Тренировка окончена.')
    return


if __name__ == '__main__':
    print(
        'Приветствую тебя, искатель приключений!',
        'Прежде чем начать игру...',
        sep='\n'
    )
    chosen_name: str = input('...назови себя: ')
    print(f'Здравствуй, {chosen_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    chosen_class: Character = choice_char_class(chosen_name)
    start_training(chosen_class)
