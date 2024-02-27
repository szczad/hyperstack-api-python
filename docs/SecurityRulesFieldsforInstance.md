# SecurityRulesFieldsforInstance


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
from hyperstack.models.security_rules_fieldsfor_instance import SecurityRulesFieldsforInstance

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRulesFieldsforInstance from a JSON string
security_rules_fieldsfor_instance_instance = SecurityRulesFieldsforInstance.from_json(json)
# print the JSON string representation of the object
print SecurityRulesFieldsforInstance.to_json()

# convert the object into a dict
security_rules_fieldsfor_instance_dict = security_rules_fieldsfor_instance_instance.to_dict()
# create an instance of SecurityRulesFieldsforInstance from a dict
security_rules_fieldsfor_instance_form_dict = security_rules_fieldsfor_instance.from_dict(security_rules_fieldsfor_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


