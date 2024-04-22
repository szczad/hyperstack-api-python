# AdminVolumeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**bootable** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_volume_resource import AdminVolumeResource

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVolumeResource from a JSON string
admin_volume_resource_instance = AdminVolumeResource.from_json(json)
# print the JSON string representation of the object
print(AdminVolumeResource.to_json())

# convert the object into a dict
admin_volume_resource_dict = admin_volume_resource_instance.to_dict()
# create an instance of AdminVolumeResource from a dict
admin_volume_resource_form_dict = admin_volume_resource.from_dict(admin_volume_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


