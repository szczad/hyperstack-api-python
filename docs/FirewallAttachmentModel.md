# FirewallAttachmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**vm** | [**FirewallAttachmentVMModel**](FirewallAttachmentVMModel.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.firewall_attachment_model import FirewallAttachmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallAttachmentModel from a JSON string
firewall_attachment_model_instance = FirewallAttachmentModel.from_json(json)
# print the JSON string representation of the object
print(FirewallAttachmentModel.to_json())

# convert the object into a dict
firewall_attachment_model_dict = firewall_attachment_model_instance.to_dict()
# create an instance of FirewallAttachmentModel from a dict
firewall_attachment_model_form_dict = firewall_attachment_model.from_dict(firewall_attachment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


