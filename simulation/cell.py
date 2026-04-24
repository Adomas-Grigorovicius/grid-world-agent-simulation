class Cell:
    VALID_TYPES = ("E","W","G","S")

    def __init__(self, x, y, cell_type):
        self.__x = x
        self.__y = y
        self.__cell_type = cell_type 

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def cell_type(self):
        return self.__cell_type
    
    @cell_type.setter
    def cell_type(self, value):
        if value not in self.VALID_TYPES:
            raise ValueError(f"Invalid cell type: {value}")
        self.__cell_type = value
    
    def is_walkable(self: bool):
        return self.__cell_type != "W"
    
    def is_goal(self: bool):
        return self.__cell_type == "G"
    
    def __repr__(self: str):
        return f"Cell({self.__x}, {self.__y}, '{self.__cell_type}')"
        

