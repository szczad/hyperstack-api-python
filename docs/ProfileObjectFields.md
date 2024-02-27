# ProfileObjectFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.profile_object_fields import ProfileObjectFields

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileObjectFields from a JSON string
profile_object_fields_instance = ProfileObjectFields.from_json(json)
# print the JSON string representation of the object
print ProfileObjectFields.to_json()

# convert the object into a dict
profile_object_fields_dict = profile_object_fields_instance.to_dict()
# create an instance of ProfileObjectFields from a dict
profile_object_fields_form_dict = profile_object_fields.from_dict(profile_object_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


