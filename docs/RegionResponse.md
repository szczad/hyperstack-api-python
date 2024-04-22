# RegionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**region** | [**RegionFields**](RegionFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.region_response import RegionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegionResponse from a JSON string
region_response_instance = RegionResponse.from_json(json)
# print the JSON string representation of the object
print(RegionResponse.to_json())

# convert the object into a dict
region_response_dict = region_response_instance.to_dict()
# create an instance of RegionResponse from a dict
region_response_form_dict = region_response.from_dict(region_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


