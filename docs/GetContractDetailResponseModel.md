# GetContractDetailResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**contract** | [**AdminGetContractDetailFields**](AdminGetContractDetailFields.md) |  | [optional] 
**discount_plans** | [**List[DiscountPlanFields]**](DiscountPlanFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_contract_detail_response_model import GetContractDetailResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractDetailResponseModel from a JSON string
get_contract_detail_response_model_instance = GetContractDetailResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetContractDetailResponseModel.to_json())

# convert the object into a dict
get_contract_detail_response_model_dict = get_contract_detail_response_model_instance.to_dict()
# create an instance of GetContractDetailResponseModel from a dict
get_contract_detail_response_model_form_dict = get_contract_detail_response_model.from_dict(get_contract_detail_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


