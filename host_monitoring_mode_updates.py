import requests
import json

# Env URL
environment = "<Env URL Here>"

# Dynatrace API token with entities.read, settings.read, settings.write scope applied
api_token = "<API Token Here>"

# Entity selector filter encoded for API use
entity_selector = "entitySelector=type%28%22HOST%22%29"

# Header values for ALL API requests
headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'Authorization': 'Api-Token ' + api_token
}

# Gets hosts as per the entity selector above
get_hosts = requests.request("GET", environment + "/api/v2/entities?pageSize=1000&" + entity_selector, headers=headers)

# Validate GET hosts request was successful
print("Get host entity list response:")
print(get_hosts)

# Load into a JSON object
pretty_hosts = json.loads(get_hosts.content)

# Put hosts in an array for later use
host_ids = []
for host in pretty_hosts['entities']:
  host_ids.append(host['entityId'])

# Loops through all host IDs in the list and sends the POST request to update the monitoring mode setting based on the payload
for i in range(len(host_ids)):
    entityId = host_ids[i]
    payload = json.dumps([
  {
    "schemaId": "builtin:host.monitoring.mode",
    "scope": entityId,
    "value": {
      "monitoringMode":"FULL_STACK"
    }
  }
])
    host_monitoring_mode_setting_update = requests.request("POST", environment + "/api/v2/settings/objects?validateOnly=false", headers=headers, data=payload)
    print("Host monitoring mode settings POST request for " + entityId)
    print(host_monitoring_mode_setting_update)