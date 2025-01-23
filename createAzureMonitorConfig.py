import requests

# Setting variables
dt_env_url = "<Env URL Here>"
dt_api_token = "<API Token Here>"
dt_azure_credentials_id = "<Azure Cred Entity>"
secret_key = "<Azure SecretKey>"
dt_configuration_name = "<Azure Configname>"
azure_client_id = "<Azure ClientID>"
azure_tenant_id = "<Azure TenantID>"
azure_secret_key = "<Azure SecretKey>"

# Setting headers 
headers = {
    "Authorization": f"Api-Token {dt_api_token}",
    "Content-Type": "application/json",
}

# Setting POST payload
config_json = {
        "active": 'true',
        "label": dt_configuration_name,
        "appId": azure_client_id,
        "directoryId": azure_tenant_id,
        "key": azure_secret_key,
        "autoTagging": 'true',
        "monitorOnlyTaggedEntities": 'false'
    }

# POST request to create the Azure Monitor configuration
post_url = f"{dt_env_url}/api/config/v1/azure/credentials/"
post_response = requests.post(post_url, headers=headers, json=config_json)

# Exception handling
if post_response.status_code == 201:
    print("Azure Monitor configuration created successfully!")
    print(post_response.json())
else:
    print(f"Failed to create Azure Monitor configuration. Status code: {post_response.status_code}")
    print(post_response.json())