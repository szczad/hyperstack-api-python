# InstancesAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instances** | [**List[InstanceAdminFields]**](InstanceAdminFields.md) |  | [optional] 
**instance_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.instances_admin import InstancesAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesAdmin from a JSON string
instances_admin_instance = InstancesAdmin.from_json(json)
# print the JSON string representation of the object
print(InstancesAdmin.to_json())

# convert the object into a dict
instances_admin_dict = instances_admin_instance.to_dict()
# create an instance of InstancesAdmin from a dict
instances_admin_form_dict = instances_admin.from_dict(instances_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


