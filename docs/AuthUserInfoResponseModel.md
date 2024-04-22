# AuthUserInfoResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**user** | [**AuthUserFields**](AuthUserFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.auth_user_info_response_model import AuthUserInfoResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthUserInfoResponseModel from a JSON string
auth_user_info_response_model_instance = AuthUserInfoResponseModel.from_json(json)
# print the JSON string representation of the object
print(AuthUserInfoResponseModel.to_json())

# convert the object into a dict
auth_user_info_response_model_dict = auth_user_info_response_model_instance.to_dict()
# create an instance of AuthUserInfoResponseModel from a dict
auth_user_info_response_model_form_dict = auth_user_info_response_model.from_dict(auth_user_info_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


