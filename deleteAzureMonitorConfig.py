import requests

# Setting variables
dt_env_url = "<Env URL Here>"
dt_api_token = "<API Token Here>"
secret_key = "<Azure SecretKey>"

# Setting headers 
headers = {
    "Authorization": f"Api-Token {dt_api_token}",
    "Content-Type": "application/json",
}

# DELETE request to delete the Azure Monitor configuration relating to the DT configuration ID set above (dt_azure_credentials_id)
delete_request_url = f"{dt_env_url}/api/config/v1/azure/credentials/{dt_azure_credentials_id}"
delete_request_response = requests.delete(delete_request_url, headers=headers)

# Exception handling
if delete_request_response.status_code == 204:
    print("The Azure Monitor configuration specified has been successfully deleted.")
else:
    print(f"Failed to detelete the Azure Monitor configuration specified. Status code: {delete_request_response.status_code}")
