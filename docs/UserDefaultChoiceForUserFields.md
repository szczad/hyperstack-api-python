# UserDefaultChoiceForUserFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **int** |  | [optional] 
**environment_id** | **int** |  | [optional] 
**keypair_id** | **int** |  | [optional] 
**flavor_id** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.user_default_choice_for_user_fields import UserDefaultChoiceForUserFields

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefaultChoiceForUserFields from a JSON string
user_default_choice_for_user_fields_instance = UserDefaultChoiceForUserFields.from_json(json)
# print the JSON string representation of the object
print(UserDefaultChoiceForUserFields.to_json())

# convert the object into a dict
user_default_choice_for_user_fields_dict = user_default_choice_for_user_fields_instance.to_dict()
# create an instance of UserDefaultChoiceForUserFields from a dict
user_default_choice_for_user_fields_form_dict = user_default_choice_for_user_fields.from_dict(user_default_choice_for_user_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


