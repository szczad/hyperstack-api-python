# Environments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**environments** | [**List[EnvironmentFields]**](EnvironmentFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.environments import Environments

# TODO update the JSON string below
json = "{}"
# create an instance of Environments from a JSON string
environments_instance = Environments.from_json(json)
# print the JSON string representation of the object
print(Environments.to_json())

# convert the object into a dict
environments_dict = environments_instance.to_dict()
# create an instance of Environments from a dict
environments_form_dict = environments.from_dict(environments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


