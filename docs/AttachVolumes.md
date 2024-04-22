# AttachVolumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**volume_attachments** | [**List[AttachVolumeFields]**](AttachVolumeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.attach_volumes import AttachVolumes

# TODO update the JSON string below
json = "{}"
# create an instance of AttachVolumes from a JSON string
attach_volumes_instance = AttachVolumes.from_json(json)
# print the JSON string representation of the object
print(AttachVolumes.to_json())

# convert the object into a dict
attach_volumes_dict = attach_volumes_instance.to_dict()
# create an instance of AttachVolumes from a dict
attach_volumes_form_dict = attach_volumes.from_dict(attach_volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


