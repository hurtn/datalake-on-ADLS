import json
import requests
#Setup the endpoint
endpoint = 'https://login.microsoftonline.com/[TENANT_ID]/oauth2/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = 'grant_type=client_credentials&client_id=[CLIENT_ID]&client_secret=[CLIENT_SECRET]&resource=https%3A%2F%2Fstorage.azure.com%2F'
r = requests.post(endpoint, headers=headers, data=payload)
response = r.json()
#extract the bearer token from the response
bearertoken = response["access_token"]
# Set the storage header and parameter
headers = {'Authorization': 'Bearer %s' % bearertoken}
params = {
    'api-version': '2018-11-09'
}
# Create the container
r = requests.put("https://[STORAGE_ACCOUNT].dfs.core.windows.net/[CONTAINER_NAME]?resource=filesystem", headers=headers, params=params)
print(r.status_code)
