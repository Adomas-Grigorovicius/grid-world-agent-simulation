# Grid World Agent Simulation

## Introduction

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

Make sure you have Python installed (version 3.10 or higher). To check, run:

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

```
=== Grid World Agent Simulation ===
Select agent type:
1. Random Agent
2. Greedy Agent

Enter 1 or 2:
```

Enter `1` to run the **Random Agent**, which moves to a random valid
neighbouring cell each step, or `2` to run the **Greedy Agent**, which
always moves toward the cell closest to the goal.

The grid will be printed to the console at each step of the simulation,
showing the current state of the world:

- `S` - Start position
- `G` - Goal position
- `W` - Wall (not walkable)
- `E` - Empty cell (walkable)
- `A` - Current agent position

The simulation ends automatically when the agent reaches the goal. The
number of steps taken is displayed and the result is saved to
`data/results.csv`. All previous results are then printed to the console.

---

## Design

### 4 OOP Pillars

| Pillar          | Where                                                              |
|------------------|---------------------------------------------------------------------|
| Encapsulation | `Cell`/`Grid` use name-mangled private attributes (`__x`, `__y`, …) exposed via `@property`. |
| Abstraction    | `BaseAgent(ABC)` defines the `move()` contract without an implementation. |
| Inheritance     | `RandomAgent` and `GreedyAgent` inherit shared state/behaviour from `BaseAgent`. |
| Polymorphism | `move()` is called uniformly on any `BaseAgent`, but resolves to different logic per subclass. |

### Design patterns

- **Factory** - `agent_factory()` in `main.py` decouples agent construction
  from the calling code; new agent types are added by extending one dict.
- **Singleton** - `FileManager` guarantees a single instance via `__new__`,
  so all reads/writes to `data/results.csv` go through one object.

### Composition vs. aggregation

- `Grid` **owns** its `Cell` objects (composition) - cells are constructed
  inside `Grid.__load()` and have no meaningful existence outside a grid.
- `Agent` **references** a `Grid` (aggregation) - the grid is constructed
  externally and passed in; an agent doesn't own the grid's lifecycle, and
  the same grid instance could in principle be shared across agents.

### File I/O

This project uses CSV files for both reading and writing data. The `csv`
module built into Python is used throughout.

#### Reading - Loading the Grid

The grid world is loaded from `data/world.csv` when the simulation starts.
The `Grid` class reads the file row by row and converts each value into a
`Cell` object.

#### Writing - Saving Results

After each simulation run, the result is saved to `data/results.csv` using
the `FileManager` class. The file is opened in append mode (`"a"`) so
previous results are never overwritten.

Each row in `results.csv` contains the timestamp, agent type, and number
of steps taken. For example:

```
2026-04-25 15:48:17,random,56

```

---

### Testing

Unit tests are written using Python's built-in `unittest` framework and
are located in `test/test_agent.py`. The tests cover the core functionality
of all major classes.

To run the tests:

```bash
python -m unittest test/test_agent.py
```

---

## Known limitations

- `RandomAgent` has no step cap or visited-cell tracking, so on a grid
  where the start and goal aren't connected it would run indefinitely.
  The bundled `world.csv` is guaranteed solvable, so this doesn't surface
  in normal use.
- `Cell`'s type validation lives in its property setter, but the
  constructor currently assigns the private attribute directly rather
  than going through the setter, so a malformed CSV entry isn't caught
  at load time.
- `GreedyAgent` uses a pure Manhattan-distance heuristic with no
  backtracking or visited-cell memory. It reaches the goal reliably on
  the bundled grid, but a purely greedy strategy like this isn't
  guaranteed to terminate on an arbitrary grid - it can oscillate
  between two equally-close cells or stall at a local minimum around a
  wall.

*(These are tracked and will be fixed in a follow-up commit this
section will shrink as they're addressed.)*

---

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
