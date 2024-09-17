import requests

class BeyondIdentityConnector:
    def __init__(self, token):
        self.base_url = "https://api.beyondidentity.com/scim/v2"
        self.token = token

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_user(self, user_data):
        url = f"{self.base_url}/Users"
        try:
            response = requests.post(url, json=user_data, headers=self._get_headers())
            response.raise_for_status()  # request was successful
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"Other error occurred: {err}")

    def disable_user(self, user_id):
        url = f"{self.base_url}/Users/{user_id}"
        data = {
            "active": False  # This assumes the API allows disabling a user by setting active to False
        }
        try:
            response = requests.patch(url, json=data, headers=self._get_headers())
            response.raise_for_status()  # request was successful
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"Other error occurred: {err}")
