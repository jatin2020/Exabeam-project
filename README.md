# Beyond Identity Service for Exabeam Action Editor

# Project Overview

This project implements a custom service in Exabeam's Action Editor to manage user operations via the Beyond Identity SCIM API. The service includes two key actions:

    Create a New User: Creates a new user in Beyond Identity.
    Disable a User: Disables an existing user in Beyond Identity.

The playbook automates the process of creating and immediately disabling a user as part of an Incident Response workflow or for testing purposes. It handles inputs, outputs, and errors gracefully, ensuring smooth operation.

# Service Components

The service is made up of the following files:

    connector.py: This file handles communication with the Beyond Identity SCIM API, including API authentication (API token) and endpoint interaction.
    __init__.py: This file initializes the service and makes it available in the Action Editor.
    requirements.txt: Specifies the Python dependencies required to run the service (e.g., requests library for API communication).

# Custom Actions
1. Create a New User

    Description: This action creates a new user in Beyond Identity by sending a request to the SCIM API. It accepts user details as inputs and returns the newly created user’s ID and status.

    Inputs:
        userName: The username for the new user.
        displayName: The display name of the user.
        email: The user's primary email address.
        givenName: The user's first name.
        familyName: The user's last name.

    Outputs:
        userId: The unique ID of the newly created user.
        status: Success or error message.

    Error Handling: Handles validation errors (e.g., missing fields), API response errors (e.g., invalid API token).

2. Disable a User

    Description: This action disables an existing user by setting their status to inactive using the Beyond Identity SCIM API. It accepts the user’s ID as input and returns the success status of the action.

    Inputs:
        userId: The unique ID of the user to be disabled.

    Outputs:
        status: Success or error message.

    Error Handling: Handles cases where the user ID is invalid or the API request fails.

# Running the Playbook
Prerequisites

    Exabeam Action Editor: Make sure Exabeam's Action Editor is available and configured for your environment.
    Beyond Identity API Credentials: Obtain an API token and any other necessary authentication information (tenant ID, realm ID) from Beyond Identity.
    Python Dependencies: Install dependencies listed in requirements.txt using the command: pip install -r requirements.txt

Instructions to Set Up and Run the Playbook

    Step 1: Configure the Service
        Upload the custom service files (connector.py, __init__.py, requirements.txt) to Exabeam's Action Editor.
        Set up the necessary API credentials (API token, tenant ID, etc.) in connector.py to enable communication with the Beyond Identity SCIM API.

    Step 2: Configure the Actions
        Define the two actions:
            Create a New User: This action requires inputs such as userName, displayName, email, givenName, and familyName.
            Disable a User: This action requires userId as an input.
        Configure the outputs of these actions (userId and status) to be displayed in the Exabeam workbench.

    Step 3: Create the Playbook Workflow
        Build a new playbook in Exabeam’s Incident Responder.
        Add the Create a New User action as the first step.
        Add a conditional check to see if the user creation was successful (based on status == 'success').
        If successful, trigger the Disable a User action using the userId from the previous step.
        Log errors and outputs to the workbench for monitoring.

    Step 4: Test the Playbook
        Execute the playbook by providing sample input data for user creation.
        Verify that a new user is created, and upon success, the same user is disabled.
        Review the output in the Exabeam workbench, ensuring that the process is logged and any errors are captured.

    Step 5: Monitoring and Output
        The outputs of each action (e.g., userId, status) will be displayed in a table in the Exabeam workbench.
        If an error occurs at any step, helpful error messages will be shown for troubleshooting.

# Error Handling and Logging

Both actions handle errors gracefully, including:

    Missing or invalid input fields: Displays error messages indicating the missing information.
    API-related issues: Handles issues like invalid tokens, network failures, and non-responsive endpoints.
    Invalid user data: Catches errors when attempting to disable a non-existent user.

Errors are logged and displayed in the Exabeam workbench for easy troubleshooting.
