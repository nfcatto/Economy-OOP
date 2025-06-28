from abc import ABC, abstractmethod

class EconomicAgent(ABC):
    @abstractmethod
    def act(self, economy_state: dict) -> dict:
        """Take action based on economic conditions"""
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