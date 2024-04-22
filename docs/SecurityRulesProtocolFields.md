# SecurityRulesProtocolFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**protocols** | **List[str]** |  | [optional] 

## Example

```python
from hyperstack.models.security_rules_protocol_fields import SecurityRulesProtocolFields

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRulesProtocolFields from a JSON string
security_rules_protocol_fields_instance = SecurityRulesProtocolFields.from_json(json)
# print the JSON string representation of the object
print(SecurityRulesProtocolFields.to_json())

# convert the object into a dict
security_rules_protocol_fields_dict = security_rules_protocol_fields_instance.to_dict()
# create an instance of SecurityRulesProtocolFields from a dict
security_rules_protocol_fields_form_dict = security_rules_protocol_fields.from_dict(security_rules_protocol_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


