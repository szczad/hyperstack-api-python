# FirewallEnvironmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.firewall_environment_fields import FirewallEnvironmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallEnvironmentFields from a JSON string
firewall_environment_fields_instance = FirewallEnvironmentFields.from_json(json)
# print the JSON string representation of the object
print(FirewallEnvironmentFields.to_json())

# convert the object into a dict
firewall_environment_fields_dict = firewall_environment_fields_instance.to_dict()
# create an instance of FirewallEnvironmentFields from a dict
firewall_environment_fields_form_dict = firewall_environment_fields.from_dict(firewall_environment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


