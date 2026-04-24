import csv
from datetime import datetime


class FileManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def save_result(self, agent_type, steps, filepath: str = "data/results.csv"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, agent_type, steps]

        with open(filepath, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)

        print(f"Result saved to {filepath}")

    def load_results(self, filepath: str = "data/results.csv"):
        results = []
        try:
            with open(filepath, newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    results.append(row)
        except FileNotFoundError:
            print("No results file found yet.")
        return results

    def print_results(self, filepath: str = "data/results.csv"):
        results = self.load_results(filepath)
        if results:
            print("\n--- Simulation Results ---")
            for row in results:
                print(f"Date: {row[0]} | Agent: {row[1]} | Steps: {row[2]}")
        else:
            print("No results to display.")

        
    


