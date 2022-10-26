"""Basics of the game."""
from random import randint

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

    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
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
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

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

    BRIEF_DESC_CHAR_CLASS: str = ('дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    """
    A distant combat Character.

    Specifies character's stats for mage.
    """

    BREIF_DESC_CHAR_CLASS: str = ('находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    """
    A support Character.

    Specifies character's stats for healer.
    """

    BREIF_DESC_CHAR_CLASS: str = ('могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'
