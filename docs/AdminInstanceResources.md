# AdminInstanceResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**flavor** | [**AdminFlavorResource**](AdminFlavorResource.md) |  | [optional] 
**image_id** | **int** |  | [optional] 
**volume_id** | **int** |  | [optional] 
**keypair_name** | **str** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**contract_id** | **int** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_instance_resources import AdminInstanceResources

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInstanceResources from a JSON string
admin_instance_resources_instance = AdminInstanceResources.from_json(json)
# print the JSON string representation of the object
print(AdminInstanceResources.to_json())

# convert the object into a dict
admin_instance_resources_dict = admin_instance_resources_instance.to_dict()
# create an instance of AdminInstanceResources from a dict
admin_instance_resources_form_dict = admin_instance_resources.from_dict(admin_instance_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


