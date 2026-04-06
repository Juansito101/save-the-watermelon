
Design


# 1 Problem statement and target audience:
The goal of this project is to create a game similar to hangman. The pool of words will all be percussion instruments. The target audience will be music students or anyone interested in learning perussion instruments.


# 2 Game rules and win/lose conditions:  
You will be asked to play the game and a word will randomly select a secret word from the list. Each word will be masked and you will have to enter a letter to fill in the blanks to complete the word.  If you enter the correct letter, the letter will be revealed.  If incorrect letter is entered, then a slice of a watermelon will be removed.  Try to save the watermelon by guesting the correct letters to reveal the secret percussion instrument word.  You will get 4 attements to guest the correct word before the watermelon is completely sliced up and game over.  


# 3 Core features (must-haves) vs stretch goals (nice to have):
Core features: Words must be masked and patially revealed to the user.  Game must have a while looped back to the begining until the counter of incorrect guesses reaches 4 attempts.  If letter or word is repeated it must remind user that the word or letter has already been guessed.   

Nice to have (optional): hints, scorebord, optional difficulty levels, catagories.


# 4 Basic flow diagram:


1. START
  

2. Call main()
  

3. Get random word (get_word)
  

4. Call play(word)
  

5. Mask word (mask_word)
 


6. Initialize:
- guessed = False
- tries = 4
- guessed_letters
- guessed_words
  


7. Display intro + watermelon + masked word
                  

get_word()
Pick random word from list
→ Return uppercase word
mask_word(word)
Select 2 random unique letters
→ Replace others with "_"
→ Return masked word
display_watermelon(tries)
Return ASCII drawing based on tries (0–4)




# 5 Data design:

Data Flow
word_list → get_word() → word
word → mask_word() → word_completion
User input → updates:
guessed_letters
guessed_words
tries
word_completion
Game loop continues until:
guessed = True OR
tries == 0


# 6 Module/function responsibilities:

Module Responsibility

Main Module from .py file

This module is responsible for:

Running the game
Managing overall program flow
Connecting all functions together

External Module: words
Provides: word_list
Responsibility:
Stores and supplies possible words
Keeps data separate from game logic


1. get_word()

Responsibility:
Selects a random word from word_list

It's function:
Uses random.choice()
Converts word to uppercase

Provides Data


2. mask_word(word, reveal_count=2)

Responsibility:
Creates the partially hidden version of the word

What it does:
Randomly reveals a few letters
Replaces others with a underscore _

Data transformation (input → modified output)

3. play(word)

Responsibility:
Controls the entire game logic

What it does:
Initializes game state
Handles user input
Processes guesses (letter & word)
Updates progress
Controls loop and win/loss conditions
Displays results

This is the Main core controller 

4. display_watermelon(tries)

Responsibility:
Returns the visual of game progress

What it does:
Uses tries as an index
Returns ASCII art stage

UI helper


5. main()

Responsibility:
Starts and restarts the game

This intiates:
Calls get_word()
Calls play()
Handles replay loop


Type of role:
Program entry controller

Responsibility Flow
main()
  ↓
get_word()
  ↓
play(word)
mask_word()
display_watermelon()
(game loop + user interaction)







  



