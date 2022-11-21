# This is a simple number guessing game

from random import randint


def get_right_border():
    while True:
        print("Welcome to the number guessing game! Specify the right border for random number selection:")
        right_border = input()
        if is_valid(right_border):
            return int(right_border)
        else:
            print("Enter an integer!")


def is_valid(user_input):
    return user_input.isdigit()


def game(right_border):
    number = randint(1, right_border)
    attempt_counter = 0
    while True:
        print(f"Enter an integer from 1 to {right_border}!")
        user_number = input()
        # this is a short-circuit operator, so it only evaluates the second argument if the first one is true.
        if is_valid(user_number) and 1 <= int(user_number) <= right_border:
            user_number = int(user_number)
            attempt_counter += 1
            if user_number < number:
                print("Your number is less than the hidden number, try again.")
            elif user_number > number:
                print("Your number is bigger than the hidden number, try again.")
            else:
                print("You won the game!")
                print(f"Number of attempts: {attempt_counter}")
                break
        else:
            print(f"Be careful!")


def main():
    again = True
    while again:

        right_border = get_right_border()
        game(right_border)

        print("Would you like to play again? Y - yes, N - no.")
        user_ans = input().upper()
        if user_ans == "Y":
            continue
        elif user_ans == "N":
            print("Thanks for playing numerical guessing. See you later...")
        else:
            print("I couldn't understand you. Goodbye :(")
        again = False

main()