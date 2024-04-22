# GetPoliciesResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**policies** | [**List[PolicyFields]**](PolicyFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_policies_response_model import GetPoliciesResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetPoliciesResponseModel from a JSON string
get_policies_response_model_instance = GetPoliciesResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetPoliciesResponseModel.to_json())

# convert the object into a dict
get_policies_response_model_dict = get_policies_response_model_instance.to_dict()
# create an instance of GetPoliciesResponseModel from a dict
get_policies_response_model_form_dict = get_policies_response_model.from_dict(get_policies_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


