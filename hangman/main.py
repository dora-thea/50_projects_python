import random

word_list = ['awkward', 'axiom', 'bagpipes', 'beekeeper', 'bookworm', 'cycle', 'funny', 'galaxy', 'hyphen',
             'ice', 'jelly', 'khaki', 'length', 'matrix', 'nymph', 'pixel', 'queue', 'quiz', 'rhythm', 'staff',
             'subway', 'true', 'uptown', 'vodka', 'wave', 'wizard', 'xylophone', 'yummy', 'zigzag', 'zipper']


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries_left):
    stages = [
        # final state
        '''
        ________
        |      |
        |      O
        |     /|\\
        |      |
        |     / \\
        |___
        ''',
        # 1 attempt left
        # head, torso, arms, left leg
        '''
        ________
        |      |
        |      O
        |     /|\\
        |      |
        |     / 
        |___
        ''',
        # 2 attempts left
        # head, torso, arms
        '''
        ________
        |      |
        |      O
        |     /|\\
        |      |
        |     
        |___
        ''',
        # 3 attempts left
        # head, torso, left arm
        '''
        ________
        |      |
        |      O
        |     /|
        |      |
        |     
        |___
        ''',
        # 4 attempts left
        # head and torso
        '''
        ________
        |      |
        |      O
        |      |
        |      |
        |     
        |___
        ''',
        # 5 attempts left
        # head
        '''
        ________
        |      |
        |      O
        |    
        |      
        |    
        |___
        ''',
        # initial state
        '''
        ________
        |      |
        |     
        |     
        |      
        |  
        |___
        '''
    ]
    return stages[tries_left]


def play(word):
    word_progress = word[0] + '_' * (len(word) - 2) + word[len(word) - 1]
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play!")
    display_hangman(6)
    print(word_progress, '\n')

    while not guessed and tries > 0:
        guess = input("Enter a letter or full word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You’ve already named this letter", guess)
            elif guess not in word:
                print('The letter', guess, 'is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Congrats, the letter', guess, 'is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_progress)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_progress = ''.join(word_as_list)
                if '_' not in word_progress:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You’ve already named this word', guess)
            elif guess != word:
                print('The word', guess, 'is incorrect.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_progress = word
        else:
            print('Enter a letter or full word.')
        print(display_hangman(tries))
        print(word_progress, '\n')

    if guessed:
        print("Congrats, you won!")
    else:
        print("You didn’t guess the word. The word: " + word + ". Maybe next time!")


def main():
    again = True
    while again:

        word = get_word()
        play(word)

        print("Would you like to play again? Y - yes, N - no.")
        user_ans = input().upper()
        if user_ans == "Y":
            continue
        elif user_ans == "N":
            print("Thanks for playing. See you later...")
        else:
            print("I couldn't understand you. Goodbye :(")
        again = False


main()
