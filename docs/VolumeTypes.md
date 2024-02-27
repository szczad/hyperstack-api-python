# VolumeTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**volume_types** | **List[str]** |  | [optional] 

## Example

```python
from hyperstack.models.volume_types import VolumeTypes

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeTypes from a JSON string
volume_types_instance = VolumeTypes.from_json(json)
# print the JSON string representation of the object
print VolumeTypes.to_json()

# convert the object into a dict
volume_types_dict = volume_types_instance.to_dict()
# create an instance of VolumeTypes from a dict
volume_types_form_dict = volume_types.from_dict(volume_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


