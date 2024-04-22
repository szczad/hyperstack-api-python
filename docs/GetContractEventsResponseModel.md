# GetContractEventsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**contract_events** | [**List[AdminContractEventFields]**](AdminContractEventFields.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.get_contract_events_response_model import GetContractEventsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractEventsResponseModel from a JSON string
get_contract_events_response_model_instance = GetContractEventsResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetContractEventsResponseModel.to_json())

# convert the object into a dict
get_contract_events_response_model_dict = get_contract_events_response_model_instance.to_dict()
# create an instance of GetContractEventsResponseModel from a dict
get_contract_events_response_model_form_dict = get_contract_events_response_model.from_dict(get_contract_events_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


