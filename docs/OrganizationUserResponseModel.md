# OrganizationUserResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sub** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**rbac_roles** | [**List[RbacRoleField]**](RbacRoleField.md) |  | [optional] 
**joined_at** | **datetime** |  | [optional] 
**last_login** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.organization_user_response_model import OrganizationUserResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUserResponseModel from a JSON string
organization_user_response_model_instance = OrganizationUserResponseModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationUserResponseModel.to_json())

# convert the object into a dict
organization_user_response_model_dict = organization_user_response_model_instance.to_dict()
# create an instance of OrganizationUserResponseModel from a dict
organization_user_response_model_form_dict = organization_user_response_model.from_dict(organization_user_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


