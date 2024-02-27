# VolumeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**bootable** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.volume_resource import VolumeResource

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeResource from a JSON string
volume_resource_instance = VolumeResource.from_json(json)
# print the JSON string representation of the object
print VolumeResource.to_json()

# convert the object into a dict
volume_resource_dict = volume_resource_instance.to_dict()
# create an instance of VolumeResource from a dict
volume_resource_form_dict = volume_resource.from_dict(volume_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


