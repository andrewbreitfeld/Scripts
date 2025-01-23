import requests
import json

# Env URL
environment = "<Env URL Here>"

# Dynatrace API token with entities.read, settings.read, settings.write scope applied
api_token = "<API Token Here>"

# Entity selector filter encoded for API use, filters on process groups with the defined tag key (replace ProcessGroupAvailabilityTesting)
entity_selector = "entitySelector=type%28%22PROCESS_GROUP%22%29%2Ctag%28%22ProcessGroupAvailabilityTesting%22%29"

# Example of entity selector filtering tag key and value, replace tagkey and tagvalue # entity_selector = "entitySelector=type%28%22PROCESS_GROUP%22%29%2Ctag%28%22tagkey%3Atagvalue%22%29"

# Header values for ALL API requests
headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'Authorization': 'Api-Token ' + api_token
}

# Get all process groups
all_pgs = requests.request("GET", environment + "/api/v2/entities?pageSize=1000&" + entity_selector, headers=headers)

# Validate GET PG request was successful
print(all_pgs)

# Load into a JSON object
pretty_pgs = json.loads(all_pgs.content)

# Put Process Group Ids in an array for later use
pg_ids = []
for pg in pretty_pgs['entities']:
  pg_ids.append(pg['entityId'])

# Prints all PG IDs that were pulled from the JSON
print(pg_ids)

# Loops through all PG IDs in the list and sends the POST request to update the process group availability monitoring setting based on the enabled parameter being True or False
for i in range(len(pg_ids)):
    entityId = pg_ids[i]
    payload = json.dumps([
  {
    "schemaId": "builtin:availability.process-group-alerting",
    "scope": entityId,
    "value": {
      "enabled": True,
      "alertingMode": "ON_PGI_UNAVAILABILITY"
    }
  }
])
    pg_availability_setting_update = requests.request("POST", environment + "/api/v2/settings/objects?validateOnly=false", headers=headers, data=payload)
    print("PG Availability monitoring settings POST request for " + entityId)
    print(pg_availability_setting_update)