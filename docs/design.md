# 1 Problem statement and target audience:
The goal of this project is to create a game similar to hangman. The pool of words will all be percussion instruments. The target audience will be music students or anyone interested in learning perussion instruments.

# 2 Game rules and win/lose conditions:  
You will be asked to randomly select a secret word from the list.  Each word will be masked and you will have to enter a letter to fill in the blanks to complete the word.  If you enter the correct letter, the letter will be revealed.  If incorrect letter is entered, then a slice of a watermelon will be removed.  Try to save the watermelon by guesting the correct letters to reveal the secret percussion instrument word.  You will get 4 attements to guest the correct word before the watermelon is completely sliced up and game over.   

# 3 Core features (must-haves) vs stretch goals (nice to have):
Core features: Words must be masked and patially revealed to the user.  Game must be looped back to the begining until the counter of incorrect guesses reaches 4 attempts.  If user guesses correct letters then the secret percussion word will be revealed.  If user guest all correct letters then they win, saving the watermelon!  
Nice to have (optional): hints, scorebord, optional difficulty levels.

# 4 Basic flow diagram:
The basic flow will be:  
a. Secret percussion word will be masked with only partially the word revealed
b. User will guess and enter a letter, if correct word is guessed then the letter will be revealed in the scret word and the game will loop back to the beginning.  
c. If the user enters the incorrect letter then the incorrect counter will save the number of attempts and letters and loop back to the beginning. 
d. If the user enters all the correct letters before 4 incorrect attempts then the watermelon is saved and the user wins!
e. If the user enters 4 incorrect letters then the watermelon will be sliced and the watermelon will not be saved and the user loses.  
f.  Secret percussion word will be masked

# 5 Data design:
Data design will be:
The secret words will be stored a list.  Words will be masked with only few letter revealed. If letters are guessed correctly then letters will be revealed.  If letters are guessed incorrectly then a slice of the watermelon will be removed.  If 4 attempts are guessed incorrectly then the water melon will be completely sliced off and the game will end.

# 6 Module/function responsibilities:
Module and function responsiblilities will be 
a. Create a scret word list of different percussion instruments
b. Loop and reveal letters if correct letters are guessed
c. Loop and save incorrect letters if guessed incorrectly
d. If 4 are guessed incorrectly then game is over
e. If 3 or less incorrectly letters are guessed then loops back to the beginning
f. 




Hello and welcome to our guest a secret percussion word save the watermelon game!  Here you will get to select a secret percussion word and try and guest the correct letter and save the waterdmelon.





