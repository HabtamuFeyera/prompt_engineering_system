
class Configuration:
    def __init__(self):
        # Define configuration parameters or settings
        self.api_key = "my_api_key"
        self.max_attempts = 3
        self.log_level = "info"

    def update_config(self, api_key=None, max_attempts=None, log_level=None):
        # Update configuration parameters
        if api_key:
            self.api_key = api_key
        if max_attempts:
            self.max_attempts = max_attempts
        if log_level:
            self.log_level = log_level


