# SecurityGroupRuleFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**direction** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**port_range_min** | **int** |  | [optional] 
**port_range_max** | **int** |  | [optional] 
**ethertype** | **str** |  | [optional] 
**remote_ip_prefix** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.security_group_rule_fields import SecurityGroupRuleFields

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupRuleFields from a JSON string
security_group_rule_fields_instance = SecurityGroupRuleFields.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupRuleFields.to_json())

# convert the object into a dict
security_group_rule_fields_dict = security_group_rule_fields_instance.to_dict()
# create an instance of SecurityGroupRuleFields from a dict
security_group_rule_fields_form_dict = security_group_rule_fields.from_dict(security_group_rule_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


