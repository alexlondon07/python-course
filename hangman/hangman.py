# HANGMAN
import random

# STEP ONE
from hangman_words import word_list

# STEP TWO
chosen_word = random.choice(word_list)

# TESTING CODE
print(f'Psst, the solution is {chosen_word}')

# TODO ONE Create an empty List called display. For each letter in the chosen_word, add a "-" to 'display'
# So if the chosen_word wAS "apple", display should be ["-", "_", "-", "-", "-"] with 5 "-" representing
# each letter to guess
display = []
word_length = len(chosen_word)

# Print Logo
from hangman_logo import logo, stages

print(logo)

for _ in range(word_length):
    display += "_"
print(display)

# TODO TWO : Loop through each position in the chose_word:
# If the letter at that position matches 'guess' then revel that letter in the display at that position.
# Example IF the user guessed "p" and the the chosen word was "apple", the display should be  ["-", "p", "p", "-", "-"].
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guest a letter: ").lower()

    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chose_word
    # Then reduce 'lives' by 1
    # If lives goes down to 0 then the game should stop stop and it should print "You lose"
    if guess not in chosen_word:
        # If the user has entered a letter they've already guessed, print the letter and let them know
        print(f"You guessed {guess}, that´s not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(" You win")

    print(stages[lives])
