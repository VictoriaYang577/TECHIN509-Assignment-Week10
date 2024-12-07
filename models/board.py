class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        for row in self.grid:  # go through everything 
            print("|".join(row))  # use | 
            print("-" * 5)  # print under each line 

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """

    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)

if __name__ == "__main__":
    board = Board()

    # Testsss
    board.grid = [["X", "O", "X"], [" ", "X", "O"], ["O", " ", "X"]]
    
    # use draw_board method print grid
    board.draw_board() 
