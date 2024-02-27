# FlavorItemGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**flavors** | [**List[FlavorFields]**](FlavorFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.flavor_item_get_response import FlavorItemGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorItemGetResponse from a JSON string
flavor_item_get_response_instance = FlavorItemGetResponse.from_json(json)
# print the JSON string representation of the object
print FlavorItemGetResponse.to_json()

# convert the object into a dict
flavor_item_get_response_dict = flavor_item_get_response_instance.to_dict()
# create an instance of FlavorItemGetResponse from a dict
flavor_item_get_response_form_dict = flavor_item_get_response.from_dict(flavor_item_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


