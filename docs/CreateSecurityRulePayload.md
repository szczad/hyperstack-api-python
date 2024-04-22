# CreateSecurityRulePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The direction of traffic that the firewall rule applies to. | 
**protocol** | **str** | The network protocol associated with the rule. Call the [&#x60;GET /core/sg-rules-protocols&#x60;](https://infrahub-api-doc.nexgencloud.com/#get-/core/sg-rules-protocols) endpoint to retrieve a list of permitted network protocols. | 
**ethertype** | **str** | The Ethernet type associated with the rule. | 
**remote_ip_prefix** | **str** | The IP address range that is allowed to access the specified port. Use \&quot;0.0.0.0/0\&quot; to allow any IP address. | 

## Example

```python
from hyperstack.models.create_security_rule_payload import CreateSecurityRulePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecurityRulePayload from a JSON string
create_security_rule_payload_instance = CreateSecurityRulePayload.from_json(json)
# print the JSON string representation of the object
print(CreateSecurityRulePayload.to_json())

# convert the object into a dict
create_security_rule_payload_dict = create_security_rule_payload_instance.to_dict()
# create an instance of CreateSecurityRulePayload from a dict
create_security_rule_payload_form_dict = create_security_rule_payload.from_dict(create_security_rule_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


