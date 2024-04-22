# FlavorAdminResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**flavor** | [**FlavorAdminResponseFlavors**](FlavorAdminResponseFlavors.md) |  | [optional] 

## Example

```python
from hyperstack.models.flavor_admin_response import FlavorAdminResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorAdminResponse from a JSON string
flavor_admin_response_instance = FlavorAdminResponse.from_json(json)
# print the JSON string representation of the object
print(FlavorAdminResponse.to_json())

# convert the object into a dict
flavor_admin_response_dict = flavor_admin_response_instance.to_dict()
# create an instance of FlavorAdminResponse from a dict
flavor_admin_response_form_dict = flavor_admin_response.from_dict(flavor_admin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


