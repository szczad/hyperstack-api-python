# ContractInstancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instances** | [**List[ContractInstanceFields]**](ContractInstanceFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.contract_instances_response import ContractInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractInstancesResponse from a JSON string
contract_instances_response_instance = ContractInstancesResponse.from_json(json)
# print the JSON string representation of the object
print(ContractInstancesResponse.to_json())

# convert the object into a dict
contract_instances_response_dict = contract_instances_response_instance.to_dict()
# create an instance of ContractInstancesResponse from a dict
contract_instances_response_form_dict = contract_instances_response.from_dict(contract_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


