# FlavorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**flavor** | [**FlavorFields**](FlavorFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.flavor_response import FlavorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorResponse from a JSON string
flavor_response_instance = FlavorResponse.from_json(json)
# print the JSON string representation of the object
print FlavorResponse.to_json()

# convert the object into a dict
flavor_response_dict = flavor_response_instance.to_dict()
# create an instance of FlavorResponse from a dict
flavor_response_form_dict = flavor_response.from_dict(flavor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


