# AdminUserResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**user** | [**AdminUserFields**](AdminUserFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_user_response_model import AdminUserResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserResponseModel from a JSON string
admin_user_response_model_instance = AdminUserResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminUserResponseModel.to_json())

# convert the object into a dict
admin_user_response_model_dict = admin_user_response_model_instance.to_dict()
# create an instance of AdminUserResponseModel from a dict
admin_user_response_model_form_dict = admin_user_response_model.from_dict(admin_user_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


