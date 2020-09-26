import random

print("COWS AND BULLS: Single Player")
print("""Instructions:
You are guessing the 4-Digit number in my mind
No repetitions
"B" represents the number you guessed consists digit(s) which are in the right position
"C" represents the number you guessed consists digits that are correct but not in their exact position
Use your deductive skills to chase down my number
All the best!!""")


def game():

    k = 0
    while True:
        k += 1
        guess = str(input(f"Guess{k}: "))
        cows = 0
        bulls = 0
        if len(guess) != 4:
            print("Invalid Input")
        else:
            for i in range(4):
                if guess[i] == (first+last)[i]:
                    bulls += 1
                elif guess[i] in first+last:
                    cows += 1
            print(f"{bulls}B {cows}C")
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
