# ContainerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**flavor** | [**FlavorResource**](FlavorResource.md) |  | [optional] 
**status** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.container_resource import ContainerResource

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerResource from a JSON string
container_resource_instance = ContainerResource.from_json(json)
# print the JSON string representation of the object
print ContainerResource.to_json()

# convert the object into a dict
container_resource_dict = container_resource_instance.to_dict()
# create an instance of ContainerResource from a dict
container_resource_form_dict = container_resource.from_dict(container_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


