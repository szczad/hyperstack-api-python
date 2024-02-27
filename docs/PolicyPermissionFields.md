# PolicyPermissionFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**resource** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.policy_permission_fields import PolicyPermissionFields

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyPermissionFields from a JSON string
policy_permission_fields_instance = PolicyPermissionFields.from_json(json)
# print the JSON string representation of the object
print PolicyPermissionFields.to_json()

# convert the object into a dict
policy_permission_fields_dict = policy_permission_fields_instance.to_dict()
# create an instance of PolicyPermissionFields from a dict
policy_permission_fields_form_dict = policy_permission_fields.from_dict(policy_permission_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


