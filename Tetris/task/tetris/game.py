class Shape:
    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name
        self.current_coordinates = coordinates[0]
        self.rotated = 0
        self.floor = False

    def rotateCurrentCoordinates(self):
        self.rotated += 1
        self.current_coordinates = self.coordinates[self.rotated % len(self.coordinates)]


class TetrisGame:
    def __init__(self):
        self.board = None
        self.M = 0
        self.N = 0
        self.O = [[4, 14, 15, 5]]
        self.I = [[4, 14, 24, 34], [3, 4, 5, 6]]
        self.S = [[5, 4, 14, 13], [4, 14, 15, 25]]
        self.Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
        self.L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
        self.J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
        self.T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
        self.choices = "I, S, Z, L, J, O, T".split(", ")
        self.pieces = [self.I, self.S, self.Z, self.L, self.J, self.O, self.T]

    def populate_board(self):
        board_size = input().split(" ")
        print()
        self.M = int(board_size[0])
        self.N = int(board_size[1])
        formatted = " -"

        self.board = "-" + formatted * (self.M * self.N)
        self.board = self.board.split(" ")

    def print_board(self, board_copy):
        for i in range(0, (self.M * self.N), self.M):
            print(" ".join(board_copy[i:i + self.M]))

    # in the next phase, when things land then the proper self.board will be updated
    # for left, check the modulo value is >0
    # for right check the modulo value is <M
    # for rotate, check that every rotated value is within bounds

    # for floor, if any of the coordinates = N

    def update_current_coordinates(self, shape, value):
        temp_coordinates = []
        for coordinate in shape.current_coordinates:
            if value == -1:
                if (coordinate + value) % self.N == self.N - 1:
                    if coordinate + value >= self.M * self.N:
                        shape.floor = True
                    return
            elif value == 1:
                if (coordinate) % self.N+1 == self.N:
                    if coordinate + value >= self.M * self.N:
                        shape.floor = True
                    return

            if coordinate + value >= self.M * (self.N-1):
                shape.floor = True
            coordinate += value
            temp_coordinates.append(coordinate)
        shape.current_coordinates = temp_coordinates

    def update_all_coordinates(self, shape, value):
        temp_coordinates = []

        if shape.floor is False:
            for i in range(len(shape.coordinates)):
                temp_coordinates.append([])
                for coordinate in shape.coordinates[i]:
                    temp_coordinates[i].append((coordinate + value))
            shape.coordinates = temp_coordinates

    def shift_shape(self, shape, direction):
        if direction == "down" and shape.floor is False:
            self.update_current_coordinates(shape, self.M)
            self.update_all_coordinates(shape, self.M)


        elif direction == "right" and shape.floor is False:
            self.update_current_coordinates(shape, 1)
            self.update_all_coordinates(shape, 1)


        elif direction == "left" and shape.floor is False:
            self.update_current_coordinates(shape, -1)
            self.update_all_coordinates(shape, -1)

    def rotate_shape(self, shape):
        shape.rotateCurrentCoordinates()

    def map_coordinates_board(self, value):
        board_copy = self.board.copy()
        for coordinate in value:
            board_copy[coordinate] = "0"

        return board_copy

    def get_input(self):
        user_input = input()
        self.populate_board()
        self.print_board(self.board)
        print()

        if user_input in self.choices:
            piece = self.pieces[self.choices.index(user_input)]
            shape = Shape(piece, user_input)
            self.print_board(self.map_coordinates_board(shape.current_coordinates))

        movement = input()

        while movement != "exit":
            if shape.floor == True:
                pass
            else:
                if movement == "rotate":
                    self.rotate_shape(shape)
                    self.shift_shape(shape, "down")
                elif movement == "left":
                    self.shift_shape(shape, "left")
                    self.shift_shape(shape, "down")
                elif movement == "right":
                    self.shift_shape(shape, "right")
                    self.shift_shape(shape, "down")
                elif movement == "down":
                    self.shift_shape(shape, "down")
                else:
                    print("Unrecognised")

            print()
            self.print_board(self.map_coordinates_board(shape.current_coordinates))
            movement = input()

    def main(self):
        self.get_input()


tetris_game = TetrisGame()
tetris_game.main()
