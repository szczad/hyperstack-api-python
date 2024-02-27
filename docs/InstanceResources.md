# InstanceResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**flavor** | [**FlavorResource**](FlavorResource.md) |  | [optional] 
**image_id** | **int** |  | [optional] 
**volume_id** | **int** |  | [optional] 
**keypair_name** | **str** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.instance_resources import InstanceResources

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceResources from a JSON string
instance_resources_instance = InstanceResources.from_json(json)
# print the JSON string representation of the object
print InstanceResources.to_json()

# convert the object into a dict
instance_resources_dict = instance_resources_instance.to_dict()
# create an instance of InstanceResources from a dict
instance_resources_form_dict = instance_resources.from_dict(instance_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


