# GetUserPermissionsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**permissions** | [**List[UserPermissionFields]**](UserPermissionFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_user_permissions_response_model import GetUserPermissionsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPermissionsResponseModel from a JSON string
get_user_permissions_response_model_instance = GetUserPermissionsResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetUserPermissionsResponseModel.to_json())

# convert the object into a dict
get_user_permissions_response_model_dict = get_user_permissions_response_model_instance.to_dict()
# create an instance of GetUserPermissionsResponseModel from a dict
get_user_permissions_response_model_form_dict = get_user_permissions_response_model.from_dict(get_user_permissions_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


