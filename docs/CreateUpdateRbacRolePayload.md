# CreateUpdateRbacRolePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**policies** | **List[int]** |  | [optional] 
**permissions** | **List[int]** |  | [optional] 

## Example

```python
from hyperstack.models.create_update_rbac_role_payload import CreateUpdateRbacRolePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateRbacRolePayload from a JSON string
create_update_rbac_role_payload_instance = CreateUpdateRbacRolePayload.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateRbacRolePayload.to_json())

# convert the object into a dict
create_update_rbac_role_payload_dict = create_update_rbac_role_payload_instance.to_dict()
# create an instance of CreateUpdateRbacRolePayload from a dict
create_update_rbac_role_payload_form_dict = create_update_rbac_role_payload.from_dict(create_update_rbac_role_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


