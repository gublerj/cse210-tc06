import random

class Board:
    """
    A designated playing surface. The responsibility of Board is to create a board, check the guessed number
    and check for a winner.
    
    Stereotype: 
        Information Holder

    Attributes:
        board (list): The number of digits.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self.board = []
        self._checked_guess = ['*','*','*','*']
        self._checked_guess1 = []
        self._checked_guess2 = []
        self.player = []
        self.count = 0
        self.guess = ['-','-','-','-']
        self.guess1 = ['-','-','-','-']


    
    def create_board(self, playerName):
        """
        Creates the board
        """
        self.player.append(playerName)
        self.board = []
        for x in range(4):
            if x == 0:
                n = random.randint(1,9)
            else:
                n = random.randint(0,9)
            self.board.append(n)
        return self.board

    def check_guess(self, board, guess):
        
        for x in range(4):
            if board[x] == guess[x]:
                self._checked_guess[x] = 'o'
            elif: 
                for y in range(4):
                    if guess[y] == board[x]:
                        self._checked_guess[x] = 'x'
            else:
                self._checked_guess[x] = '*'
        if self.count % 2 == 0:
            self.guess = guess
            self._checked_guess1 = self._checked_guess
        else:
            self.guess1 = guess
            self._checked_guess2 = self._checked_guess
        self.count = self.count + 1


    def to_string(self):
        """
        prepares everything to be printed
        takes _checked_guess and guess. Returns a string to be printed.
        """
        text =  "\n--------------------\n"
        for x in range(2):
            test += (f"Player {playerName[x]}: ")
            for y in range(4)
                text += (f"{self.guess[y]}")
            for z in range(4):
                text += (f"{self._checked_guess[z]}")
            text += "\n"
        text += "\n--------------------"

    def did_win(self):
        """
        checks to see if any player won
        """
        for x in range(4)
        if guess[x] == board[x]:
            return True
        else:
            return False
    





