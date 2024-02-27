# RBACRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**role** | [**RBACRoleFields**](RBACRoleFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.rbac_role import RBACRole

# TODO update the JSON string below
json = "{}"
# create an instance of RBACRole from a JSON string
rbac_role_instance = RBACRole.from_json(json)
# print the JSON string representation of the object
print RBACRole.to_json()

# convert the object into a dict
rbac_role_dict = rbac_role_instance.to_dict()
# create an instance of RBACRole from a dict
rbac_role_form_dict = rbac_role.from_dict(rbac_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


