import random
import time

# introduction to the game

print ("let/'s play hangman")
print ('''
       _________
        |/    |
        |     O
        |   \_|_/
        |     |
        |    / \\
        |   /   \\
    ____|____
    \n''')

# Game instructions:
print('''You get 7 lives to guess the letters in the word.
If you guess incorrectly more of the hangman will appear and you lose a life.
When you have used all of your 7 lives, the man will have hung and you will have lost.
If you guess a correct letter, it will be shown and if you guess the word without using the 7 turns, you win!''')
#credits
print("made by Total Aviation")
print("version 1.0 ")
input("\nPress enter to start the game")

print("Hangman words are based on computer science and Youtube Enjoy ")
# List of words
words = ['variable','string','integer','selection', 'iteration','loop','operator','computerscience']
words1 = ['subscribe','dislikes','likes','Youtube', 'views','upload','Tags','contentcreator']

#Randomly choose a word from the list
secret = random.choice(words1)
secret = random.choice(words)
guessed = ''
turns = 7

while turns > 0:
    missed = 0
    print()
    for letter in secret:
        if letter in guessed:
            print (letter,end=' ')
        else:
            print ('_',end=' ')
            missed = missed + 1
    if missed == 0:
        print ('\n\nYou win!')
        break

    guess = input('\n\nGuess a letter: ')
    guessed = guessed + guess
    if guess not in secret:
        turns = turns - 1
        missed = missed + 1
        print ('Nope.')
        print (turns, 'more turns')

    if turns < 7:
        print('  _________')
        print('   |/    |')
    if turns < 6:
        print('   |     O')
    if turns < 5:
        print('   |   \_|_/')
    if turns < 4:
        print('   |     |')
    if turns < 3:
        print('   |    / \\')
    if turns < 2:
        print('   |   /   \\')
    if turns == 0:
        print(' __|____')
        print ('\nThe answer is', secret)

print("https://github.com/TotalAviationJmyt")
print("version 1.0 ")        
play_again = input("Do you want to restart? Y/N")
if play_again == "Y":
    exec(open("./Hangman-TA.py").read())
else:
    exit()
