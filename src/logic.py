
# Core Module and functions


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


Main core controller 

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



