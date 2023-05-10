class TetrisGame:
    def __init__(self):
        self.board = ["-", "-", "-", "-"] * 4
        self.O = [[5, 6, 9, 10]]
        self.I = [[1, 5, 9, 13], [4, 5, 6, 7]]
        self.S = [[6, 5, 9, 8], [5, 9, 10, 14]]
        self.Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
        self.L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
        self.J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
        self.T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
        self.choices = "I, S, Z, L, J, O, T".split(", ")
        self.pieces = [self.I, self.S, self.Z, self.L, self.J, self.O, self.T]

    def print_board(self, board_copy):
        index1 = 0
        index2 = 4

        for i in range(0, 4):
            board_row = (board_copy[index1:index2])
            print(" ".join(board_row))
            index1 += 4
            index2 += 4

    def populate_board(self, value):
        board_copy = self.board.copy()
        for coordinate in value:
            board_copy[coordinate] = "0"

        return board_copy

    def print_all_positions(self, value):
        for i in range(5):
            self.print_board(self.populate_board(value[i % len(value)]))
            print()

    def get_input(self):
        user_input = input()
        self.print_board(self.board)
        print()

        if user_input.upper() in self.choices:
            self.print_all_positions(self.pieces[self.choices.index(user_input)])

    def main(self):
        self.get_input()



tetris_game = TetrisGame()
tetris_game.main()
