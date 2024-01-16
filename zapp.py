# zapp.py

from config.config import Configuration

# Initialize the configuration
config_instance = Configuration()

# Access configuration parameters
api_key = config_instance.api_key
max_attempts = config_instance.max_attempts
log_level = config_instance.log_level

# Use the configuration parameters in your application logic
