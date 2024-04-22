# AdminGetVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.admin_get_version_response import AdminGetVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGetVersionResponse from a JSON string
admin_get_version_response_instance = AdminGetVersionResponse.from_json(json)
# print the JSON string representation of the object
print(AdminGetVersionResponse.to_json())

# convert the object into a dict
admin_get_version_response_dict = admin_get_version_response_instance.to_dict()
# create an instance of AdminGetVersionResponse from a dict
admin_get_version_response_form_dict = admin_get_version_response.from_dict(admin_get_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


