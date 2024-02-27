# RBACRolePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**policies** | **List[int]** |  | [optional] 
**permissions** | **List[int]** |  | [optional] 

## Example

```python
from hyperstack.models.rbac_role_payload import RBACRolePayload

# TODO update the JSON string below
json = "{}"
# create an instance of RBACRolePayload from a JSON string
rbac_role_payload_instance = RBACRolePayload.from_json(json)
# print the JSON string representation of the object
print RBACRolePayload.to_json()

# convert the object into a dict
rbac_role_payload_dict = rbac_role_payload_instance.to_dict()
# create an instance of RBACRolePayload from a dict
rbac_role_payload_form_dict = rbac_role_payload.from_dict(rbac_role_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


