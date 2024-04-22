# CreateUpdatePolicyResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**policy** | [**PolicyFields**](PolicyFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.create_update_policy_response_model import CreateUpdatePolicyResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdatePolicyResponseModel from a JSON string
create_update_policy_response_model_instance = CreateUpdatePolicyResponseModel.from_json(json)
# print the JSON string representation of the object
print(CreateUpdatePolicyResponseModel.to_json())

# convert the object into a dict
create_update_policy_response_model_dict = create_update_policy_response_model_instance.to_dict()
# create an instance of CreateUpdatePolicyResponseModel from a dict
create_update_policy_response_model_form_dict = create_update_policy_response_model.from_dict(create_update_policy_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


