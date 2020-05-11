headers = {'Content-type': 'application/json; charset=utf-8','Authorization': 'Bearer %s' % bearertoken}
params = {
    'api-version': '2019-04-01-preview'
}

assign_Storage_Blob_Data_Contributor = {
  "properties": {
    "roleDefinitionId": "/subscriptions/[SUBSCRIPTION_ID]/resourceGroups/[RESOURCE_GROUP]/providers/Microsoft.Storage/storageAccounts/[STORAGE_ACC]/blobServices/default/containers/[CONTAINER_NAME]/providers/Microsoft.Authorization/roleDefinitions/[BUILT_IN_ROLE_ID]",
     "principalId": "[Security_Group_Object_Id]"
  }
}
assign_Storage_Blob_Data_Reader = {
  "properties": {
    "roleDefinitionId": "/subscriptions/[SUBSCRIPTION_ID]/resourceGroups/[RESOURCE_GROUP]/providers/Microsoft.Storage/storageAccounts/[STORAGE_ACC]/blobServices/default/containers/[CONTAINER_NAME]/providers/Microsoft.Authorization/roleDefinitions/[BUILT_IN_ROLE_ID]",
    "principalId": "[Security_Group_Object_Id]"
  }
}
request_str = "https://management.azure.com/subscriptions/[SUBSCRIPTION_ID]/resourceGroups/[RESOURCE_GROUP]/providers/Microsoft.Storage/storageAccounts/[STORAGE_ACC]/blobServices/default/containers/[CONTAINER_NAME]/providers/Microsoft.Authorization/roleAssignments/"
# Make the contributor role assignment
contributor_assignment = requests.put(request_str +str(uuid.uuid4()), data=json.dumps(assign_Storage_Blob_Data_Contributor), headers=headers, params=params)
print(contributor_assignment.text)
# Make the reader role assignment
reader = requests.put(request_str +str(uuid.uuid4()), data=json.dumps(assign_Storage_Blob_Data_Reader), headers=headers, params=params)  
print(reader_assignment.text)
