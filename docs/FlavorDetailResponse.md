# FlavorDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**flavor** | [**AdminFlavorDetailFields**](AdminFlavorDetailFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.flavor_detail_response import FlavorDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorDetailResponse from a JSON string
flavor_detail_response_instance = FlavorDetailResponse.from_json(json)
# print the JSON string representation of the object
print(FlavorDetailResponse.to_json())

# convert the object into a dict
flavor_detail_response_dict = flavor_detail_response_instance.to_dict()
# create an instance of FlavorDetailResponse from a dict
flavor_detail_response_form_dict = flavor_detail_response.from_dict(flavor_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


