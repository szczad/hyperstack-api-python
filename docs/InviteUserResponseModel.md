# InviteUserResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**invite** | [**InviteFields**](InviteFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.invite_user_response_model import InviteUserResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserResponseModel from a JSON string
invite_user_response_model_instance = InviteUserResponseModel.from_json(json)
# print the JSON string representation of the object
print(InviteUserResponseModel.to_json())

# convert the object into a dict
invite_user_response_model_dict = invite_user_response_model_instance.to_dict()
# create an instance of InviteUserResponseModel from a dict
invite_user_response_model_form_dict = invite_user_response_model.from_dict(invite_user_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


