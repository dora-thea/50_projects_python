# Python project for "Secure password generator"

### Project description: 
The program generates a set number of passwords and includes a smart setting for the length of the password, as well as which characters need to be included in it and which ones to exclude.

### Details:
The program should request the following information from the user:
- Number of passwords to generate;
- The length of one password;
- Should the numbers 0123456789 be included?
- Should the uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ be included?
- Should the lowercase letters abcdefghijklmnopqrstuvwxyz be included?
- Whether to include symbols !#$%&*+-=?@^_?
- Should the ambiguous il1Lo0O characters be excluded?

Also this is a strong password generator which necessarily include characters from each selected section.

### Components of the project:

- Variables;
- Data input/output (input() and print() functions);
- Conditional operator (if/elif/else);
- While loop;
- Writing custom functions;
- Foolproof;
- Working with the random module to generate random numbers.

### Code 
```python
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

    print("\nYour passwords:")
    for _ in range(amount_of_passwords):
        print(generate_password(pass_length))


main()

```

### Output example
```
How many passwords you want to generate?
5
Enter the desired password length:
8
Do you want to include digits in your password??(Y - yes)y
Do you want to include uppercase letters in your password?(Y - yes, N - no) y
Do you want to include lowercase letters in your password?(Y - yes, N - no) y
Do you want to include punctuation characters in your password?(Y - yes, N - no) y
Do you want to use ambiguous characters: "iloLO10"?(Y - yes, N - no) n

Your passwords:
_9Qv6fU?
jY8?9f^S
P?*Pe48s
e84Dx*J!
n5*k4J%P
```
