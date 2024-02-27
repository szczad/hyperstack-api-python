# PermissionsforUserPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**permissions** | [**List[PermissionFieldsforUserPermission]**](PermissionFieldsforUserPermission.md) |  | [optional] 

## Example

```python
from hyperstack.models.permissionsfor_user_permission import PermissionsforUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsforUserPermission from a JSON string
permissionsfor_user_permission_instance = PermissionsforUserPermission.from_json(json)
# print the JSON string representation of the object
print PermissionsforUserPermission.to_json()

# convert the object into a dict
permissionsfor_user_permission_dict = permissionsfor_user_permission_instance.to_dict()
# create an instance of PermissionsforUserPermission from a dict
permissionsfor_user_permission_form_dict = permissionsfor_user_permission.from_dict(permissionsfor_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


