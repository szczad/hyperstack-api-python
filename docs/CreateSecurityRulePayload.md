# CreateSecurityRulePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | 
**protocol** | **str** |  | 
**ethertype** | **str** |  | 
**remote_ip_prefix** | **str** |  | 

## Example

```python
from hyperstack.models.create_security_rule_payload import CreateSecurityRulePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecurityRulePayload from a JSON string
create_security_rule_payload_instance = CreateSecurityRulePayload.from_json(json)
# print the JSON string representation of the object
print CreateSecurityRulePayload.to_json()

# convert the object into a dict
create_security_rule_payload_dict = create_security_rule_payload_instance.to_dict()
# create an instance of CreateSecurityRulePayload from a dict
create_security_rule_payload_form_dict = create_security_rule_payload.from_dict(create_security_rule_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


