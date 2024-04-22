# AdminEnvrionmentResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**instances** | [**List[AdminInstanceResources]**](AdminInstanceResources.md) |  | [optional] 
**volumes** | [**List[AdminVolumeResource]**](AdminVolumeResource.md) |  | [optional] 
**containers** | [**List[AdminContainerResource]**](AdminContainerResource.md) |  | [optional] 
**clusters** | [**List[AdminClusterResource]**](AdminClusterResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_envrionment_resources import AdminEnvrionmentResources

# TODO update the JSON string below
json = "{}"
# create an instance of AdminEnvrionmentResources from a JSON string
admin_envrionment_resources_instance = AdminEnvrionmentResources.from_json(json)
# print the JSON string representation of the object
print(AdminEnvrionmentResources.to_json())

# convert the object into a dict
admin_envrionment_resources_dict = admin_envrionment_resources_instance.to_dict()
# create an instance of AdminEnvrionmentResources from a dict
admin_envrionment_resources_form_dict = admin_envrionment_resources.from_dict(admin_envrionment_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


