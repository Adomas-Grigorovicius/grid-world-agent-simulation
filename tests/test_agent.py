import unittest
from simulation.grid import Grid
from simulation.agent import RandomAgent, GreedyAgent
from simulation.file_manager import FileManager


class TestCell(unittest.TestCase):

    def setUp(self):
        self.grid = Grid("data/world.csv")

    def test_cell_type(self):
        cell = self.grid.get_cell(0, 0)
        self.assertEqual(cell.cell_type, "S")

    def test_cell_is_walkable(self):
        cell = self.grid.get_cell(1, 0)
        self.assertTrue(cell.is_walkable())

    def test_wall_is_not_walkable(self):
        cell = self.grid.get_cell(3, 0)
        self.assertFalse(cell.is_walkable())

    def test_cell_is_goal(self):
        cell = self.grid.get_cell(4, 4)
        self.assertTrue(cell.is_goal())

    def test_invalid_cell_type(self):
        cell = self.grid.get_cell(0, 0)
        with self.assertRaises(ValueError):
            cell.cell_type = "X"

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid("data/world.csv")

    def test_grid_loads_start(self):
        self.assertIsNotNone(self.grid.start)
        self.assertEqual(self.grid.start.cell_type, "S")

    def test_grid_loads_goal(self):
        self.assertIsNotNone(self.grid.goal)
        self.assertEqual(self.grid.goal.cell_type, "G")

    def test_grid_dimensions(self):
        self.assertEqual(self.grid.rows, 5)
        self.assertEqual(self.grid.cols, 5)

    def test_valid_move(self):
        self.assertTrue(self.grid.is_valid_move(1, 0))

    def test_invalid_move_wall(self):
        self.assertFalse(self.grid.is_valid_move(3, 0))

    def test_invalid_move_out_of_bounds(self):
        self.assertFalse(self.grid.is_valid_move(-1, 0))
        self.assertFalse(self.grid.is_valid_move(0, -1))
        self.assertFalse(self.grid.is_valid_move(10, 0))