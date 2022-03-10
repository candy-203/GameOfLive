import tkinter


class Squares:

    def __init__(self, width: int, height: int, cell_size: int, color_dict: dict):
        self.HEIGHT = height
        self.WIDTH = width
        self.CELL_SIZE = cell_size
        self.STD_COLOR = "white"
        self.COLOR_DICT = color_dict

        self.__cell_dict = {}  # (x,y) -> id

        self.__tk = tkinter.Tk()

        self.__canvas = tkinter.Canvas(self.__tk, height=self.HEIGHT * cell_size, width=self.WIDTH * cell_size)
        self.__canvas.pack()

        self.__config_canvas()

    def __config_canvas(self):
        for i in range(self.WIDTH):
            for k in range(self.HEIGHT):
                square_id = self.__canvas.create_rectangle(i * self.CELL_SIZE, k * self.CELL_SIZE,
                                                           (i + 1) * self.CELL_SIZE,
                                                           (k + 1) * self.CELL_SIZE, fill=self.STD_COLOR)
                self.__cell_dict[(i, k)] = square_id

    def draw(self, square_dict):
        for square in square_dict:
            self.set_color_square(square[0], square[1], self.COLOR_DICT[square_dict[square]])
        self.update()

    def set_color_square(self, x_coord: int, y_coord: int, color: str):
        self.proof_coords(x_coord, y_coord)
        self.__canvas.itemconfig(self.__cell_dict[(x_coord, y_coord)], fill=color)

    def update(self):
        self.__tk.update()

    def loop(self):
        self.__tk.mainloop()

    def proof_coords(self, x_coord: int, y_coord: int):
        if x_coord < 0 or y_coord < 0:
            raise ValueError("Wrong Coordinates!!!")
        if x_coord >= self.WIDTH or y_coord >= self.HEIGHT:
            raise ValueError("Wrong Coordinates!!!")
