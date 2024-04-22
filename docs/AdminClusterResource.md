# AdminClusterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**master_count** | **int** |  | [optional] 
**node_count** | **int** |  | [optional] 
**node_flavor** | [**AdminFlavorResource**](AdminFlavorResource.md) |  | [optional] 
**enable_public_ip** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_cluster_resource import AdminClusterResource

# TODO update the JSON string below
json = "{}"
# create an instance of AdminClusterResource from a JSON string
admin_cluster_resource_instance = AdminClusterResource.from_json(json)
# print the JSON string representation of the object
print(AdminClusterResource.to_json())

# convert the object into a dict
admin_cluster_resource_dict = admin_cluster_resource_instance.to_dict()
# create an instance of AdminClusterResource from a dict
admin_cluster_resource_form_dict = admin_cluster_resource.from_dict(admin_cluster_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


