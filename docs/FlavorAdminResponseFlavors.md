# FlavorAdminResponseFlavors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**region_id** | **int** |  | [optional] 
**region** | **str** |  | [optional] 
**cpu** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**disk** | **int** |  | [optional] 
**ephemeral** | **int** |  | [optional] 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**is_custom** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**organizations** | **List[int]** |  | 
**flavors** | **List[str]** |  | [optional] 
**projects** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.flavor_admin_response_flavors import FlavorAdminResponseFlavors

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorAdminResponseFlavors from a JSON string
flavor_admin_response_flavors_instance = FlavorAdminResponseFlavors.from_json(json)
# print the JSON string representation of the object
print(FlavorAdminResponseFlavors.to_json())

# convert the object into a dict
flavor_admin_response_flavors_dict = flavor_admin_response_flavors_instance.to_dict()
# create an instance of FlavorAdminResponseFlavors from a dict
flavor_admin_response_flavors_form_dict = flavor_admin_response_flavors.from_dict(flavor_admin_response_flavors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


