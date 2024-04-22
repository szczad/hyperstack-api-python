# AdminUsersResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**users** | [**List[AdminUserFields]**](AdminUserFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_users_response_model import AdminUsersResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersResponseModel from a JSON string
admin_users_response_model_instance = AdminUsersResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminUsersResponseModel.to_json())

# convert the object into a dict
admin_users_response_model_dict = admin_users_response_model_instance.to_dict()
# create an instance of AdminUsersResponseModel from a dict
admin_users_response_model_form_dict = admin_users_response_model.from_dict(admin_users_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


