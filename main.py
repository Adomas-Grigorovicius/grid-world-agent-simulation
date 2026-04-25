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

def run_simulation(agent_type: str):
    grid = Grid("data/world.csv")
    agent = agent_factory(agent_type, grid)
    file_manager = FileManager()

    print(f"\nStarting simulation with {agent_type.capitalize()}Agent")
    print(f"Goal: ({grid.goal.x}, {grid.goal.y})\n")

    grid.display(agent._x, agent._y)

    while not agent.has_reached_goal():
        agent.move()
        grid.display(agent._x, agent._y)

    print(f"Goal reached in {agent.steps} steps!")
    file_manager.save_result(agent_type, agent.steps)

def main():
    print("=== Grid World Agent Simulation ===")
    print("Select agent type:")
    print("1. Random Agent")
    print("2. Greedy Agent")

    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "1":
        run_simulation("random")
    elif choice == "2":
        run_simulation("greedy")
    else:
        print("Invalid choice, please enter 1 or 2.")
        return

    file_manager = FileManager()
    file_manager.print_results()


if __name__ == "__main__":
    main()