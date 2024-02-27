# DetachVolumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**volume_attachments** | [**List[AttachVolumeFields]**](AttachVolumeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.detach_volumes import DetachVolumes

# TODO update the JSON string below
json = "{}"
# create an instance of DetachVolumes from a JSON string
detach_volumes_instance = DetachVolumes.from_json(json)
# print the JSON string representation of the object
print DetachVolumes.to_json()

# convert the object into a dict
detach_volumes_dict = detach_volumes_instance.to_dict()
# create an instance of DetachVolumes from a dict
detach_volumes_form_dict = detach_volumes.from_dict(detach_volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


