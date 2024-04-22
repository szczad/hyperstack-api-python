# GetContractsListResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**contracts** | [**List[AdminContractFields]**](AdminContractFields.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.get_contracts_list_response_model import GetContractsListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractsListResponseModel from a JSON string
get_contracts_list_response_model_instance = GetContractsListResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetContractsListResponseModel.to_json())

# convert the object into a dict
get_contracts_list_response_model_dict = get_contracts_list_response_model_instance.to_dict()
# create an instance of GetContractsListResponseModel from a dict
get_contracts_list_response_model_form_dict = get_contracts_list_response_model.from_dict(get_contracts_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


