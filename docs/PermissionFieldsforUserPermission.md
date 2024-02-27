# PermissionFieldsforUserPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**resource** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.permission_fieldsfor_user_permission import PermissionFieldsforUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionFieldsforUserPermission from a JSON string
permission_fieldsfor_user_permission_instance = PermissionFieldsforUserPermission.from_json(json)
# print the JSON string representation of the object
print PermissionFieldsforUserPermission.to_json()

# convert the object into a dict
permission_fieldsfor_user_permission_dict = permission_fieldsfor_user_permission_instance.to_dict()
# create an instance of PermissionFieldsforUserPermission from a dict
permission_fieldsfor_user_permission_form_dict = permission_fieldsfor_user_permission.from_dict(permission_fieldsfor_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


