import random

class PromptTestingAndRanking:
    def __init__(self, evaluation_data_generator):
        self.evaluation_data_generator = evaluation_data_generator
        self.prompt_candidates = []
        self.matchups_history = {}
        self.elo_ratings = {}

    def add_prompt_candidates(self, prompt_candidates):
        """
        Add prompt candidates to the testing and ranking system.

        Args:
        - prompt_candidates (list): List of prompt candidates.
        """
        self.prompt_candidates = prompt_candidates
        self.initialize_elo_ratings()

    def initialize_elo_ratings(self):
        """
        Initialize ELO ratings for each prompt candidate.
        """
        for prompt_candidate in self.prompt_candidates:
            self.elo_ratings[prompt_candidate] = 1000  # Initial ELO rating

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

            # Update ELO ratings
            self.update_elo_ratings(winner, loser)

            matchups_outcomes[matchup] = winner

        return matchups_outcomes

    def update_elo_ratings(self, winner, loser, k=32):
        """
        Update ELO ratings based on the outcome of a matchup.

        Args:
        - winner (str): Winner prompt candidate.
        - loser (str): Loser prompt candidate.
        - k (int): ELO rating update constant.
        """
        rating_difference = self.elo_ratings[winner] - self.elo_ratings[loser]
        expected_outcome = 1 / (1 + 10 ** (-rating_difference / 400))

        self.elo_ratings[winner] += k * (1 - expected_outcome)
        self.elo_ratings[loser] -= k * expected_outcome

    def rank_prompts(self):
        """
        Rank prompt candidates based on their ELO ratings.

        Returns:
        - list: Ranked prompt candidates.
        """
        ranked_prompts = sorted(self.elo_ratings, key=lambda x: self.elo_ratings[x], reverse=True)
        return ranked_prompts


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

# Rank prompts based on ELO ratings
ranked_prompts = prompt_testing_and_ranking.rank_prompts()
print("\nRanked Prompts:")
for i, prompt in enumerate(ranked_prompts, 1):
    print(f"{i}. {prompt} - ELO Rating: {prompt_testing_and_ranking.elo_ratings[prompt]}")
