from random import randint as guess_number

def generatingRandomNumber():
    """ """
    random_number = guess_number(1, 100)

def guessingUserNumber(rand):
    initial_guess = 0

    print("Guessing AI")
    print("RULES: \n I have selected an integer number less than 100.\n ")

    while True:
        guess_input = int(input("You are to guess these number.\n What is the number: "))
        initial_guess += 1

        if guess_input > rand:
            print("Your guessed number{guess_input} is too high. Please, try again...")
        if guess_input < rand:
            print("Your guessed number{guess_input} is too low. Please, try again...")
        else:
            print("Well Done. You have guess the number {guess_input} correctly.")
            break

if __name__ == "__main__":
    rand = generatingRandomNumber()
    guessingUserNumber(rand)


