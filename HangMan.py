#hangman
import random

num_guesses = 7
#number of incorrect guesses allowed

print("Welcome to Hangman!")
print("If you guess the wrong letter", num_guesses, "times, Game Over!")
print("Type a lowercase letter and press enter to begin")
#prints welcome to game and rules

word_list = ["chain", "basic", "crowd", "group", "frame", "exist", "local", "joint", "river", "point", "storm", "voice", "world", "apple", "heart", "queen", "young", "visit", "rudimentary", "abyss", "axiom", "voyeurism", "megahertz", "larynx", "daiquiri", "zigzagging", "galvanize", "jiujitsu", "red", "bear", "disc"]
#list of 5 letter words

random_number = random.randint(0, len(word_list)-1) 
#makes random number up to how long the list of words is

ran_word = word_list[random_number]
#takes the random number and matches it with a word

def print_word_slots():
    print(" ".join(word_slots))
#puts the letters guessed and the empty spaces in word_slots together so that the player can see what they are at

def get_user_input():
    user_input = input("Enter guess: ")
    return user_input
#function gets users guess

strike = 0 #number of wrong guesses at the begining of the game

word_slots = ["_"] * len(ran_word)
#creates a list filled with these -> "_" however long the word is and will keep the guessed letters in the right spot 

print_word_slots()
#shows player how many letters are in the word before starting

while strike < num_guesses:
    player_guess = get_user_input() 

    if player_guess not in ran_word:
        strike += 1 #adds one wrong guess to counter
        print("Strike", strike, "out of", num_guesses)

    else:
        for i in range(len(ran_word)): #runs through as many times as the word is long
            if ran_word[i] == player_guess: #checks if each letter is equal to the players guess
                word_slots[i] = player_guess #switches "_" for the correctly guessed letter in word_slots

        print_word_slots()
    if "_" not in word_slots: #if there are npo more black spaces then that means you have guessed all the letters correctly and the game is over
        print("Congratulations! You guessed the word:", ran_word)
        break

if strike == num_guesses: #if you guessed incorrectly 6 times, game over
    print("Game Over! The word was:", ran_word)