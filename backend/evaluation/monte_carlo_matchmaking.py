
import random
import math

class PromptTestingAndRanking:
    def __init__(self, evaluation_data_generator, exploration_rate=0.2):
        self.evaluation_data_generator = evaluation_data_generator
        self.prompt_candidates = []
        self.matchups_history = {}
        self.bandit_rewards = {}
        self.exploration_rate = exploration_rate

    def add_prompt_candidates(self, prompt_candidates):
        """
        Add prompt candidates to the testing and ranking system.

        Args:
        - prompt_candidates (list): List of prompt candidates.
        """
        self.prompt_candidates = prompt_candidates
        self.initialize_bandit_rewards()

    def initialize_bandit_rewards(self):
        """
        Initialize rewards for each prompt candidate in the Multi-Armed Bandit.
        """
        for prompt_candidate in self.prompt_candidates:
            self.bandit_rewards[prompt_candidate] = {"wins": 0, "losses": 0}

    def perform_monte_carlo_matchmaking(self, num_matchups=10):
        """
        Perform Monte Carlo Matchmaking to simulate prompt matchups.

        Args:
        - num_matchups (int): Number of matchups to simulate.

        Returns:
        - dict: Dictionary containing matchups and their outcomes.
        """
        matchups_outcomes = {}

        for _ in range(num_matchups):
            matchup = random.sample(self.prompt_candidates, 2)
            winner = random.choice(matchup)
            loser = matchup[0] if matchup[0] != winner else matchup[1]

            # Update matchups history
            if matchup not in self.matchups_history:
                self.matchups_history[matchup] = {"wins": 0, "losses": 0}
            self.matchups_history[matchup]["wins"] += 1

            # Update Multi-Armed Bandit rewards
            self.bandit_rewards[winner]["wins"] += 1
            self.bandit_rewards[loser]["losses"] += 1

            matchups_outcomes[matchup] = winner

        return matchups_outcomes

    def select_prompt_to_evaluate(self):
        """
        Select a prompt candidate to evaluate using the Multi-Armed Bandit Algorithm.

        Returns:
        - str: Selected prompt candidate.
        """
        total_evaluations = sum(self.bandit_rewards[prompt]["wins"] + self.bandit_rewards[prompt]["losses"] for prompt in self.prompt_candidates)

        if random.uniform(0, 1) < self.exploration_rate:
            # Explore: Randomly choose a prompt to evaluate
            return random.choice(self.prompt_candidates)
        else:
            # Exploit: Choose the prompt with the highest reward estimate (wins / total evaluations)
            rewards_estimates = {prompt: (self.bandit_rewards[prompt]["wins"] + 1) / (total_evaluations + 1) for prompt in self.prompt_candidates}
            selected_prompt = max(rewards_estimates, key=rewards_estimates.get)
            return selected_prompt

# Usage:
evaluation_data_generator = EvaluationDataGenerator()
prompt_testing_and_ranking = PromptTestingAndRanking(evaluation_data_generator)

# User input
prompt_candidates = ["Prompt 1", "Prompt 2", "Prompt 3"]
evaluation_data_generator.generate_evaluation_data("User's description", num_test_cases=5)

# Add prompt candidates to the system
prompt_testing_and_ranking.add_prompt_candidates(prompt_candidates)

# Perform Monte Carlo Matchmaking
matchups_outcomes = prompt_testing_and_ranking.perform_monte_carlo_matchmaking(num_matchups=10)
print("Matchups Outcomes:")
for matchup, winner in matchups_outcomes.items():
    print(f"{matchup[0]} vs {matchup[1]} - Winner: {winner}")

# Select a prompt to evaluate using the Multi-Armed Bandit Algorithm
selected_prompt = prompt_testing_and_ranking.select_prompt_to_evaluate()
print(f"\nSelected Prompt to Evaluate: {selected_prompt}")
