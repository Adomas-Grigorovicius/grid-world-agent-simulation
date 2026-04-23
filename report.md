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

### How to use the program?

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
    def get_type(self):
        return self.__cell_type
    
    @cell_type.setter
    def set_type(self, cell_type):
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

### File I/O

### Testing

---

## 3. Results and Summary

### Results

### Conclusions

### Future Prospects

---

## 4. Resources

https://www.geeksforgeeks.org
https://www.w3schools.com
https://docs.python.org/3/