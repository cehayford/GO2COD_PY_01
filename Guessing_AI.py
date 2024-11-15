from random import randint as guess_number

def generatingRandomNumber():
    """ """
    random_number = guess_number(1, 100)
    return random_number

def guessingUserNumber(rand) -> int:
    initial_guess = 0

    print("Guessing AI")
    print("RULES: \n I have selected an integer number less than 100.\n ")

    while True:
        try:
            guess_input = int(input("You are to guess these number.\n What is the number: "))
            initial_guess += 1
            # print(type(guess_input ))
            if guess_input <=1 or guess_input >= 100:
                print("Guess number is between 1 and 100. Guess within the range...")
                break
            else:
                if guess_input > rand:
                    print(f"Your guessed number {guess_input} is too high. Please, try again...")
                elif guess_input < rand:
                    print(f"Your guessed number {guess_input} is too low. Please, try again...")
                else:
                    print(f"Well Done. You have guess the number {guess_input} and the CPU random number {rand} correctly.")
                    
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 100.")
                

if __name__ == "__main__":
    rand = generatingRandomNumber()
    guessingUserNumber(rand)


