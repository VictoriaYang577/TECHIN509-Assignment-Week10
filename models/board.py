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
        # Check rows for winner
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns for winner
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " ":
                return self.grid[0][col]

        # Check diagonals for winner
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]

        # No winner
        return ""

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

if __name__ == "__main__":
    board = Board()

    # 测试1
    board.grid = [["X", "X", "X"], ["O", " ", "O"], [" ", " ", " "]]
    print("Winner:", board.check_winner())  # 输出: Winner: X

    # 测试2
    board.grid = [["X", "O", " "], ["X", "O", " "], [" ", "O", " "]]
    print("Winner:", board.check_winner())  # 输出: Winner: O

    # 测试3
    board.grid = [["X", "O", "O"], [" ", "X", " "], ["O", " ", "X"]]
    print("Winner:", board.check_winner())  # 输出: Winner: X

    # 测试4
    board.grid = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "O"]]
    print("Winner:", board.check_winner())  # 输出: Winner: 
