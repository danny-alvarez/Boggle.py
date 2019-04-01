Skip to content
Search…
All gists
Back to GitHub
New gist

@cdent cdent/boggle.py
Created 9 years ago • 
0
0
 Code  Revisions 2
 
<script src="https://gist.github.com/cdent/268079.js"></script>
  
 boggle.py
from random import random
from math import sqrt

import sys

WORDS = 'web2'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

INDEX = {}
FOUND = []

def make_index():
    """Read in the words from the word list creating a really
    fat and wasteful dict that enables lookups. If the words 'cat'
    and 'cater' are in the list, you'll get this in the dictionary:
       { 'c': ['cat','cater'],
         'ca': ['cat','cater'],
         'cat': ['cat','cater'],
         'cate': ['cater'],
         'cater': ['cater'],
       }
    
    This makes for some nice brute force.
    Words in the list which are too short, proper names, contractions
    are trimmed out.
    """
    words = open(WORDS).readlines()
    for word in words:
        if word.istitle():
            continue
        if "'" in word:
            continue
        word = word.lower().rstrip()
        if not word.isalpha():
            continue
        if len(word) < 3:
            continue
        if len(word) > 16:
            continue
        for index, letter in enumerate(word):
            try:
                INDEX[word[:index+1]].append(word)
            except KeyError:
                INDEX[word[:index+1]]= [word]

def test_board():
    """Make a test board which has a few obvious words."""
    return [
            'C', 'A', 'T', 'X',
            'A', 'N', 'T', 'X',
            'T', 'R', 'E', 'E',
            'E', 'B', 'X', 'Y',
            ]


def start_hunt(board):
    """Start traversing the board, hunting for words."""
    for index in range(len(board)):
        current_word = [index]
        hunt(board, current_word)


def hunt(board, current_word):
    """Traverse nearest neighbors to see if we have found a word
    or a valid word prefix. current_word is the list of board indexes
    active right now."""
    neighbor_indexes = neighbors(board, current_word[-1], current_word)
    for candidate in neighbor_indexes:
        current_word.append(candidate)
        if is_word(board, current_word):
            word = print_word(board, current_word)
            if not word in FOUND:
                FOUND.append(word)
        if starts_word(board, current_word):
            hunt(board, current_word)
        current_word.pop()


def print_word(board, current_word):
    """Turn a current_word list of board indexes into a string of letters."""
    return (''.join(board[index] for index in current_word)).lower()


def is_word(board, current_word):
    """See if the current_word is in the word INDEX."""
    word = print_word(board, current_word)
    return len(word) > 2 and word in INDEX and word in INDEX[word]


def starts_word(board, current_word):
    """See if the current_word is a prefix in the word INDEX."""
    word = print_word(board, current_word)
    return word in INDEX


def neighbors(board, index, mask=None):
    """Find the valid neighbor letters from the current index on
    the board. The mask is a list of indexed letters already used
    in the current hunt."""
    if mask == None:
        mask = []

    indexes = []

    length = len(board)
    square = int(sqrt(length))
    NEIGHBORS = [1, square+1, square, square-1, -1, -(square+1), -square, -(square-1)]

    for neighbor in NEIGHBORS:
        # There's probably some math for this but this is clear to me
        # weak head.
        if index % square == 0 and neighbor in [-(square+1), -1, square-1]:
            continue
        if (index + 1) % square == 0 and neighbor in [-(square-1), 1, square+1]:
            continue

        local_index = index + neighbor
        if local_index in mask:
            continue
        if local_index < 0:
            continue
        if local_index > length - 1:
            continue
        indexes.append(local_index)

    return indexes


def print_board(board):
    """Display the current board."""
    square = sqrt(len(board))
    for index, value in enumerate(board):
        print value,
        if (index + 1) % square:
            print ' ',
        else:
            print


def make_board():
    """Make a random board. Note this does not map to real boggle dice."""
    return [random_letter() for x in range(16)]

def random_letter():
    return LETTERS[int(random() * len(LETTERS))]

def run(args):
    """Do a sample run. If a string of letters is provided as the first
    argument it will be used to build a board. The string must be 16, 25, 36, etc
    characters long. If not string is a provided a test_board is used."""
    make_index()
    searching = True
    global FOUND
    while searching:
        try:
            board = list(args[1])
            searching = False
        except IndexError:
            board = test_board()
            # make_board for a random board
            #board = make_board()
        print_board(board)
        start_hunt(board)
        if len(FOUND) > 10:
            searching = False
        else:
            FOUND = []
    print len(FOUND)
    FOUND = reversed(sorted(FOUND, key=len))
    print list(FOUND)




   
 
 

