#create a wordlist
#randomly choose a word from the list you've created
#make the program take input from the user and make it lowecase
#check if the letter is in the word 
import random
import time
print("Welcome to Hangman!")
time.sleep(2)
words = ["random", "bounty", "hacker"]
secret_word = random.choice(words)
print("You only get 5 guesses")
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

num = 0
game_over = False
while not game_over:
    guess = input("Guess any random letter from the alphabets: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
       num += 1
       guesses_left = 5 - num
       print(f"You have {guesses_left} guesses left")
       if num >= 5:
          print("You loser")
          game_over = True
    print(display_word)
    if "_" not in display_word:
        print("You win....Initiating life sequence fellow bounty hunter")
        game_over = True
      
