# UserFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.user_fields import UserFields

# TODO update the JSON string below
json = "{}"
# create an instance of UserFields from a JSON string
user_fields_instance = UserFields.from_json(json)
# print the JSON string representation of the object
print UserFields.to_json()

# convert the object into a dict
user_fields_dict = user_fields_instance.to_dict()
# create an instance of UserFields from a dict
user_fields_form_dict = user_fields.from_dict(user_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


