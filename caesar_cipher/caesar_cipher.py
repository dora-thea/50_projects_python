alphabets = [
    # russian upper
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
    # english upper
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    # russian lower
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    # english lower
    'abcdefghijklmnopqrstuvwxyz'
]


def secure_caesar(text, lang_code, alph_size):
    line = [s for s in text.split()]
    answer = []
    for word in line:
        length = 0
        new_word = ""
        for c in word:
            if c.isalpha():
                length += 1
        for c in word:
            if c.isupper():
                new_word += alphabets[lang_code][(alphabets[lang_code].find(c) + length) % alph_size]
            elif c.islower():
                new_word += alphabets[lang_code + 2][(alphabets[lang_code + 2].find(c) + length) % alph_size]
            else:
                new_word += c
        answer.append(new_word)
    return " ".join(answer)


def encrypt(line, step, lang_code, alph_size):
    new_line = ""
    for c in line:
        if c.isupper():
            new_line += alphabets[lang_code][(alphabets[lang_code].find(c) + step) % alph_size]
        elif c.islower():
            new_line += alphabets[lang_code + 2][(alphabets[lang_code + 2].find(c) + step) % alph_size]
        else:
            new_line += c
    return new_line


def decrypt(line, step, lang_code, alph_size):
    new_line = ""
    for c in line:
        if c.isupper():
            new_line += alphabets[lang_code][(alphabets[lang_code].find(c) - step) % alph_size]
        elif c.islower():
            new_line += alphabets[lang_code + 2][(alphabets[lang_code + 2].find(c) - step) % alph_size]
        else:
            new_line += c
    return new_line


def get_language(line):
    is_ru, is_en = False, False
    for c in line:
        if c.upper() in alphabets[0]:
            is_ru = True
        elif c.upper() in alphabets[1]:
            is_en = True
        if is_ru and is_en:
            return 'error'
    if is_ru:
        return 'ru'
    elif is_en:
        return 'en'
    else:
        # another language...
        return 'error'


def get_alphabet_encoding(language):
    if language == 'ru':
        return 0, 33
    elif language == 'en':
        return 1, 26
    else:
        # error, mixed text
        return -1, -1


def is_valid(user_input):
    return user_input.isdigit()


def main():
    again = True
    while again:
        print('Hello! This program encrypts/decrypts text with the Caesar cipher.')

        operation = input("Do you want to decrypt or encrypt your text? (D - decrypt, E - encrypt)\n")
        if operation.lower() == 'd':
            operation = "decrypt"
        elif operation.lower() == 'e':
            operation = "encrypt"
        else:
            print("You entered incorrect data. Please, be careful")
            main()

        print(f"Please enter the string you want to {operation}. Languages available: english and russian.")
        line = input()
        language_code, alph_size = get_alphabet_encoding(get_language(line))
        if language_code == -1:
            print("You entered incorrect text. Please, use only one language: english or russian.")
            main()

        print(f"Please, enter the {operation}ion step.")
        step = input()
        while True:
            if is_valid(step):
                step = int(step) % alph_size
                break
            else:
                print("Step must be an integer!")

        if operation == "encrypt":
            print(encrypt(line, step, language_code, alph_size))

            print("\nBonus! Secure encryption: each word of a string is encrypted with a cyclic shift to the length "
                  "of the word.")
            print(secure_caesar(line, language_code, alph_size), '\n')
        else:
            print(decrypt(line, step, language_code, alph_size), '\n')

        print("Would you like to do this again? Y - yes, N - no.")
        user_ans = input().upper()
        if user_ans == "Y":
            print()
            continue
        elif user_ans == "N":
            print("Thanks. See you later...")
        else:
            print("I couldn't understand you. Goodbye :(")
        again = False


main()
