import random
from hangman_words import word_list

lives = 6
display = []

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

print(display)

end_of_game = False

while not end_of_game:

    print(f"Lives: {lives}")

    guess = input("Guess a letter: ").lower()

    for index in range(word_length):
        letter = chosen_word[index]

        if letter == guess:
           display[index] = letter

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
