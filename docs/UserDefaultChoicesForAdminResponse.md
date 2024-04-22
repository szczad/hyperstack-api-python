# UserDefaultChoicesForAdminResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**user_default_choices** | [**List[UserDefaultChoiceForAdminFields]**](UserDefaultChoiceForAdminFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.user_default_choices_for_admin_response import UserDefaultChoicesForAdminResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefaultChoicesForAdminResponse from a JSON string
user_default_choices_for_admin_response_instance = UserDefaultChoicesForAdminResponse.from_json(json)
# print the JSON string representation of the object
print(UserDefaultChoicesForAdminResponse.to_json())

# convert the object into a dict
user_default_choices_for_admin_response_dict = user_default_choices_for_admin_response_instance.to_dict()
# create an instance of UserDefaultChoicesForAdminResponse from a dict
user_default_choices_for_admin_response_form_dict = user_default_choices_for_admin_response.from_dict(user_default_choices_for_admin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


