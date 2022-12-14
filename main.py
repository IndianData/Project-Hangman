import random
import art
import dictionary

print(art.logo)
chosen_word = random.choice(dictionary.word_list)
word_length = len(chosen_word)
end_of_game = False

lives = 6
print(
  'Instructions:\n============\n1. Guess the alphabets in a word one at a time.\n2. Every wrong answer, you loose one life.\n3. You have 6 lives in total.\n'
)
#Test code:
#print(f'The solution is {chosen_word}.')

display = []
for _ in range(word_length):
  display += "_"
print(display)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    print(
      f"You guessed {guess}, that's not in the word. You lose a life.\nRemaining lives: {lives}."
    )
    if lives == 0:
      end_of_game = True
      print(
        f'\nYou lose.\nThe word was "{chosen_word}".\nBetter luck next time!')

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(art.stages[lives])
