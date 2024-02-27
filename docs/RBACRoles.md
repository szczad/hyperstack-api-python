# RBACRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**roles** | [**List[RBACRoleFields]**](RBACRoleFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.rbac_roles import RBACRoles

# TODO update the JSON string below
json = "{}"
# create an instance of RBACRoles from a JSON string
rbac_roles_instance = RBACRoles.from_json(json)
# print the JSON string representation of the object
print RBACRoles.to_json()

# convert the object into a dict
rbac_roles_dict = rbac_roles_instance.to_dict()
# create an instance of RBACRoles from a dict
rbac_roles_form_dict = rbac_roles.from_dict(rbac_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


