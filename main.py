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