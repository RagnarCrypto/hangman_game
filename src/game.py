import random
from typing import Iterable

from src.game_status import GameStatus
from src.invalid_operation_exception import InvalidOperationException


class Game:

    def __init__(self, allow_misses: int = 6):
        if allow_misses < 5 or allow_misses > 8:
            raise ValueError('Number of allowed misses should be between 5 and 8.')

        self.__allow_misses = allow_misses
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ''

    @property
    def generate_word(self) -> str:
        filename = 'data\\WordsStockRus.txt'

        words = []
        with open(filename, encoding='utf8') as file:
            for line in file:
                words.append(line.strip('\n'))

        rand_word_index = random.randint(0, len(words) - 1)

        self.__word = words[rand_word_index]

        self.__open_indexes = [False for _ in self.__word]

        self.__game_status = GameStatus.IN_PROGRESS

        return self.__word

    def user_letter(self, letter: str) -> Iterable[str]:
        if self.tries_counter == self.allow_misses:
            raise InvalidOperationException(f'Exceeded the max misses numbers, allowed {self.allow_misses}')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(f'Wrong game status {self.game_status}')

        open_any = False
        result = []

        for i, c in enumerate(self.word):

            if c == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(c)
            else:
                result.append('-')

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__is_win():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allow_misses:
            self.__game_status = GameStatus.LOST

        return result

    def __is_win(self):
        for cur in self.__open_indexes:
            if not cur:
                return False
        return True

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def remaining_tries(self) -> int:
        return self.__allow_misses - self.__tries_counter

    @property
    def allow_misses(self) -> int:
        return self.__allow_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def tried_letters(self) -> Iterable[str]:
        return sorted(self.__tried_letters)
