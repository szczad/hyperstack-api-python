# AdminFlavorDetailNodeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**available** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**provision_date** | **datetime** |  | [optional] 
**projects** | **List[str]** |  | [optional] 

## Example

```python
from hyperstack.models.admin_flavor_detail_node_fields import AdminFlavorDetailNodeFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFlavorDetailNodeFields from a JSON string
admin_flavor_detail_node_fields_instance = AdminFlavorDetailNodeFields.from_json(json)
# print the JSON string representation of the object
print(AdminFlavorDetailNodeFields.to_json())

# convert the object into a dict
admin_flavor_detail_node_fields_dict = admin_flavor_detail_node_fields_instance.to_dict()
# create an instance of AdminFlavorDetailNodeFields from a dict
admin_flavor_detail_node_fields_form_dict = admin_flavor_detail_node_fields.from_dict(admin_flavor_detail_node_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


