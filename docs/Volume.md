# Volume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**volume** | [**VolumeFields**](VolumeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.volume import Volume

# TODO update the JSON string below
json = "{}"
# create an instance of Volume from a JSON string
volume_instance = Volume.from_json(json)
# print the JSON string representation of the object
print Volume.to_json()

# convert the object into a dict
volume_dict = volume_instance.to_dict()
# create an instance of Volume from a dict
volume_form_dict = volume.from_dict(volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


