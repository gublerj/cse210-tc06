from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """
        Imports classes
        Controls flow of the game
    """
    def __init__(self):
        self._board = Board()
        self._console = Console()
        self._move = Move()
        self._player = Player()
        self._roster = Roster()

    def start_game(self):
        """
            Starts the game
        """

        _prepare_game()

        while self._keep_playing() == True:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _prepare_game(self):
        """
            Sets up the game and gets number of players
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

        p1_board = self._board.create_board()
        p2_board = self._board.create_board()

    def _get_inputs(self):
        """
            Gets input from the player(s)
        """
        # Create and display the board
        # board = self._board.to_string()
        # self._console.write(board)

        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn: ")
        guess = _console.read_number("What is your guess? ")
        move = Move(guess)
        player.set_move(move)


    def _do_outputs(self):
        """
            Outputs information to the console
        """


    def _do_updates():
        """
            Updates the user's guess and which numbers are correct
        """
        player = self._roster.next_player()
        move = player.get_move()
        # Not sure about this one.
        # self._board.apply()

    def keep_playing():
        """
            Determines whether the game has ended or not
        """
        player = self._roster.get_current()
