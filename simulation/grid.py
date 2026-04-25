import csv
from simulation.cell import Cell

class Grid:

    def __init__(self, filepath):
        self.__filepath = filepath 
        self.__grid = []
        self.__goal = None
        self.__start = None 
        self.__rows = 0
        self.__cols = 0
        self.__load(filepath)

    def __load(self, filepath):
        with open(filepath, newline="") as f:
            reader = csv.reader(f)
            for y, row in enumerate(reader):
                grid_row = []
                for x, cell_type in enumerate(row):
                    cell = Cell(x, y, cell_type.strip())
                    grid_row.append(cell)
                    if cell.cell_type == "S":
                        self.__start = cell
                    elif cell.cell_type == "G":
                        self.__goal = cell
                self.__grid.append(grid_row)
            self.__rows = len(self.__grid)
            self.__cols = len(self.__grid[0]) if self.__grid else 0
    
    def get_cell(self, x, y):
        return self.__grid[y][x]
    
    @property
    def start(self):
        return self.__start

    @property
    def goal(self):
        return self.__goal

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols
    
    def is_valid_move(self, x, y):
        if 0 <= x < self.__cols and 0 <= y < self.__rows:
            return self.__grid[y][x].is_walkable()
        return False
    
    def display(self, agent_x: int = None, agent_y: int = None):
        for y in range(self.__rows):
            row_str = ""
            for x in range(self.__cols):
                if agent_x == x and agent_y == y:
                    row_str += "A "
                else:
                    row_str += self.__grid[y][x].cell_type + " "
            print(row_str)
        print()


    