import unittest
from main import Consumer, Business, Economy

class TestConsumer(unittest.TestCase):
    def test_spending(self):
        consumer = Consumer(savings=1000)
        state = {'inflation': 0.1, 'wage': 100}
        result = consumer.act(state)
        
        # Should save at least 10% (max(0.1, 0.2-0.1))
        self.assertAlmostEqual(result['spend'], 90) 
        self.assertAlmostEqual(result['saved'], 1010) 

class TestBusiness(unittest.TestCase):
    def test_production(self):
        business = Business()
        state = {'demand': 200, 'interest': 0.1}
        result = business.act(state)
        
        self.assertAlmostEqual(result['produce'], 180) 

class TestEconomy(unittest.TestCase):
    def test_simulation(self):
        economy = Economy()
        economy.add_agent(Consumer(savings=1000))
        economy.add_agent(Business())
        
        # Run one cycle
        economy.run_cycle()

        
        self.assertNotEqual(economy.state['demand'], 100)  # Initial demand was 100
        self.assertTrue(economy.state['inflation'] > 0.02)  # Inflation should increase

if __name__ == '__main__':
    unittest.main()
