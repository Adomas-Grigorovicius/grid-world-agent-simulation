from simulation.grid import Grid
from simulation.agent import RandomAgent, GreedyAgent
from simulation.file_manager import FileManager


def agent_factory(agent_type: str, grid: Grid):
    agents = {
        "random": RandomAgent,
        "greedy": GreedyAgent
    }
    if agent_type not in agents:
        raise ValueError(f"Unknown agent type: {agent_type}")
    return agents[agent_type](grid)