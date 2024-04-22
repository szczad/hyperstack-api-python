# DetachVolumesPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_ids** | **List[int]** |  | [optional] 

## Example

```python
from hyperstack.models.detach_volumes_payload import DetachVolumesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DetachVolumesPayload from a JSON string
detach_volumes_payload_instance = DetachVolumesPayload.from_json(json)
# print the JSON string representation of the object
print(DetachVolumesPayload.to_json())

# convert the object into a dict
detach_volumes_payload_dict = detach_volumes_payload_instance.to_dict()
# create an instance of DetachVolumesPayload from a dict
detach_volumes_payload_form_dict = detach_volumes_payload.from_dict(detach_volumes_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


