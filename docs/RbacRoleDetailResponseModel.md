# RbacRoleDetailResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**role** | [**RbacRoleFields**](RbacRoleFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.rbac_role_detail_response_model import RbacRoleDetailResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of RbacRoleDetailResponseModel from a JSON string
rbac_role_detail_response_model_instance = RbacRoleDetailResponseModel.from_json(json)
# print the JSON string representation of the object
print(RbacRoleDetailResponseModel.to_json())

# convert the object into a dict
rbac_role_detail_response_model_dict = rbac_role_detail_response_model_instance.to_dict()
# create an instance of RbacRoleDetailResponseModel from a dict
rbac_role_detail_response_model_form_dict = rbac_role_detail_response_model.from_dict(rbac_role_detail_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


