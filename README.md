secret_word = "castle"
guess = ""
guess_count = 0
guess_limit = 3
guess_limit_reached = False

hints = ["1", "2", "3"]
for so in hints:
    print[0]


hint = input("For help type 'help': ")
if hint.upper() == "HELP":
    print("Word we are looking for is a name of a kind of a building")

while guess != secret_word and not(guess_limit_reached):
    if guess_count < guess_limit:
        guess = input("Guess the secret word: ")
        guess_count += 1
    else:
        guess_limit_reached = True

if guess_limit_reached:
    print("You lost!")
else:
    print("You win!")



