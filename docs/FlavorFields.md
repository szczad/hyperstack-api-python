# FlavorFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**cpu** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**disk** | **int** |  | [optional] 
**ephemeral** | **int** |  | [optional] 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**stock_available** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.flavor_fields import FlavorFields

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorFields from a JSON string
flavor_fields_instance = FlavorFields.from_json(json)
# print the JSON string representation of the object
print(FlavorFields.to_json())

# convert the object into a dict
flavor_fields_dict = flavor_fields_instance.to_dict()
# create an instance of FlavorFields from a dict
flavor_fields_form_dict = flavor_fields.from_dict(flavor_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


