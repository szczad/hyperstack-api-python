# AssignRBACRolePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** |  | 

## Example

```python
from hyperstack.models.assign_rbac_role_payload import AssignRBACRolePayload

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRBACRolePayload from a JSON string
assign_rbac_role_payload_instance = AssignRBACRolePayload.from_json(json)
# print the JSON string representation of the object
print AssignRBACRolePayload.to_json()

# convert the object into a dict
assign_rbac_role_payload_dict = assign_rbac_role_payload_instance.to_dict()
# create an instance of AssignRBACRolePayload from a dict
assign_rbac_role_payload_form_dict = assign_rbac_role_payload.from_dict(assign_rbac_role_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


