# VolumeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**environment** | [**EnvironmentFieldsforVolume**](EnvironmentFieldsforVolume.md) |  | [optional] 
**description** | **str** |  | [optional] 
**volume_type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**bootable** | **bool** |  | [optional] 
**image_id** | **int** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.volume_fields import VolumeFields

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeFields from a JSON string
volume_fields_instance = VolumeFields.from_json(json)
# print the JSON string representation of the object
print(VolumeFields.to_json())

# convert the object into a dict
volume_fields_dict = volume_fields_instance.to_dict()
# create an instance of VolumeFields from a dict
volume_fields_form_dict = volume_fields.from_dict(volume_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


