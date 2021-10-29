selection = input("Please choose a word: ").lower()
incorrect_guesses = []

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# You could also suggest making it more robust by creating a list of plyer 2's
# incorrect guesses.
# Then if the user accidentally guesses the same thing twice, they won't
# be penalised.

picture_count = 0

selection_list = list(selection)
word_length = len(selection_list)

display_list = [" - "] * word_length

lives = 6


def is_game_finished():
    if " - " not in display_list:
        return True


while not is_game_finished():
    user_guess = input("Pick a letter: ")
    if user_guess.lower() not in selection_list:
        if user_guess in incorrect_guesses:
            print("You've already guessed this letter.")
            print(f"{user_guess} is not in the word.")
            print(f"Number of lives remaining: {lives}")
        else:
            print(f"Too bad... {user_guess} is not in the word.")
            lives -= 1
            print(f"Number of lives remaining: {lives}")
            incorrect_guesses.append(user_guess)
            picture_count += 1
    for position in range(word_length):  # This is replacing the spaces with the correct letter
        letter = selection[position]
        if letter == user_guess:
            display_list[position] = letter

    for character in display_list:
        print(character, end=' ')
    print(HANGMANPICS[picture_count])

    if lives == 0:
        print("PLAYER 1 WINS!!")
        print(f"The word was: {selection}")
        break

if is_game_finished():
    print("PLAYER 2 WINS!!")

input('\nPress ENTER to exit')
