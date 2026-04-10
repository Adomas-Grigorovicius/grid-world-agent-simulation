class Cell:
    VALID_TYPES = ("E","W","G","S")

    def __init__(self, x: int, y: int, cell_type: str):
        self.__x = x
        self.__y = y
        self.__cell_type = cell_type 
    
    @property
    def get_x(self):
        return self.__x
    
    @property
    def get_y(self):
        return self.__y
    
    @property
    def get_type(self):
        return self.__cell_type
    
    @cell_type.setter
    def set_type(self, cell_type):
        if cell_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid cell type: {cell_type}")
        self.__cell_type = cell_type
    
    @cell_type.setter
    def is_walkable(self: bool):
        return self.__cell_type != "W"
    
    @cell_type.setter
    def is_goal(self: bool):
        return self.__cell_type == "G"
    
    @cell_type.setter
    def __repr__(self: str):
        return f"Cell({self.__x}, {self.__y}, '{self.__cell_type}')"
        

