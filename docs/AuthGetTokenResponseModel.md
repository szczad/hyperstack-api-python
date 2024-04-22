# AuthGetTokenResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**token** | [**TokenFields**](TokenFields.md) |  | [optional] 
**first_login** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.auth_get_token_response_model import AuthGetTokenResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetTokenResponseModel from a JSON string
auth_get_token_response_model_instance = AuthGetTokenResponseModel.from_json(json)
# print the JSON string representation of the object
print(AuthGetTokenResponseModel.to_json())

# convert the object into a dict
auth_get_token_response_model_dict = auth_get_token_response_model_instance.to_dict()
# create an instance of AuthGetTokenResponseModel from a dict
auth_get_token_response_model_form_dict = auth_get_token_response_model.from_dict(auth_get_token_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


