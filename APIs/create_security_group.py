import json
import requests
#Setup the endpoint and create the bearer token
endpoint = 'https://login.microsoftonline.com/[TENANT_ID]/oauth2/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = 'grant_type=client_credentials&client_id=[CLIENT_ID]&client_secret=[CLIENT_SECRET]&resource=https%3A%2F%2Fgraph.microsoft.com%2F'
r = requests.post(endpoint, headers=headers, data=payload)
response = r.json()
bearertoken = response["access_token"]
#Setup the graph endpoint
endpoint = 'https://graph.microsoft.com/beta/groups'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % bearertoken}
params = {
    'api-version': '2013-11-08'
}
payload = {
      "description": "[Group description]",
      "displayName": "[Group Name]",
      "mailEnabled": "false",
      "mailNickname": "",
      "securityEnabled": "true",
      "members@odata.bind": [
        "https://graph.microsoft.com/beta/servicePrincipals/[OBJECT_ID]"
      ]
    }
r=requests.post(endpoint, headers=headers, data=json.dumps(payload))
print(r.status_code)
