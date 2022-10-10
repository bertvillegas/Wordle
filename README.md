# Wordle
Project that solves the algorithm for Wordle

In the game of Wordle, you try to guess a secret word. Every time you guess a word, you receive a response consisting of green, yellow, and black tiles.

The rules are as follows:

A green tile at position i indicates that the letter at position i in the guess word is also in the secret word at that position
A yellow tile at position i indicates that the letter at position i in the guess word is in the secret word, but at a different position
A black tile at position i indiciates that the letter at position i in the guess word is not in the secret word at all.
alt text

# Handling duplicate letters
If the guess includes multiple copies of the same letter, when determining what color tile to return for each letter:

Green tiles always take precedence over anything else (handle these first!). If a letter is the correct letter in the correct location, return a green tile in that position no matter what.
If there are G copies of a particular letter in the guess word, but the secret word has S copies of that letter where S < G, then the answer should contain no more than S yellow or green tiles at positions where the guess word has a copy of that letter.
For a given letter, after the green tiles have been dealt with, work left to right to determine which tiles to make yellow until you've used up S tiles. The remaining tiles containing that letter should be black.


# Function specs
Write a function called wordle that takes a string guess and a string secret_word and returns the response as a string of G for green, Y for yellow, B for black.

# Assumptions
The input words are the same length
The input words are in all uppercase
The input words contain only letters (no numbers, symbols, etc)
The input words will not be empty strings

