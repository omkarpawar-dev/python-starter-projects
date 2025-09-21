import random
print("I am guessing a number form 1-20, Guess it correctly to win!")
secretNum = random.randint(1, 20)
attempt = 0
while True:

    userInput = (input("Guess the Number [Type x to exit]:  "))

    if userInput.lower() == "x":
        break
    if not userInput.isdigit():
        print("Please Enter a valid number")
        continue
    userInput = int(userInput)
    if userInput > 20 or userInput < 1:
        print("Please Enter a number between 1-20")
        continue
    attempt = attempt+1
    if userInput > secretNum:
        print("Too High")
    elif userInput < secretNum:
        print("Too Low")
    else:
        print(f"Congratulations!, you won in {attempt} attempts")
        break
