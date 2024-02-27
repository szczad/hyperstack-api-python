# Policies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**policies** | [**List[PolicyFields]**](PolicyFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.policies import Policies

# TODO update the JSON string below
json = "{}"
# create an instance of Policies from a JSON string
policies_instance = Policies.from_json(json)
# print the JSON string representation of the object
print Policies.to_json()

# convert the object into a dict
policies_dict = policies_instance.to_dict()
# create an instance of Policies from a dict
policies_form_dict = policies.from_dict(policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


