import random


digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(digits)
first = [digits[0]]
digits[0] = "0"
random.shuffle(digits)
last = digits[0:3]

k = 0
i = 0
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
