from words import words
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

get_valid_word(words)

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphanet = set(string.ascii_uppercase)
    used_letters = set()
    print('Welcome to hangman \nYou can only use capitalize letter ')
    lives=int(input('how many lives do you want?'))

    while len(word_letters) > 0 and lives>0 :
        print(f'You have  {lives} lives left !\n  You used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word', ' '.join(word_list))

        user_input = input('Guess a letter')
        if user_input in alphanet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives=lives-1
                print(f'letter is not in the word !')
        elif used_letters in used_letters:
            print('You already guessed that letter,Please try again')
        else:
            print('That not a valid input')
    if lives==0:
        print(f'You lost the word was {word} , good luck next time')

    else:
        print(f'You won ! the word was {word}')


hangman()
