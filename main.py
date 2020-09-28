import random

print("COWS AND BULLS: Single Player")
print("""Instructions:
You are guessing the 4-Digit number in my mind
No repetitions
"B" represents the number you guessed consists digit(s) which are in the right position
"C" represents the number you guessed consists digits that are correct but not in their exact position
Use your deductive skills to chase my number down
Type "key" in guess box to get the key and "hint" to get one hint per match
All the best!!""")


def game():

    k = 0
    while True:
        guess = str(input(f"""Guess{k+1}(Type "key" to reveal the number and "hint" to get a hint):"""))
        cows = 0
        bulls = 0
        if guess == "key":
            print(first+last)
            print("Game ends here! Better luck next time")
            replay()
        elif guess == "hint":
            print(f"{(first+last)[1]} is there in the secret number.........You're hints are over:(")
        elif len(guess) != 4 or len(guess) != 3:
            print("Invalid Input")
        else:
            k += 1
            for i in range(4):
                if guess[i] == (first+last)[i]:
                    bulls += 1
                elif guess[i] in first+last:
                    cows += 1
            print(f"""{bulls} digit(s) is/are in the right place
{cows} digit(s) is/are not in the right position
{4 - (cows+bulls)} digits is/are not in the number you guessed
One more try!!""")
            if bulls == 4:
                print("You won!!")
                print(f"You took {k} guess(es)")
                break


def replay():

    re = str(input("Do you want to play again(yes/no)? ")).lower()
    if re == "yes":
        game()
    else:
        exit(1)


digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(digits)
first = [digits[0]]
digits[0] = "0"
random.shuffle(digits)
last = digits[0:3]
game()
replay()
