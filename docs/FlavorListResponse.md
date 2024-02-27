# FlavorListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**List[FlavorItemGetResponse]**](FlavorItemGetResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.flavor_list_response import FlavorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorListResponse from a JSON string
flavor_list_response_instance = FlavorListResponse.from_json(json)
# print the JSON string representation of the object
print FlavorListResponse.to_json()

# convert the object into a dict
flavor_list_response_dict = flavor_list_response_instance.to_dict()
# create an instance of FlavorListResponse from a dict
flavor_list_response_form_dict = flavor_list_response.from_dict(flavor_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


