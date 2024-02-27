# InstanceFlavorFields


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
from hyperstack.models.instance_flavor_fields import InstanceFlavorFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceFlavorFields from a JSON string
instance_flavor_fields_instance = InstanceFlavorFields.from_json(json)
# print the JSON string representation of the object
print InstanceFlavorFields.to_json()

# convert the object into a dict
instance_flavor_fields_dict = instance_flavor_fields_instance.to_dict()
# create an instance of InstanceFlavorFields from a dict
instance_flavor_fields_form_dict = instance_flavor_fields.from_dict(instance_flavor_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


