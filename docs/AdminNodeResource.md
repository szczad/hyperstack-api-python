# AdminNodeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**available** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**provision_date** | **datetime** |  | [optional] 
**organizations** | **List[int]** |  | [optional] 

## Example

```python
from hyperstack.models.admin_node_resource import AdminNodeResource

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNodeResource from a JSON string
admin_node_resource_instance = AdminNodeResource.from_json(json)
# print the JSON string representation of the object
print(AdminNodeResource.to_json())

# convert the object into a dict
admin_node_resource_dict = admin_node_resource_instance.to_dict()
# create an instance of AdminNodeResource from a dict
admin_node_resource_form_dict = admin_node_resource.from_dict(admin_node_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


