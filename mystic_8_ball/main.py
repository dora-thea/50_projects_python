# fortune-telling mystic 8 ball

from random import choice
from time import sleep

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.",
           "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
           "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
           "Concentrate and ask again.",
           "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

def salute():
    print("Hi, I'm a magic ball, and I know the answer to any of your questions")
    print("What's your name?")
    print("Hello,", input())

def divinate():
    print("You can ask your question now")
    input()
    print("Wait...")
    sleep(1)
    print(choice(answers))

def main():
    salute()

    again = True
    while again == True:
        divinate()
        print("Another question? Y - yes, N - no")
        user_ans = input().upper()
        if user_ans == "Y":
            continue
        elif user_ans == "N":
            print("Come back again if you have any questions")
        else:
            print("I couldn't understand you. Don't try to joke with fate! Goodbye")
        again = False

main()