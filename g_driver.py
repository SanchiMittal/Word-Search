import game_func as gf
import sys

def inst():
    print("\nHow to play:")
    print("Find English words hidden in the grid of letters."
          "\nThe words should start and end either from left to right or "
          "\nfrom top to bottom."
          "\nDiagonal words are not valid."
          "\nType a found word and press enter to play your turn and score!")
    
def rules():
    print("\nScoring Rules:"
          "\nWord length:"
          "\n  < 3: 0 points"
          "\n  3-6: 1 point per character for all characters in word"
          "\n  7-9: 2 points per character for all characters in word"
          "\n  10+: 3 points per character for all characters in word")    

def choice(c):

    try:
        k = int(c)
    except ValueError:
        print("Choice not available.")
        
    else:
        if(int(k)==1):
            inst()
        elif(int(k)==2):
            rules()
        elif(int(k)==3):
            print("\nWhile playing:")
            print("\nEnter 0 to stop the game and return to menu.")
            print("\nEnter 5 to get solutions and quit.")
            print("\nLoading game...")
            players = get_players_list()
            play_game(players, board, words)
            print_score(players)
            input("Press any key to exit.")
            sys.exit("Goodbye!")

        elif(int(k)==4):
            a = input("Are you sure you want to quit? Y/N?")
            if a.upper() == 'Y':
                sys.exit("Goodbye!")
            else:
                response()
        else:
            print("Choice not available.")
            
    response()
    
        

def response():
    print("\n1. How to play"
          "\n2. Rules"
          "\n3. Play"
          "\n4. Quit")
    c = input("\nEnter your choice: ")
    choice(c)


def answers():
    print("Solutions:\n")
    print(words)
    
def print_board(board):
    """ 
    Display the contents of board.
    """

    for row_idx in range(len(board)):
        print(gf.make_str_from_row(board, row_idx))


def get_players_list():
    """
    Prompt the player(s) to enter their names and return a list of player info
    as a two-item list with name and score, respectively.
    """

    players = []
    player = input('Enter player 1 name: ')
    while player.strip() or not players:
        player = player.strip()

        if player in players:
            print("A player by that name is already playing.")

        if player:
            players.append([player, 0])

        if players:
            print('Leave a blank player name to begin playing.')
        player = input('Enter player {num} name: '.format(num=len(players) + 1))

    return players


def play_game(players, board, words):
    """ 
    Play the game with players, board and words.
    """
    num_remaining = gf.num_words_on_board(board, words) - len(found_words)
    player_num = 0
    while num_remaining > 0:
        print_headers(players, board, found_words, num_remaining)

        guess = input("[{player}] Enter a word (or blank to pass): ".format(
            player=players[player_num % len(players)][0]))

        if(guess == '0'):
            response()
        if(guess == '5'):
            answers()
            input("Press any key to exit.")
            sys.exit("Goodbye!")
                
        guess = guess.strip().upper()
        if gf.is_valid_word(words, guess) and gf.board_contains_word(board, guess) and \
            not guess in found_words:
            gf.update_score(players[player_num % len(players)], guess)
            found_words.append(guess)

        num_remaining = gf.num_words_on_board(board, words) - len(found_words)
        player_num += 1

    answers()
    print("Game over!\n")


def print_headers(players, board, found_words, num_remaining):
    """ 
    Play the score, board, and some other details.
    """

    print_score(players)
    print_board(board)
    print('\nWords remaining: {num} words left.'.format(num=num_remaining))
    print('Words found: ' + (' '.join(found_words) or 'No words found, yet.'))


def print_score(players):
    """ 
    Print the scores for each of the players.
    """
    for name, score in players:
        print('\t' + name + '  ' + str(score).rjust(3) )
    print("\n")


# Load the words list.
words_file = open(gf.words(), 'r')
words = gf.read_words(words_file)
words_file.close()

# Load the board.
board_file = open(gf.board(), 'r')
board = gf.read_board(board_file)
board_file.close()

print("Welcome to the game of Word Search!")

found_words = []

response()

found_words = []

