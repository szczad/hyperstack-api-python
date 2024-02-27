# InternalVolumesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**volumes** | [**List[InternalVolumeFields]**](InternalVolumeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.internal_volumes_response import InternalVolumesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalVolumesResponse from a JSON string
internal_volumes_response_instance = InternalVolumesResponse.from_json(json)
# print the JSON string representation of the object
print InternalVolumesResponse.to_json()

# convert the object into a dict
internal_volumes_response_dict = internal_volumes_response_instance.to_dict()
# create an instance of InternalVolumesResponse from a dict
internal_volumes_response_form_dict = internal_volumes_response.from_dict(internal_volumes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


