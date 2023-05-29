#                                                      ----====||||[HANGMAN]||||====----                                                          #

# IMPORTING ⇓

import random

# VARIABLES (ʏ)

words = ["number", "house", "friend", "troublesome", "fantastic", "japan", "anime", "movie",
         "chilling", "adventures", "mildly", "chocolate", "pizza", "handsome", "seriously"]
word = random.choice(words)
display = ["_" for letter in word]
print(" ".join(display))
guesses = 6

# MAIN GAME LOOP (↻)

while guesses > 0:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print(" ".join(display))

        if "_" not in display:
            print("Congratulations! You guessed the word!")
            break
    else:
        guesses -= 1
        print("Incorrect. You have", guesses, "guesses left.")

# Display the hangman figure

        if guesses == 5:
            print('''
 ________
|        |
|        O
|
|
|             
''')
        elif guesses == 4:
            print('''
 ________
|        |
|        O
|        |
|
|
''')
        elif guesses == 3:
            print('''
 ________     
|        |
|        O
|       /|
|
|
''')
        elif guesses == 2:
            print('''
 ________
|        |
|        O
|       /|\\
|
|
''')
        elif guesses == 1:
            print('''
 ________
|        |
|        O
|       /|\\
|       /
|
''')
        else:
            print('''
 ________
|        |
|        O
|       /|\\
|       / \\
|             
''')
print("Game over. The word was", word)
