# PermissionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**permission** | **str** |  | 
**method** | **str** |  | 
**endpoint** | **str** |  | 

## Example

```python
from hyperstack.models.permission_payload import PermissionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionPayload from a JSON string
permission_payload_instance = PermissionPayload.from_json(json)
# print the JSON string representation of the object
print PermissionPayload.to_json()

# convert the object into a dict
permission_payload_dict = permission_payload_instance.to_dict()
# create an instance of PermissionPayload from a dict
permission_payload_form_dict = permission_payload.from_dict(permission_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


