# Grid World Agent Simulation

## 1. Introduction

### What is this application?

This application is a Grid World Agent Simulation built using Python.
The program simulates one or more agents navigating through a 2D grid world
loaded from a CSV file. The grid consists of different cell types: empty cells,
walls, a start position, and a goal position.

Two types of agents are implemented: a Random Agent, which moves to a random
valid neighbouring cell each step, and a Greedy Agent, which always moves
toward the cell closest to the goal. The simulation runs until the agent
successfully reaches the goal cell.

The project demonstrates core Object-Oriented Programming principles including
encapsulation, abstraction, inheritance, and polymorphism, as well as the
Factory design pattern and composition between the Grid and Cell classes.

### How to run the program?

Make sure you have Python installed (version 3.8 or higher). To check, run:

```bash
python --version
```

Clone the repository from GitHub:

```bash
git clone https://github.com/Adomas-Grigorovicius/grid-world-agent-simulation
```

Navigate into the project folder:

```bash
cd grid-world-agent-simulation
```

Run the program from the root of the project:

```bash
python main.py
```

Make sure you always run `main.py` from the root folder, not from inside
any of the subfolders, otherwise the imports will not work correctly.

---

### How to use the program?

When the program starts, you will see the following menu:

=== Grid World Agent Simulation ===
Select agent type:
1. Random Agent
2. Greedy Agent

Enter 1 or 2:

Enter `1` to run the **Random Agent**, which moves to a random valid
neighbouring cell each step, or `2` to run the **Greedy Agent**, which
always moves toward the cell closest to the goal.

The grid will be printed to the console at each step of the simulation,
showing the current state of the world:

- `S` — Start position
- `G` — Goal position
- `W` — Wall (not walkable)
- `E` — Empty cell (walkable)
- `A` — Current agent position

The simulation ends automatically when the agent reaches the goal. The
number of steps taken is displayed and the result is saved to
`data/results.csv`. All previous results are then printed to the console.

---

## 2. Body / Analysis

### 4 OOP Pillars

#### Encapsulation

Encapsulation is the principle of hiding an object's internal data and only
exposing it through controlled methods (getters and setters). This prevents
outside code from directly modifying an object's state in unexpected ways.

In this project, the Cell class demonstrates Strict Encapsulation by using double underscores (__) to make attributes private. This triggers Python’s name mangling, making the attributes inaccessible from outside the class:

```python
def __init__(self, x: int, y: int, cell_type: str):
    self.__x = x
    self.__y = y
    self.__cell_type = cell_type
```
I implemented Pythonic Getters and Setters using the @property decorator. This allows the attributes to be accessed like variables while maintaining control over how they are handled. For example, the cell_type setter includes validation logic to ensure the grid only contains valid cell characters:

```python
@property
    def cell_type(self):
        return self.__cell_type
    
    @cell_type.setter
    def cell_type(self, cell_type):
        if cell_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid cell type: {cell_type}")
        self.__cell_type = cell_type
```

#### Abstraction

Abstraction means hiding complex implementation details and only exposing
what is necessary for the outside world to interact with. It allows you to
define a common interface without specifying exactly how it works internally.

In this project, abstraction is implemented through the `BaseAgent` abstract
class. It inherits from Python's built-in `ABC` (Abstract Base Class) and
defines what every agent must be able to do, without specifying how:

```python
from abc import ABC, abstractmethod
class BaseAgent(ABC):

    @abstractmethod
    def move(self):
        pass
```
The `@abstractmethod` decorator on `move()` enforces that any class
inheriting from `BaseAgent` must implement its own version of `move()`.
If a subclass forgets to do this, Python will immediately throw an error
when trying to create an instance of it.

#### Inheritance

Inheritance allows a class to reuse attributes and methods from a parent
class. Both `RandomAgent` and `GreedyAgent` inherit from `BaseAgent`,
meaning they automatically get attributes like `_x`, `_y`, `_steps` and
methods like `has_reached_goal()` and `_get_valid_neighbours()` without
rewriting them:

```python
class RandomAgent(BaseAgent):
    def move(self):
        neighbours = self._get_valid_neighbours()
        if neighbours:
            self._x, self._y = random.choice(neighbours)
            self._steps += 1
```

#### Polymorphism

Polymorphism means different classes can share the same method name but
behave differently. Both `RandomAgent` and `GreedyAgent` have a `move()`
method, but their logic is completely different:

- `RandomAgent.move()` picks a random valid neighbour
- `GreedyAgent.move()` picks the neighbour closest to the goal

This means the simulation can call `agent.move()` without needing to know
which type of agent it is — the correct behaviour happens automatically.

### Design Pattern

This project implements two design patterns: the **Singleton Pattern** in
`FileManager` and the **Factory Pattern** in `main.py`.

#### Singleton Pattern

The Singleton Pattern ensures that only one instance of a class can ever
exist. This is implemented in the `FileManager` class using Python's
`__new__` method:

```python
class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Every time `FileManager()` is called, Python checks if an instance already
exists. If it does, it returns the existing one instead of creating a new one.
This can be verified like so:

```python
fm1 = FileManager()
fm2 = FileManager()
fm1 is fm2  # True — they are the exact same object
```

The Singleton Pattern is suitable here because there should only ever be one
central point responsible for reading and writing simulation results. Having
multiple `FileManager` instances could cause conflicts when writing to the
same file simultaneously.

#### Factory Pattern

The Factory Pattern provides a way to create objects without specifying the
exact class directly. In `main.py`, the `agent_factory()` function takes a
string input and returns the correct agent object:

```python
def agent_factory(agent_type: str, grid: Grid):
    agents = {
        "random": RandomAgent,
        "greedy": GreedyAgent
    }
    if agent_type not in agents:
        raise ValueError(f"Unknown agent type: {agent_type}")
    return agents[agent_type](grid)
```

Instead of the simulation directly creating `RandomAgent(grid)` or
`GreedyAgent(grid)`, it simply calls `agent_factory("random", grid)` and
gets back the correct agent. This makes it easy to add new agent types in
the future - you only need to add a new entry to the `agents` dictionary
without changing any other code.

The Factory Pattern was chosen here because the type of agent needed is
determined at runtime based on user input, making a factory function a
natural and flexible solution.

### Composition and Aggregation

Composition is when one class is made up of objects of another class.
The `Grid` class is composed of `Cell` objects — it creates and owns them,
and they cannot exist independently of the grid:

```python
cell = Cell(x, y, cell_type.strip())
grid_row.append(cell)
```

The entire grid world is built from individual `Cell` objects, each knowing
their own position and type.

---

### File I/O

This project uses CSV files for both reading and writing data. The `csv`
module built into Python is used throughout.

#### Reading - Loading the Grid

The grid world is loaded from `data/world.csv` when the simulation starts.
The `Grid` class reads the file row by row and converts each value into a
`Cell` object:

```python
def __load(self, filepath):
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        for y, row in enumerate(reader):
            grid_row = []
            for x, cell_type in enumerate(row):
                cell = Cell(x, y, cell_type.strip())
                grid_row.append(cell)
```

The `world.csv` file defines the layout of the grid world using these
symbols:

| Symbol | Meaning |
|--------|---------|
| S | Start position |
| G | Goal position |
| W | Wall |
| E | Empty cell |

#### Writing - Saving Results

After each simulation run, the result is saved to `data/results.csv` using
the `FileManager` class. The file is opened in append mode (`"a"`) so
previous results are never overwritten:

```python
def save_result(self, agent_type: str, steps: int, filepath: str = "data/results.csv"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, agent_type, steps]
    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)
```

Each row in `results.csv` contains the timestamp, agent type, and number
of steps taken. For example:

2026-04-25 15:48:17,random,56

---

### Testing

Unit tests are written using Python's built-in `unittest` framework and
are located in `tests/test_agent.py`. The tests cover the core functionality
of all major classes.

To run the tests:

```bash
python -m unittest tests/test_agent.py
```

#### TestCell

Tests for the `Cell` class verify that:
- Cell types are loaded correctly from the CSV file
- Empty cells are correctly identified as walkable
- Wall cells are correctly identified as not walkable
- The goal cell is correctly identified
- Setting an invalid cell type raises a `ValueError`

#### TestGrid

Tests for the `Grid` class verify that:
- The start and goal positions are loaded correctly
- The grid dimensions are correct (5x5)
- Valid moves are correctly identified
- Moving into a wall is correctly rejected
- Moving outside the grid boundaries is correctly rejected

#### TestAgents

Tests for `RandomAgent` and `GreedyAgent` verify that:
- Agents start at the correct start position
- Agents start with 0 steps
- Agents correctly increment steps after each move
- Agents have not reached the goal at the start
- The `GreedyAgent` always reaches the goal within 100 steps

#### TestFileManager

Tests for the `FileManager` class verify that:
- The Singleton pattern works correctly - two instances of `FileManager`
are always the exact same object

All 18 tests pass successfully.

---

## 3. Results and Summary

### Results

- The simulation was successfully implemented with two agent types:
  `RandomAgent` and `GreedyAgent`. Both agents are able to navigate the
  grid world and reach the goal, demonstrating the core functionality of
  the program.

- All 4 OOP pillars were implemented and demonstrated across the project:
  encapsulation in `Cell` and `Grid`, abstraction and inheritance in
  `BaseAgent`, and polymorphism through the different `move()` behaviours
  of `RandomAgent` and `GreedyAgent`.

- The Singleton and Factory design patterns were successfully applied.
  `FileManager` ensures only one instance handles file operations, and
  `agent_factory()` cleanly handles agent creation based on user input.

- All 18 unit tests pass successfully, covering the core functionality of
  `Cell`, `Grid`, `RandomAgent`, `GreedyAgent` and `FileManager`.

- One challenge faced during implementation was transitioning from
  explicit getter methods like `get_x()` to Python `@property` decorators,
  which required updating all references across multiple files consistently.

---

### Conclusions

This project successfully demonstrates the application of Object-Oriented
Programming principles in Python through a Grid World Agent Simulation.
The program implements all 4 OOP pillars, two design patterns, composition
between `Grid` and `Cell`, file reading and writing, and a full unit test
suite.

The result is a working simulation where an agent navigates a grid world
loaded from a CSV file, with results saved automatically after each run.
The `GreedyAgent` consistently reaches the goal in fewer steps than the
`RandomAgent` due to its goal-directed movement logic.

### Future Prospects

Future improvements could include:
- Adding more agent types such as a wall-avoiding agent or a
  pathfinding agent using algorithms like A* or Dijkstra
- Adding a visual interface using a library like `pygame` instead of
  printing to the console
- Allowing the user to design their own grid world through the program
  instead of editing the CSV file manually
- Adding difficulty levels by generating random grid worlds of different
  sizes and wall densities

---

## 4. Resources

https://docs.python.org/3/library/csv.html
https://docs.python.org/3/library/abc.html
https://docs.python.org/3/library/unittest.html
https://www.geeksforgeeks.org/python/factory-method-python-design-patterns/
https://git-scm.com/docs/gittutorial
https://www.geeksforgeeks.org/python/singleton-pattern-in-python-a-complete-guide/