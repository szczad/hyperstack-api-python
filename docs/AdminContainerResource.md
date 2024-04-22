# AdminContainerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**flavor** | [**AdminFlavorResource**](AdminFlavorResource.md) |  | [optional] 
**status** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_container_resource import AdminContainerResource

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContainerResource from a JSON string
admin_container_resource_instance = AdminContainerResource.from_json(json)
# print the JSON string representation of the object
print(AdminContainerResource.to_json())

# convert the object into a dict
admin_container_resource_dict = admin_container_resource_instance.to_dict()
# create an instance of AdminContainerResource from a dict
admin_container_resource_form_dict = admin_container_resource.from_dict(admin_container_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


