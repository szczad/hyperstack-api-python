# AdminFlavorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**cpu** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**disk** | **int** |  | [optional] 
**gpu** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**stock_available** | **bool** |  | [optional] 
**nodes** | [**List[AdminNodeResource]**](AdminNodeResource.md) |  | [optional] 
**vms** | **List[int]** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**is_custom** | **bool** |  | [optional] 
**ephemeral** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_flavor_resource import AdminFlavorResource

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFlavorResource from a JSON string
admin_flavor_resource_instance = AdminFlavorResource.from_json(json)
# print the JSON string representation of the object
print(AdminFlavorResource.to_json())

# convert the object into a dict
admin_flavor_resource_dict = admin_flavor_resource_instance.to_dict()
# create an instance of AdminFlavorResource from a dict
admin_flavor_resource_form_dict = admin_flavor_resource.from_dict(admin_flavor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


