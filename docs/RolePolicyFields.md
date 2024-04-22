# RolePolicyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.role_policy_fields import RolePolicyFields

# TODO update the JSON string below
json = "{}"
# create an instance of RolePolicyFields from a JSON string
role_policy_fields_instance = RolePolicyFields.from_json(json)
# print the JSON string representation of the object
print(RolePolicyFields.to_json())

# convert the object into a dict
role_policy_fields_dict = role_policy_fields_instance.to_dict()
# create an instance of RolePolicyFields from a dict
role_policy_fields_form_dict = role_policy_fields.from_dict(role_policy_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


