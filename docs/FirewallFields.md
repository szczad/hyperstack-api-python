# FirewallFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**environment** | [**FirewallEnvironmentFields**](FirewallEnvironmentFields.md) |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.firewall_fields import FirewallFields

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallFields from a JSON string
firewall_fields_instance = FirewallFields.from_json(json)
# print the JSON string representation of the object
print(FirewallFields.to_json())

# convert the object into a dict
firewall_fields_dict = firewall_fields_instance.to_dict()
# create an instance of FirewallFields from a dict
firewall_fields_form_dict = firewall_fields.from_dict(firewall_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


