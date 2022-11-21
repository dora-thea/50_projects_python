#  generate secure passwords

import random

DIGITS = '0123456789'
LO_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UP_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATIONS = '!#$%&*+-=?@^_'
BAD_SYMBOLS = 'il1Lo0O'
chars_for_password = []


def generate_password(length):
    psw = [random.choice(chars_for_password[i % len(chars_for_password)]) for i in range(length)]
    random.shuffle(psw)
    return "".join(psw)


def is_valid(num):
    while True:
        if num.isdigit() and int(num) > 0:
            return int(num)
        print('Enter a whole positive number.')


def set_password_char_settings():
    if input('Do you want to include digits in your password??(Y - yes)').lower() == 'y':
        chars_for_password.append(DIGITS)
    if input('Do you want to include uppercase letters in your password?(Y - yes, N - no) ').lower() == 'y':
        chars_for_password.append(LO_LETTERS)
    if input('Do you want to include lowercase letters in your password?(Y - yes, N - no) ').lower() == 'y':
        chars_for_password.append(UP_LETTERS)
    if input('Do you want to include punctuation characters in your password?(Y - yes, N - no) ').lower() == 'y':
        chars_for_password.append(PUNCTUATIONS)
    if input('Do you want to use ambiguous characters: "iloLO10"?(Y - yes, N - no) ').lower() == 'n':
        for i in range(len(chars_for_password)):
            for c in 'iloLO10':
                chars_for_password[i] = chars_for_password[i].replace(c, '')
    if len(chars_for_password) == 0:
        print('By default, a set of lowercase letters will be used!')
        chars_for_password.append(LO_LETTERS)


def main():
    print("How many passwords you want to generate?")
    amount_of_passwords = is_valid(input())
    print("Enter the desired password length:")
    pass_length = is_valid(input())
    if pass_length < 6:
        print('The minimum password length is 6 characters. A 6-digit password will be generated')
        pass_length = 6

    set_password_char_settings()

    for _ in range(amount_of_passwords):
        print(generate_password(pass_length))


main()
