# CreateFirewallRulePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | 
**protocol** | **str** |  | 
**port_range_min** | **int** |  | [optional] 
**port_range_max** | **int** |  | [optional] 
**ethertype** | **str** |  | 
**remote_ip_prefix** | **str** |  | 

## Example

```python
from hyperstack.models.create_firewall_rule_payload import CreateFirewallRulePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRulePayload from a JSON string
create_firewall_rule_payload_instance = CreateFirewallRulePayload.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRulePayload.to_json())

# convert the object into a dict
create_firewall_rule_payload_dict = create_firewall_rule_payload_instance.to_dict()
# create an instance of CreateFirewallRulePayload from a dict
create_firewall_rule_payload_form_dict = create_firewall_rule_payload.from_dict(create_firewall_rule_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


