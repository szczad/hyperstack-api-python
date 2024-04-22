# GetRbacRolesResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**roles** | [**List[RbacRoleFields]**](RbacRoleFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_rbac_roles_response_model import GetRbacRolesResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetRbacRolesResponseModel from a JSON string
get_rbac_roles_response_model_instance = GetRbacRolesResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetRbacRolesResponseModel.to_json())

# convert the object into a dict
get_rbac_roles_response_model_dict = get_rbac_roles_response_model_instance.to_dict()
# create an instance of GetRbacRolesResponseModel from a dict
get_rbac_roles_response_model_form_dict = get_rbac_roles_response_model.from_dict(get_rbac_roles_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


