# EnvrionmentResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**instances** | [**List[InstanceResources]**](InstanceResources.md) |  | [optional] 
**volumes** | [**List[VolumeResource]**](VolumeResource.md) |  | [optional] 
**containers** | [**List[ContainerResource]**](ContainerResource.md) |  | [optional] 
**clusters** | [**List[ClusterResource]**](ClusterResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.envrionment_resources import EnvrionmentResources

# TODO update the JSON string below
json = "{}"
# create an instance of EnvrionmentResources from a JSON string
envrionment_resources_instance = EnvrionmentResources.from_json(json)
# print the JSON string representation of the object
print EnvrionmentResources.to_json()

# convert the object into a dict
envrionment_resources_dict = envrionment_resources_instance.to_dict()
# create an instance of EnvrionmentResources from a dict
envrionment_resources_form_dict = envrionment_resources.from_dict(envrionment_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


