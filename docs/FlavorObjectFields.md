# FlavorObjectFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**disk** | **int** |  | [optional] 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.flavor_object_fields import FlavorObjectFields

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorObjectFields from a JSON string
flavor_object_fields_instance = FlavorObjectFields.from_json(json)
# print the JSON string representation of the object
print(FlavorObjectFields.to_json())

# convert the object into a dict
flavor_object_fields_dict = flavor_object_fields_instance.to_dict()
# create an instance of FlavorObjectFields from a dict
flavor_object_fields_form_dict = flavor_object_fields.from_dict(flavor_object_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


