
from prompt_generation.prompt_generator import PromptGenerator
from test_case_generation.test_case_generator import TestCaseGenerator
from evaluation.monte_carlo_matchmaking import MonteCarloMatchmaking
from evaluation.elo_rating_system import ELORatingSystem

class PromptEngineeringApp:
    def __init__(self):
        self.prompt_generator = PromptGenerator()
        self.test_case_generator = TestCaseGenerator()
        self.monte_carlo_matchmaker = MonteCarloMatchmaking()
        self.elo_rating_system = ELORatingSystem()

    def run(self):
        
        pass
