# FlavorVMsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**flavor_vms** | [**List[FlavorVMFields]**](FlavorVMFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.flavor_vms_response import FlavorVMsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorVMsResponse from a JSON string
flavor_vms_response_instance = FlavorVMsResponse.from_json(json)
# print the JSON string representation of the object
print(FlavorVMsResponse.to_json())

# convert the object into a dict
flavor_vms_response_dict = flavor_vms_response_instance.to_dict()
# create an instance of FlavorVMsResponse from a dict
flavor_vms_response_form_dict = flavor_vms_response.from_dict(flavor_vms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


