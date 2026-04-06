import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def mask_word(word, reveal_count=2):
    word = word.upper()

    reveal_count = min(reveal_count, len(set(word)))
    letters_to_reveal = random.sample(list(set(word)), reveal_count)

    masked = ""
    for letter in word:
        if letter in letters_to_reveal:
            masked += letter
        else:
            masked += "_"

    return masked


def play(word):
    word_completion = mask_word(word, reveal_count=2)
    guessed = False

    guessed_letters = [letter for letter in word_completion if letter != "_"]
    guessed_words = []
    tries = 4

    print("Let's save the watermelon! ")
    print(display_watermelon(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        # Guessing a letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter:", guess)

            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_as_list[i] = guess

                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        # Guessing the whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word:", guess)

            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        print(display_watermelon(tries))
        print(word_completion)
        print()

    if guessed:
        print("Congrats, you guessed the word! You Win! ")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ".")


def display_watermelon(tries):
    stages = [
        """
        ---------
        |       |
        |
        |
        |
        |
        |
        |
        _________________
        """,
        """
        ---------
        |       |
        |
        |
        |       ____
        |
        |
        |
        _________________
        """,
        """
        ---------
        |       |
        |
        |           |
        |       ____|
        |
        |
        |
        _________________
        """,
        """
        ---------
        |       |
        |
        |       |    |
        |       |____|
        |
        |
        |
        _________________
        """,
        """
        ---------
        |       |
        |       ______
        |       |    |
        |       |____|
        |
        |
        |
        _________________
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)

    while input("Play Again? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
