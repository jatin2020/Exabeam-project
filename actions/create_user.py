from connector import BeyondIdentityConnector

def create_user_action(userName, displayName, email, givenName, familyName):

    user_data = {
        "userName": userName,
        "displayName": displayName,
        "emails": [
            {
                "value": email,
                "primary": True
            }
        ],
        "name": {
            "givenName": givenName,
            "familyName": familyName
        },
        "active": True
    }

    # Initialize the connector
    token = "api_token"
    connector = BeyondIdentityConnector(token)

    try:
        # Call the create_user method
        result = connector.create_user(user_data)
        # Return the ID and status if the user was successfully created
        return {
            "userId": result.get("id"),
            "status": "success"
        }
    except Exception as e:
        # Handle errors and return an error status
        return {
            "status": f"error: {str(e)}"
        }

# Example execution 
if __name__ == "__main__":
    result = create_user_action(
        userName="jatin.jena",
        displayName="Jatin Jena",
        email="jatin.jena@6sense.com",
        givenName="Jatin",
        familyName="Jena"
    )
    print(result)
