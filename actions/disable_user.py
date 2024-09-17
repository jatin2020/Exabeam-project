from connector import BeyondIdentityConnector

def disable_user_action(userId):
    # Initialize the connector
    token = "api_token"
    connector = BeyondIdentityConnector(token)

    try:
        # Call the disable_user method with the userId
        result = connector.disable_user(userId)
        if result.get("active") == False:
            # Return success if the user is disabled
            return {
                "status": "success"
            }
        else:
            # Return failure if the user is not disabled
            return {
                "status": "failure"
            }
    except Exception as e:
        # Handle errors and return an error status
        return {
            "status": f"error: {str(e)}"
        }

# Example execution
if __name__ == "__main__":
    result = disable_user_action(userId="user18")
    print(result)
