import random
import hangman_art
import hangman_words
import os

def clear_console():
  os.system('clear') 

print("Welcome to Hangman.\n")
print(hangman_art.HANGMANPICS[0])

random_word = random.choice(hangman_words.words)

random_word_list = []
for letter in random_word:
  random_word_list.append(letter)

random_word_blanks = []
for letter in random_word:
  random_word_blanks.append('_')

print(random_word_blanks)

index = 0
hangman_index = 0
guesses = []

while(random_word_list != random_word_blanks and hangman_index < 6):
  user_guess = input('Guess a letter: \n').lower()
  clear_console()
  print("Welcome to Hangman.\n")

  if user_guess in guesses:
    print('You have already guesses that letter')
    print(hangman_art.HANGMANPICS[hangman_index])
    print(random_word_blanks)
    print(f"Guesses: {guesses}")
    continue

  guesses.append(user_guess)

  if(user_guess in random_word):
    print(f"You guessed {user_guess}. That is in the word.")
    for letter in random_word_list:
      if(letter == user_guess):
        random_word_blanks[index] = random_word_list[index]
      index += 1
  else:
    hangman_index += 1
    print(f"You guessed {user_guess}. That's not in the word. You lose a life.")
    

  print(hangman_art.HANGMANPICS[hangman_index])
  index = 0

  print(random_word_blanks)
  print(f"Guesses: {guesses}")

  if(hangman_index >= 6):
    print('Game Over. You lose.')
    print(f"The word was {random_word}.")
  
  if(random_word_list == random_word_blanks):
    print('Congrats. You win!')
