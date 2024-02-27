# InstanceAdminFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**environment** | [**InstanceEnvironmentFields**](InstanceEnvironmentFields.md) |  | [optional] 
**image** | [**InstanceImageFields**](InstanceImageFields.md) |  | [optional] 
**flavor** | [**InstanceFlavorFields**](InstanceFlavorFields.md) |  | [optional] 
**keypair** | [**InstanceKeypairFields**](InstanceKeypairFields.md) |  | [optional] 
**volume_attachments** | [**List[VolumeAttachmentFields]**](VolumeAttachmentFields.md) |  | [optional] 
**security_rules** | [**List[SecurityRulesFieldsforInstance]**](SecurityRulesFieldsforInstance.md) |  | [optional] 
**power_state** | **str** |  | [optional] 
**vm_state** | **str** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**openstack_id** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.instance_admin_fields import InstanceAdminFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceAdminFields from a JSON string
instance_admin_fields_instance = InstanceAdminFields.from_json(json)
# print the JSON string representation of the object
print InstanceAdminFields.to_json()

# convert the object into a dict
instance_admin_fields_dict = instance_admin_fields_instance.to_dict()
# create an instance of InstanceAdminFields from a dict
instance_admin_fields_form_dict = instance_admin_fields.from_dict(instance_admin_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


