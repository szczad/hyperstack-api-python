# RolePermissionFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**resource** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.role_permission_fields import RolePermissionFields

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissionFields from a JSON string
role_permission_fields_instance = RolePermissionFields.from_json(json)
# print the JSON string representation of the object
print RolePermissionFields.to_json()

# convert the object into a dict
role_permission_fields_dict = role_permission_fields_instance.to_dict()
# create an instance of RolePermissionFields from a dict
role_permission_fields_form_dict = role_permission_fields.from_dict(role_permission_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


