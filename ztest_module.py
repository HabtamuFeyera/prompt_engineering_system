
import unittest
from config.config import Configuration

class TestConfigurations(unittest.TestCase):
    def test_configuration_update(self):
        # Set up an initial configuration
        config_instance = Configuration()

        # Update the configuration for testing
        config_instance.update_config(api_key="test_api_key", max_attempts=2, log_level="error")

        # Perform tests based on the test configuration
        self.assertEqual(config_instance.api_key, "test_api_key")
        self.assertEqual(config_instance.max_attempts, 2)
        self.assertEqual(config_instance.log_level, "error")
