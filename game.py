secret_word = "CASTLE" 
guess = "" 
guess_count = 0
guess_limit = 3
guess_limit_reached = False

hints = ["Hint: It is made of stone", "Hint: Nowadays you visit it as a tourist", "Hint: It used to be a place of living for a kings", ""]
hint_count = 0

hint = input("Hi! Welcome to my first Python guessing game. For help type 'help': ")
if hint.upper() == "HELP": 
  print("Word we are looking for is a name of a kind of a building")

while guess.upper() != secret_word and not(guess_limit_reached):
  if guess_count < guess_limit: 
    guess = input("Guess the secret word: ") 
    guess_count += 1 
    print(hints[hint_count]
    hint_count += 1
   else: 
     guess_limit_reached = True

if guess_limit_reached: 
  print("You lost!") 
else: 
  print("You win!")
