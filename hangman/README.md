# Python project "Hangman"

### Project description: 
The program makes a word, and the user has to guess it. Initially, all letters of the word are unknown. A gallows with a noose is also drawn. The user suggests a letter that can be included in this word. If there is such a letter in the word, then the program puts the letter as many times as it occurs in the word. If there is no such letter, a circle in a loop representing the head is added to the gallows. The user continues to guess the letters until he guesses the whole word. For each unsuccessful attempt, another part of the hangman's torso is added (usually there are 6 of them: head, torso, 2 arms and 2 legs.

Starts with the first and last letters known.

### Components of the project:

- Integers (int type);
- Variables;
- Data input/output (input() and print() functions);
- Conditional operator (if/elif/else);
- While loop;
- Break, continue operators;
- Creating custom functions;
- List expressions;
- Working with the random module to generate random numbers.

### Code
```python
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

```

### Output example
```
Let's play!
R____M 

Enter a letter or full word: a
The letter A is not in the word.

        ________
        |      |
        |      O
        |    
        |      
        |    
        |___
        
R____M 

Enter a letter or full word: e
The letter E is not in the word.

        ________
        |      |
        |      O
        |      |
        |      |
        |     
        |___
        
R____M 

Enter a letter or full word: i
The letter I is not in the word.

        ________
        |      |
        |      O
        |     /|
        |      |
        |     
        |___
        
R____M 

Enter a letter or full word: o
The letter O is not in the word.

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     
        |___
        
R____M 

Enter a letter or full word: y
Congrats, the letter Y is in the word!

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     
        |___
        
R_Y__M 

Enter a letter or full word: h
Congrats, the letter H is in the word!

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     
        |___
        
RHY_HM 

Enter a letter or full word: rhytm
Enter a letter or full word.

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     
        |___
        
RHY_HM 

Enter a letter or full word: rhythm

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     
        |___
        
RHYTHM 

Congrats, you won!
Would you like to play again? Y - yes, N - no.
y
Let's play!
M____X 

Enter a letter or full word: a
Congrats, the letter A is in the word!

        ________
        |      |
        |     
        |     
        |      
        |  
        |___
        
MA___X 

Enter a letter or full word: s
The letter S is not in the word.

        ________
        |      |
        |      O
        |    
        |      
        |    
        |___
        
MA___X 

Enter a letter or full word: d
The letter D is not in the word.

        ________
        |      |
        |      O
        |      |
        |      |
        |     
        |___
        
MA___X 

Enter a letter or full word: f
The letter F is not in the word.

        ________
        |      |
        |      O
        |     /|
        |      |
        |     
        |___
        
MA___X 

Enter a letter or full word: g
The letter G is not in the word.

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     
        |___
        
MA___X 

Enter a letter or full word: h
The letter H is not in the word.

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     / 
        |___
        
MA___X 

Enter a letter or full word: j
The letter J is not in the word.

        ________
        |      |
        |      O
        |     /|\
        |      |
        |     / \
        |___
        
MA___X 

You didn’t guess the word. The word: MATRIX. Maybe next time!
Would you like to play again? Y - yes, N - no.
n
Thanks for playing. See you later...
```
