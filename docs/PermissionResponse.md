# PermissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**permission** | [**PermissionFields**](PermissionFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.permission_response import PermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionResponse from a JSON string
permission_response_instance = PermissionResponse.from_json(json)
# print the JSON string representation of the object
print PermissionResponse.to_json()

# convert the object into a dict
permission_response_dict = permission_response_instance.to_dict()
# create an instance of PermissionResponse from a dict
permission_response_form_dict = permission_response.from_dict(permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


