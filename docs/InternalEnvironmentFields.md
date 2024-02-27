# InternalEnvironmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.internal_environment_fields import InternalEnvironmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalEnvironmentFields from a JSON string
internal_environment_fields_instance = InternalEnvironmentFields.from_json(json)
# print the JSON string representation of the object
print InternalEnvironmentFields.to_json()

# convert the object into a dict
internal_environment_fields_dict = internal_environment_fields_instance.to_dict()
# create an instance of InternalEnvironmentFields from a dict
internal_environment_fields_form_dict = internal_environment_fields.from_dict(internal_environment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


