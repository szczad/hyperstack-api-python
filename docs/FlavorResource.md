# FlavorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**cpu** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**disk** | **int** |  | [optional] 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.flavor_resource import FlavorResource

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorResource from a JSON string
flavor_resource_instance = FlavorResource.from_json(json)
# print the JSON string representation of the object
print FlavorResource.to_json()

# convert the object into a dict
flavor_resource_dict = flavor_resource_instance.to_dict()
# create an instance of FlavorResource from a dict
flavor_resource_form_dict = flavor_resource.from_dict(flavor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


