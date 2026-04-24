from abc import ABC, abstractmethod
import random
from simulation.grid import Grid


class BaseAgent(ABC):
    def __init__(self, grid: Grid):
        self._grid = grid
        self._x = grid.start.x()
        self._y = grid.start.y()
        self._steps = 0
    
    @property
    def get_x(self):
        return self._x
    
    @property
    def get_y(self):
        return self._y
    
    @property
    def get_steps(self):
        return self._steps
    
    def has_reached_goal(self):
        return self._grid.get_cell(self._x, self._y).is_goal()\
    
    @abstractmethod
    def move(self):
        pass

    def _get_valid_neighbours(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        neighbours = []
        for dx, dy in directions:
            nx, ny = self._x + dx, self._y + dy
            if self._grid.is_valid_move(nx, ny):
                neighbours.append((nx, ny))
        return neighbours
    
class RandomAgent(BaseAgent):
    def move(self):
        neighbours = self._get_valid_neighbours()
        if neighbours:
            self._x, self._y = random.choice(neighbours)
            self._steps += 1
         
class GreedyAgent(BaseAgent):
    def move(self):
        neighbours = self._get_valid_neighbours()
        if neighbours:
            goal_x = self._grid.goal.x()
            goal_y = self._grid.goal.y()
            self._x, self._y = min(
                neighbours,
                key=lambda pos: abs(pos[0] - goal_x) + abs(pos[1] - goal_y)
            )
            self._steps += 1
        