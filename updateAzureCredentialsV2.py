import requests

# Setting variables
dt_env_url = "<Env URL Here>"
dt_api_token = "<API Token Here>"
dt_azure_credentials_id = "<Azure Cred Entity>"
secret_key = "<Azure SecretKey>"

# Setting headers 
headers = {
    "Authorization": f"Api-Token {dt_api_token}",
    "Content-Type": "application/json",
}

# GET request to retrieve Azure credential specifics for the given id
get_url = f"{dt_env_url}/api/config/v1/azure/credentials/{dt_azure_credentials_id}"
get_response = requests.get(get_url, headers=headers)

# Formulating the subsequent PUT update request payload
if get_response.status_code == 200:
    get_response_config_data = get_response.json()
    label = get_response_config_data["label"]
    app_id = get_response_config_data["appId"]
    directory_id = get_response_config_data["directoryId"]
    auto_tagging = get_response_config_data["autoTagging"]
    monitor_only_tagged_entities = get_response_config_data["monitorOnlyTaggedEntities"]

    updated_config_json = {
        "label": label,
        "appId": app_id,
        "directoryId": directory_id,
        "key": secret_key,
        "autoTagging": auto_tagging,
        "monitorOnlyTaggedEntities": monitor_only_tagged_entities
    }

# PUT request to update Azure credentials
    put_url = f"{dt_env_url}/api/config/v1/azure/credentials/{dt_azure_credentials_id}"
    put_response = requests.put(put_url, json=updated_config_json, headers=headers)
    
# Exception handling
    if put_response.status_code == 201 or put_response.status_code == 204:
        print("Azure credentials updated successfully!")
    else:
        print(f"Failed to update Azure credential configuration. Status code: {put_response.status_code}")
else:
    print(f"Failed to retrieve Azure configuration info. Status code: {get_response.status_code}")
    print(get_response.json())
