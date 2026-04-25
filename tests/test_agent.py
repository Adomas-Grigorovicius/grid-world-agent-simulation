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