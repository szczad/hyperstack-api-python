# AttachVolumesPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_ids** | **List[int]** |  | [optional] 

## Example

```python
from hyperstack.models.attach_volumes_payload import AttachVolumesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachVolumesPayload from a JSON string
attach_volumes_payload_instance = AttachVolumesPayload.from_json(json)
# print the JSON string representation of the object
print(AttachVolumesPayload.to_json())

# convert the object into a dict
attach_volumes_payload_dict = attach_volumes_payload_instance.to_dict()
# create an instance of AttachVolumesPayload from a dict
attach_volumes_payload_form_dict = attach_volumes_payload.from_dict(attach_volumes_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


