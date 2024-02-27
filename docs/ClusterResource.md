# ClusterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**master_count** | **int** |  | [optional] 
**node_count** | **int** |  | [optional] 
**node_flavor** | [**FlavorResource**](FlavorResource.md) |  | [optional] 
**enable_public_ip** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_resource import ClusterResource

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResource from a JSON string
cluster_resource_instance = ClusterResource.from_json(json)
# print the JSON string representation of the object
print ClusterResource.to_json()

# convert the object into a dict
cluster_resource_dict = cluster_resource_instance.to_dict()
# create an instance of ClusterResource from a dict
cluster_resource_form_dict = cluster_resource.from_dict(cluster_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


