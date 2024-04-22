# AttachFirewallsToVMPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewalls** | **List[int]** |  | 

## Example

```python
from hyperstack.models.attach_firewalls_to_vm_payload import AttachFirewallsToVMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachFirewallsToVMPayload from a JSON string
attach_firewalls_to_vm_payload_instance = AttachFirewallsToVMPayload.from_json(json)
# print the JSON string representation of the object
print(AttachFirewallsToVMPayload.to_json())

# convert the object into a dict
attach_firewalls_to_vm_payload_dict = attach_firewalls_to_vm_payload_instance.to_dict()
# create an instance of AttachFirewallsToVMPayload from a dict
attach_firewalls_to_vm_payload_form_dict = attach_firewalls_to_vm_payload.from_dict(attach_firewalls_to_vm_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


