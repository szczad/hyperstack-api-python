# InternalVolumeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**volume_type** | **str** |  | [optional] 
**size** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.internal_volume_fields import InternalVolumeFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalVolumeFields from a JSON string
internal_volume_fields_instance = InternalVolumeFields.from_json(json)
# print the JSON string representation of the object
print InternalVolumeFields.to_json()

# convert the object into a dict
internal_volume_fields_dict = internal_volume_fields_instance.to_dict()
# create an instance of InternalVolumeFields from a dict
internal_volume_fields_form_dict = internal_volume_fields.from_dict(internal_volume_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


