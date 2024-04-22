# AdminFlavorDetailFields


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
**nodes** | [**List[AdminFlavorDetailNodeFields]**](AdminFlavorDetailNodeFields.md) |  | [optional] 
**vms** | **List[int]** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**is_custom** | **bool** |  | [optional] 
**org_ids** | **List[int]** |  | [optional] 
**ephemeral** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_flavor_detail_fields import AdminFlavorDetailFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFlavorDetailFields from a JSON string
admin_flavor_detail_fields_instance = AdminFlavorDetailFields.from_json(json)
# print the JSON string representation of the object
print(AdminFlavorDetailFields.to_json())

# convert the object into a dict
admin_flavor_detail_fields_dict = admin_flavor_detail_fields_instance.to_dict()
# create an instance of AdminFlavorDetailFields from a dict
admin_flavor_detail_fields_form_dict = admin_flavor_detail_fields.from_dict(admin_flavor_detail_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


