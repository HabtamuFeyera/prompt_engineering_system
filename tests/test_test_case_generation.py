
import unittest
from backend.test_case_generation.test_case_generator import TestCaseGenerator

class TestTestCaseGeneration(unittest.TestCase):
    def test_generate_test_cases(self):
        test_case_generator = TestCaseGenerator()
        result = test_case_generator.generate_test_cases("User Input")
        
        self.assertEqual(result, ["Test Case 1", "Test Case 2"])

if __name__ == "__main__":
    unittest.main()
