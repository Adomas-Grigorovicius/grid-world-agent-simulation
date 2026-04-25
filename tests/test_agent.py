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

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.grid = Grid("data/world.csv")
        self.random_agent = RandomAgent(self.grid)
        self.greedy_agent = GreedyAgent(self.grid)

    def test_agent_starts_at_start(self):
        self.assertEqual(self.random_agent.x, self.grid.start.x)
        self.assertEqual(self.random_agent.y, self.grid.start.y)

    def test_agent_initial_steps(self):
        self.assertEqual(self.random_agent.steps, 0)

    def test_agent_moves(self):
        self.random_agent.move()
        self.assertEqual(self.random_agent.steps, 1)

    def test_agent_has_not_reached_goal_at_start(self):
        self.assertFalse(self.random_agent.has_reached_goal())

    def test_greedy_agent_moves(self):
        self.greedy_agent.move()
        self.assertEqual(self.greedy_agent.steps, 1)

    def test_greedy_reaches_goal(self):
        for _ in range(100):
            if self.greedy_agent.has_reached_goal():
                break
            self.greedy_agent.move()
        self.assertTrue(self.greedy_agent.has_reached_goal())
