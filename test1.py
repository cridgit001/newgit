guess_counter = 3

secret_number = 3

while guess_counter:
    guess = int(input('Guess a number between 0-10.'))
    guess_counter -= 1
    if guess == secret_number:
        print("That's right!")
        break
    else:
        print("Sorry, try again.")
else:
    print('You lose.')