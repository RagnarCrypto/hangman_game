from src.game import Game
from src.game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()

word = game.generate_word

letters_count = len(word)

print(f'The word has {letters_count} letters')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Guess the letter: ')
    state = game.user_letter(letter)

    print(chars_list_to_str(state))
    print(f'remaining tries {game.remaining_tries}')
    print(f'Tried letters: {chars_list_to_str(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
    print('You ara hanged')
    print(f'The word was - {game.word}')
else:
    print('Congratulations')
