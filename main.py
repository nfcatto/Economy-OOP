from typing import Dict, List

class Agent:
    def act(self, state: Dict[str, float]) -> Dict[str, float]:
        pass

class Consumer(Agent):
    def __init__(self, savings: float = 1000):
        self.savings = savings
        
    def act(self, state: Dict[str, float]) -> Dict[str, float]:
        inflation = state['inflation']
        wage = state['wage']
        
        save_rate = max(0.1, 0.2 - inflation)
        self.savings += wage * save_rate
        spend = wage * (1 - save_rate)
        
        return {'spend': spend, 'saved': self.savings}
    
class Business(Agent):
    def act(self, state: Dict[str, float]) -> Dict[str, float]:
        demand = state['demand']
        interest = state['interest']
        
        production = demand * (1 - interest)
        return {'produce': production}

class Economy:
    def __init__(self):
        self.agents: List[Agent] = []
        self.state = {
            'inflation': 0.02,
            'wage': 50,
            'demand': 100,
            'interest': 0.05
        }
        def add_agent(self, agent: Agent):
            self.agents.append(agent)
    
    def run_cycle(self):
        print("\n--- Economic Cycle ---")
        
        # Agents act
        actions = []
        for agent in self.agents:
            action = agent.act(self.state)
            actions.append(action)
            print(f"{type(agent).__name__}: {action}")
        
        # Update state
        total_spend = sum(a['spend'] for a in actions if 'spend' in a)
        total_produce = sum(a['produce'] for a in actions if 'produce' in a)
        
        self.state['demand'] = total_spend * 0.9
        self.state['inflation'] = min(0.1, total_spend / (total_produce + 1))
        self.state['interest'] = 0.02 + (self.state['inflation'] * 0.5)
        
        print("New state:", {k: round(v, 2) for k, v in self.state.items()})

def main():
    economy = Economy()
    
    # Get user inputs
    print("Welcome to Simple Economy Simulator")
    
    # Set initial economy state
    print("\nSet initial economy conditions:")
    economy.state['inflation'] = float(input("Inflation rate (0.0-1.0): "))
    economy.state['wage'] = float(input("Base wage: "))
    economy.state['demand'] = float(input("Initial demand: "))
    economy.state['interest'] = float(input("Interest rate (0.0-1.0): "))
    
    # Add consumers
    num_consumers = int(input("\nNumber of consumers: "))
    for i in range(num_consumers):
        savings = float(input(f"Consumer {i+1} initial savings: "))
        economy.add_agent(Consumer(savings))
    
    # Add businesses
    num_businesses = int(input("\nNumber of businesses: "))
    for i in range(num_businesses):
        economy.add_agent(Business())
    
    # Run simulation
    cycles = int(input("\nNumber of cycles to run: "))
    for _ in range(cycles):
        economy.run_cycle()

if __name__ == "__main__":
    main()