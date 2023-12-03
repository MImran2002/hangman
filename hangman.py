######################################################################
# Author: Nyan Lin Zaw
# Username: zawn
# Assignment: Hangman
#
# Purpose: Create a Flow Chart, create a hangman game
#
######################################################################
# Acknowledgements: APPBrewery 100 Days of Code: The Complete Python Bootcamp for 2023- Dr Angela Yu
#
# None: AppBrewery's work
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import random
from pics import logo
from pics import stages
from words import word_list

random_word = word_list[random.randint(0, 2)]
change_word = list(random_word)
num_random_word = len(random_word)
print (logo + "\nThe solution is gnostic")
blank = list("_" * num_random_word)
print(blank)
counter = 6
while list(random_word) != blank:

    guess = input("Guess a word: ").lower()
    if change_word.count(guess) > 0:
        for word in random_word:
            if word == guess:
                hehe = change_word.index(guess)
                change_word[hehe] = 1
                blank[hehe] = word
        print(blank)
        if list(random_word) == blank:
            print("You have won!")
    else:
        print("You guess "+ guess +", that's not in the word. You lost a life.")
        counter = counter - 1
        print(stages[counter])
        if counter == 0:
            print("You have lost")
            exit()


