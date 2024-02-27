# InternalVolumeAttachmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | [**InternalVolumeFields**](InternalVolumeFields.md) |  | [optional] 
**status** | **str** |  | [optional] 
**device** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.internal_volume_attachment_fields import InternalVolumeAttachmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalVolumeAttachmentFields from a JSON string
internal_volume_attachment_fields_instance = InternalVolumeAttachmentFields.from_json(json)
# print the JSON string representation of the object
print InternalVolumeAttachmentFields.to_json()

# convert the object into a dict
internal_volume_attachment_fields_dict = internal_volume_attachment_fields_instance.to_dict()
# create an instance of InternalVolumeAttachmentFields from a dict
internal_volume_attachment_fields_form_dict = internal_volume_attachment_fields.from_dict(internal_volume_attachment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


