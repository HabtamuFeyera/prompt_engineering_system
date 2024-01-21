
import unittest
from backend.prompt_generation.prompt_generator import PromptGenerator

class TestPromptGeneration(unittest.TestCase):
    def test_generate_prompt(self):
        prompt_generator = PromptGenerator()
        result = prompt_generator.generate_prompt("User Input")
      
        self.assertEqual(result, "Expected Prompt")

if __name__ == "__main__":
    unittest.main()
