"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""

import random

def is_valid_word(wordlist, word):
    #Return True if and only if word is an element of wordlist.
                  
    return(word in wordlist)

def make_str_from_row(board, row_index):

    #Return the characters from the row of the board
    #with index row_index as a single string.
                  
    w = ''
    for c in board[row_index]:
        w = w + c
    return w


def make_str_from_column(board, column_index):

    #Return the characters from the column of the board
    #with index column_index as a single string

    w=''
    for s in board:
        w = w +s[column_index]
    return w

def board_contains_word_in_row(board, word):
    """
    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.
    """

    
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """
    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.
    """
    for i in range(len(board[0])):
        if word in make_str_from_column(board, i):
            return True

    return False

    
def board_contains_word(board, word):
    """
    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.
    """

    if(board_contains_word_in_row(board, word)):
        return True
    elif(board_contains_word_in_column(board, word)):
        return True
    else:
        return False

def word_score(word):
    """
    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    """

    if(len(word) < 3):
        return 0
    elif(len(word)>=3 and len(word)<7):
        return len(word)
    elif(len(word)>=7 and len(word)<10):
        return(2*len(word))
    elif(len(word)>=10):
        return(3*len(word))

    else:
        return 0
        
def update_score(player_info, word):
    """
    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.
    """

    player_info[1] = player_info[1] + word_score(word)
    

def num_words_on_board(board, words):
    """
    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    c = 0
    for w in words:
        if(board_contains_word(board, w)):
           c= c+1

    return c

def read_words(words_file):
    """
    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    
    l = []

    for line in words_file:
        l.append(line.rstrip())

    return l

def read_board(board_file):
    """ 
    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    
    list1 = []
    
    for line in board_file:
        list2 = []
        for c in line.rstrip():
            list2.append(c)
        list1.append(list2)

    return list1
    
def board():
    return blist[x]

def words():
    return wlist[x]
    
blist = ["b1.txt", "b2.txt", "b3.txt"]
wlist = ["w1.txt", "w2.txt", "w3.txt"]
x = random.randint(0, len(blist)-1)
