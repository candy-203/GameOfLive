import copy
import random
import sys

from .graphics import Squares


class GameOfLive:

    def __init__(self, width: int, height: int, cell_size: int, color_dict: dict):
        self.HEIGHT: int = height
        self.WIDTH: int = width
        self.UI = Squares(self.WIDTH, self.HEIGHT, cell_size, color_dict)

        self._old_square_dict = {(i, k): 0 for i in range(self.WIDTH) for k in
                                 range(self.HEIGHT)}
        self._new_square_dict = copy.copy(self._old_square_dict)
        self.COLOR_DICT = color_dict

        self.config()

    def config(self):
        for i in range(self.WIDTH):
            for k in range(self.HEIGHT):
                if random.random() < 0.2:
                    self.set_cell_number(i, k, 1)
        self.update()

    def run(self):
        while True:
            self.frame()

    def frame(self):
        for i in range(self.WIDTH):
            for k in range(self.HEIGHT):
                center = self.get_cell_number(i, k)
                neighbors = self.get_neighbors_numbers(i, k)

                if neighbors.count(1) == 3 and center == 0:
                    self.set_cell_number(i, k, 1)
                elif neighbors.count(1) < 2 and center == 1:
                    self.set_cell_number(i, k, 0)
                elif neighbors.count(1) > 3 and center == 1:
                    self.set_cell_number(i, k, 0)
        self.UI.draw(self._new_square_dict)
        self._old_square_dict = copy.copy(self._new_square_dict)

    def get_neighbors_numbers(self, x_coord: int, y_coord: int) -> list:
        self.proof_coords(x_coord, y_coord)
        result = []

        for i in range(x_coord - 1, x_coord + 2):
            for k in range(y_coord - 1, y_coord + 2):
                is_center = i == x_coord and k == y_coord
                if (not is_center) and self.proof_coords_bool(i, k):
                    num = self.get_cell_number(i, k)
                    result.append(num)
        return result

    def get_cell_number(self, x_coord: int, y_coord: int) -> int:
        self.proof_coords(x_coord, y_coord)
        return self._old_square_dict[(x_coord, y_coord)]

    def set_cell_number(self, x_coord, y_coord, number: int):
        self.proof_coords(x_coord, y_coord)
        self.proof_number(number)
        self._new_square_dict[(x_coord, y_coord)] = number

    def proof_coords(self, x_coord: int, y_coord: int):
        if not self.proof_coords_bool(x_coord, y_coord):
            raise ValueError("Wrong coordinates!!!")

    def proof_coords_bool(self, x_coord: int, y_coord: int) -> bool:
        if x_coord < 0 or y_coord < 0:
            return False
        if x_coord >= self.WIDTH or y_coord >= self.HEIGHT:
            return False
        return True

    def proof_number(self, number: int):
        if number not in self.COLOR_DICT.keys():
            raise ValueError("Wrong Number!!!")

    def update(self):
        self.UI.update()

    def loop(self):
        self.UI.loop()


args = sys.argv

if not (3 <= len(args) <= 4):
    print("Usage: python3 -m GameOfLife height width")
    sys.exit(1)

size = 10

try:
    height = int(args[1])
    width = int(args[2])
    if len(args) == 4:
        size = int(args[3])
except ValueError:
    print("Usage: python3 -m GameOfLife height width (size)")
    sys.exit(1)

obj = GameOfLive(height, width, size, {1: "green", 0: "white"})
obj.run()
