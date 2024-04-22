# ContractInstanceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**flavor_name** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.contract_instance_fields import ContractInstanceFields

# TODO update the JSON string below
json = "{}"
# create an instance of ContractInstanceFields from a JSON string
contract_instance_fields_instance = ContractInstanceFields.from_json(json)
# print the JSON string representation of the object
print(ContractInstanceFields.to_json())

# convert the object into a dict
contract_instance_fields_dict = contract_instance_fields_instance.to_dict()
# create an instance of ContractInstanceFields from a dict
contract_instance_fields_form_dict = contract_instance_fields.from_dict(contract_instance_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


