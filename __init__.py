# __init__.py

# Importing necessary modules and action functions
from .connector import BeyondIdentityConnector
from .actions import create_user, disable_user
import os

# Define the class for initializing the Beyond Identity service
class BeyondIdentityService:
    def __init__(self):
        api_token = os.getenv('API_TOKEN')
        # Initialize the connector to communicate with Beyond Identity API
        self.connector = BeyondIdentityConnector()

        # Register actions to the service
        self.actions = {
            "create_user": create_user,
            "disable_user": disable_user
        }

    def run_action(self, action_name, **kwargs):
        # Execute the requested action if it exists
        if action_name in self.actions:
            return self.actions[action_name](self.connector, **kwargs)
        else:
            raise ValueError(f"Action '{action_name}' not recognized.")

# Initialize the service when this module is loaded
service = BeyondIdentityService()
