# zmodule.py

from config.config import Configuration

class SomeModule:
    def __init__(self, config):
        self.config = config

    def perform_action(self):
        # Access configuration parameters and perform actions
        api_key = self.config.api_key
        max_attempts = self.config.max_attempts
        log_level = self.config.log_level
        
