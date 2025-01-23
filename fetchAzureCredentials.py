import requests

# Setting variables
dt_env_url = "<Env URL Here>"
dt_api_token = "<API Token Here>"

# Setting headers 
headers = {
    "Authorization": f"Api-Token {dt_api_token}",
    "Content-Type": "application/json",
}

# GET request to retrieve all Azure Monitor configuration IDs and name
get_url = f"{dt_env_url}/api/config/v1/azure/credentials/"
get_response = requests.get(get_url, headers=headers)

# Exception handling
if get_response.status_code == 200:
    print("Azure Monitor configuration details:")
    print(get_response.json())
else:
    print(f"Failed to retrieve Azure Monitor credential info. Status code: {get_response.status_code}")
    print(get_response.json())