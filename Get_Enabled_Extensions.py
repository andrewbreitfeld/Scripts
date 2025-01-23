import requests
import json

# Dynatrace ENV URL and API token (requires ReadConfig scope)
env_url = "<Env URL Here>"
api_token = "<ReadConfig API Token Here>"

# Headers
headers = {
    "Authorization": f"Api-Token {api_token}",
    "Content-Type": "application/json"
}

# Retrieve all extension IDs
get_1_0_extensions = requests.get(env_url + "/api/config/v1/extensions", headers=headers)

# Exception handling for first request getting extension IDs
if get_1_0_extensions.status_code != 200:
   print(f"Get 1.0 extensions API request returned a status code of {get_1_0_extensions.status_code}.") 
   print(f"Error Message: {get_1_0_extensions.text}")
   print("\n")

# Putting json response into a variable
pretty_1_0_extensions = json.loads(get_1_0_extensions.content)

# Put extension ids in an array
extension_ids = []
for extensions in pretty_1_0_extensions['extensions']:
  extension_ids.append(extensions['id'])

# Print list of 1.0 extensions that exist in given env
print("List of 1.0 extensions in the env:")
print(extension_ids)
print("\n")

# Loop through the list of extension IDs for their state info
for extension_id in extension_ids:
    extension_state_api_url = f"{env_url}/api/config/v1/extensions/{extension_id}/states"
    get_1_0_extension_state = requests.get(extension_state_api_url, headers=headers)
    
    # Printing results and exception handling for each extension id state 
    if get_1_0_extension_state.status_code == 200:
        state_json = get_1_0_extension_state.json()
        if state_json['totalResults'] != 0:
            print(f"Extension ID: {extension_id}")
            print(f"States: {state_json['states']}")
            print(f"Total Results: {state_json['totalResults']}")
            print("\n")
        else:
            print(f"No enabled setting instances found for extension ID: {extension_id}")
    else:
        print(f"Extension state API request returned a status code of {get_1_0_extension_state.status_code}.") 
        print(f"Error Message: {get_1_0_extension_state.text}")
        print("\n")