# FirewallDetailFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**environment** | [**FirewallEnvironmentFields**](FirewallEnvironmentFields.md) |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**rules** | [**List[SecurityGroupRuleFields]**](SecurityGroupRuleFields.md) |  | [optional] 
**attachments** | [**List[FirewallAttachmentModel]**](FirewallAttachmentModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.firewall_detail_fields import FirewallDetailFields

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallDetailFields from a JSON string
firewall_detail_fields_instance = FirewallDetailFields.from_json(json)
# print the JSON string representation of the object
print(FirewallDetailFields.to_json())

# convert the object into a dict
firewall_detail_fields_dict = firewall_detail_fields_instance.to_dict()
# create an instance of FirewallDetailFields from a dict
firewall_detail_fields_form_dict = firewall_detail_fields.from_dict(firewall_detail_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


