import random


def read_file():
    """This function reads the file with words

    Returns:
        [list] -- [list of words]
    """
    words = []
    with open('./archivos/data.txt', 'r', encoding="utf-8") as f:
        for line in f:
            words.append(line.strip())
    return words


def get_word(words):
    """This function selects a random word from the list of words

    Returns:
        [str] -- [word]
    """
    word = random.choice(words)
    return word.upper()


def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hangman!")
    print(word_complete)
    print("\n")
    print('Tries: {}', tries)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indexes = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indexes:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print("Not a valid guess.")
        print(word_complete)
        print("\n")
        print("Tries: {}", tries)
    if guessed:
        print("Congratulation! You guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was {}".format(word))


def run():
    """function to run the hangman script challenge

    Returns:
        [str] -- [word]
    """
    words = read_file()
    word = get_word(words)
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = get_word(words)
        play(word)


if __name__ == '__main__':
    run()
