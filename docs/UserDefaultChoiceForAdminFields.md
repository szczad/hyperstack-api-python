# UserDefaultChoiceForAdminFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**region_name** | **str** |  | [optional] 
**flavor_id** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.user_default_choice_for_admin_fields import UserDefaultChoiceForAdminFields

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefaultChoiceForAdminFields from a JSON string
user_default_choice_for_admin_fields_instance = UserDefaultChoiceForAdminFields.from_json(json)
# print the JSON string representation of the object
print(UserDefaultChoiceForAdminFields.to_json())

# convert the object into a dict
user_default_choice_for_admin_fields_dict = user_default_choice_for_admin_fields_instance.to_dict()
# create an instance of UserDefaultChoiceForAdminFields from a dict
user_default_choice_for_admin_fields_form_dict = user_default_choice_for_admin_fields.from_dict(user_default_choice_for_admin_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


