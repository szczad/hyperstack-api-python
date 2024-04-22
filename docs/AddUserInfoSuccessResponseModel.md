# AddUserInfoSuccessResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**UsersInfoFields**](UsersInfoFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.add_user_info_success_response_model import AddUserInfoSuccessResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserInfoSuccessResponseModel from a JSON string
add_user_info_success_response_model_instance = AddUserInfoSuccessResponseModel.from_json(json)
# print the JSON string representation of the object
print(AddUserInfoSuccessResponseModel.to_json())

# convert the object into a dict
add_user_info_success_response_model_dict = add_user_info_success_response_model_instance.to_dict()
# create an instance of AddUserInfoSuccessResponseModel from a dict
add_user_info_success_response_model_form_dict = add_user_info_success_response_model.from_dict(add_user_info_success_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


