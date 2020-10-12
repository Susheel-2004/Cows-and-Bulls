import random
import time

# instructions
print("COWS AND BULLS: Single Player")
print("""Instructions:
You are guessing the 4-Digit number in my mind
No repetitions
"B" represents the number you guessed consists digit(s) which are in the right position
"C" represents the number you guessed consists digits that are correct but not in their exact position
Use your deductive skills to chase my number down
Type key in guess box to get the key and hint to get one hint per match
All the best!!""")

# Declaring a function for game
def game():

    k = 0
    # loop gives unlimited attempts
    while True:
        guess = str(input(f"""Guess{k+1}(Type "key" to reveal the number and "hint" to get a hint): """))
        cows = 0
        bulls = 0
        # in this code the user guess is split and then checked
        guess.split()
        if guess == "key":
            # empty list
            result = ""
            for element in (first+last):
                # joining the secret number which initially was in a list
                result += str(element)
            print(f"{result} is the hidden number")
            print("Game ends here! Better luck next time")
            replay()
        elif guess == "hint":
            # reveals the second digit of the secret number
            print(f"{(first+last)[1]} is there in the secret number.........You're hints are over:(")
        elif len(set(guess)) != 4:
            print("Invalid Guess. Please guess again")
        else:
            # start of deducing the legal guess
            k += 1
            for i in range(4):
                if guess[i] == (first+last)[i]:
                    bulls += 1
                elif guess[i] in first+last:
                    cows += 1
            print(f"""{bulls} digit(s) is/are in the right place: {bulls}B
{cows} digit(s) is/are not in the right position: {cows}C
{4 - (cows+bulls)} digits is/are not in the number you guessed""")
            if bulls == 4:
                print("You won!!")
                print(f"You took {k} guess(es)")
                break

# replay prompt function(optional)
def replay():
    re = str(input("Do you want to play again(yes/no)? ")).lower()
    if re in ["yes", "ya", "y", "yeah"]:
        print("Game's about to begin", end="")
        for i in range(4):
            time.sleep(1)
            print(".", end="")
        print()
        game()
    elif re in ["no", "n", "nah", "nope"]:
        print("Bye!")
        exit(0)
    else:
        print("I'm not sure I understand that so I'm gonna assume that's a no. BYE!", end="")
        exit(0)

# main source code
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(digits)
first = [digits[0]]
digits[0] = "0"
random.shuffle(digits)
last = digits[0:3]
game()
replay()
