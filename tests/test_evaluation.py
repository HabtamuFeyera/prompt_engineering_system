
import unittest
from backend.evaluation.monte_carlo_matchmaking import MonteCarloMatchmaking
from backend.evaluation.elo_rating_system import ELORatingSystem

class TestEvaluationMethods(unittest.TestCase):
    def test_monte_carlo_matchmaking(self):
        monte_carlo_matchmaker = MonteCarloMatchmaking()
        result = monte_carlo_matchmaker.match_prompts(["Prompt 1", "Prompt 2"])
       
        self.assertEqual(result, "Match Result")

    def test_elo_rating_system(self):
        elo_rating_system = ELORatingSystem()
        result = elo_rating_system.rate_prompts(["Prompt 1", "Prompt 2"])
        
        self.assertEqual(result, {"Prompt 1": 1200, "Prompt 2": 1100})

if __name__ == "__main__":
    unittest.main()
