# InstanceAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instance** | [**InstanceAdminFields**](InstanceAdminFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.instance_admin import InstanceAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceAdmin from a JSON string
instance_admin_instance = InstanceAdmin.from_json(json)
# print the JSON string representation of the object
print(InstanceAdmin.to_json())

# convert the object into a dict
instance_admin_dict = instance_admin_instance.to_dict()
# create an instance of InstanceAdmin from a dict
instance_admin_form_dict = instance_admin.from_dict(instance_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


