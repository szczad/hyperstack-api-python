# PermissionFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**resource** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.permission_fields import PermissionFields

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionFields from a JSON string
permission_fields_instance = PermissionFields.from_json(json)
# print the JSON string representation of the object
print PermissionFields.to_json()

# convert the object into a dict
permission_fields_dict = permission_fields_instance.to_dict()
# create an instance of PermissionFields from a dict
permission_fields_form_dict = permission_fields.from_dict(permission_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


