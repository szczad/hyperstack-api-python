# RBACRoleFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**policies** | [**List[RolePolicyFields]**](RolePolicyFields.md) |  | [optional] 
**permissions** | [**List[RolePermissionFields]**](RolePermissionFields.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.rbac_role_fields import RBACRoleFields

# TODO update the JSON string below
json = "{}"
# create an instance of RBACRoleFields from a JSON string
rbac_role_fields_instance = RBACRoleFields.from_json(json)
# print the JSON string representation of the object
print RBACRoleFields.to_json()

# convert the object into a dict
rbac_role_fields_dict = rbac_role_fields_instance.to_dict()
# create an instance of RBACRoleFields from a dict
rbac_role_fields_form_dict = rbac_role_fields.from_dict(rbac_role_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


