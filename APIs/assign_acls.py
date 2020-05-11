import requests, uuid

#Authorisation request
endpoint = 'https://login.microsoftonline.com/[TENANT_ID]/oauth2/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = 'grant_type=client_credentials&client_id=[CLIENT_ID]&client_secret=[CLIENT_SECRET]&resource=https%3A%2F%2Fstorage.azure.com%2F'
r = requests.post(endpoint, headers=headers, data=payload)
response = r.json()
#extract the bearer token from the response
bearertoken = response["access_token"]
puuid = str(uuid.uuid4())
print('Log analytics UUID'+ puuid)
headers = {'x-ms-version': '2018-11-09','Authorization': 'Bearer %s' % bearertoken, 'x-ms-acl': 'user:c05d78ab-d947-4a76-a89b-c4aa68848a67:rwx,default:user:[SECURITY_PRINCIPAL]:rwx','x-ms-client-request-id': '%s' % puuid}
r = requests.patch("https://[STORAGE_ACCOUNT].dfs.core.windows.net/[CONTAINER]/[PATH]?action=setAccessControl", headers=headers)
print(r.status_code)
