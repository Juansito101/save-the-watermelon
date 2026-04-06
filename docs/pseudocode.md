
IMPORT random
IMPORT word_list from words file

FUNCTION get_word
    SELECT random word from word_list
    CONVERT word to uppercase
    RETURN word
END FUNCTION


FUNCTION mask_word(word, reveal_count)
    CONVERT word to uppercase

    GET unique letters from word
    RANDOMLY choose reveal_count letters from unique letters

    SET masked_word = empty string

    FOR each letter in word
        IF letter is in chosen letters
            ADD letter to masked_word
        ELSE
            ADD "_" to masked_word
    END FOR

    RETURN masked_word
END FUNCTION


FUNCTION play(word)
    SET word_completion = mask_word(word, 2)
    SET guessed = false
    SET guessed_letters = letters already revealed in word_completion
    SET guessed_words = empty list
    SET tries = 4

DISPLAY "Let's save the watermelon!"
DISPLAY watermelon drawing based on tries
DISPLAY word_completion

WHILE guessed is false AND tries > 0

ASK user to guess a letter or word
CONVERT guess to uppercase

IF guess is one letter AND alphabetic
            IF guess already in guessed_letters
                DISPLAY "already guessed"
            
ELSE IF guess not in word
                DISPLAY "not in word"
                DECREASE tries by 1
                ADD guess to guessed_letters
            
ELSE
                DISPLAY "correct guess"
                ADD guess to guessed_letters

FOR each position in word
                    IF letter matches guess
                        REVEAL letter in word_completion
END FOR

IF no "_" left in word_completion
                    SET guessed = true
                END IF
            END IF

ELSE IF guess length equals word length AND alphabetic
            IF guess already in guessed_words
                DISPLAY "already guessed word"

ELSE IF guess is not equal to word
                DISPLAY "wrong word"
                DECREASE tries by 1
                ADD guess to guessed_words

ELSE
                SET guessed = true
                SET word_completion = word
            END IF

ELSE
            DISPLAY "invalid guess"
        END IF

        DISPLAY watermelon drawing
        DISPLAY word_completion

END WHILE

IF guessed is true
        DISPLAY "You win"
ELSE
        DISPLAY "You lose" and show correct word
END FUNCTION

FUNCTION display_watermelon(tries)
    STORE list of watermelon stages (5 drawings)
    RETURN stage based on tries index
END FUNCTION

FUNCTION main
    CALL get_word → word
    CALL play(word)

 WHILE user wants to play again
        CALL get_word → word
        CALL play(word)
    END WHILE
END FUNCTION


IF program is main
    CALL main
END IF


