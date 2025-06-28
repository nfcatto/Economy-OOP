from abc import ABC, abstractmethod
from typing import Dict, List

class EconomicEntity(ABC):
    """Base class for all economic entities"""
    @abstractmethod
    def calculate(self, economy_state: Dict[str, float]) -> Dict[str, float]:
        pass

class Consumer(EconomicEntity):
    def __init__(self, name: str, initial_savings: float):
        self.name = name
        self.savings = initial_savings
        
    def calculate(self, economy_state: Dict[str, float]) -> Dict[str, float]:
        inflation = economy_state.get('inflation', 0.02)
        wage = economy_state.get('wage', 50)
        
        savings_rate = max(0.1, 0.2 - inflation)  # At least 10% savings
        self.savings += wage * savings_rate
        spending = wage * (1 - savings_rate)
        
        return {
            'agent_type': 'Consumer',
            'name': self.name,
            'spending': spending,
            'new_savings': self.savings,
            'savings_rate': savings_rate
        }
    
class Business(EconomicEntity):
    def __init__(self, name: str, production_capacity: float):
        self.name = name
        self.capacity = production_capacity
        
    def calculate(self, economy_state: Dict[str, float]) -> Dict[str, float]:
        demand = economy_state.get('demand', 100)
        interest = economy_state.get('interest', 0.05)
        
        production = min(self.capacity, demand * (1 - interest))
        profit = production * 0.2  # Simple 20% margin
        
        return {
            'agent_type': 'Business',
            'name': self.name,
            'production': production,
            'profit': profit,
            'utilization': production / self.capacity
        }
    

