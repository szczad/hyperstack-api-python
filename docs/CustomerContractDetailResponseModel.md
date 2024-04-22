# CustomerContractDetailResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**contracts** | [**CustomerContractFields**](CustomerContractFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.customer_contract_detail_response_model import CustomerContractDetailResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerContractDetailResponseModel from a JSON string
customer_contract_detail_response_model_instance = CustomerContractDetailResponseModel.from_json(json)
# print the JSON string representation of the object
print(CustomerContractDetailResponseModel.to_json())

# convert the object into a dict
customer_contract_detail_response_model_dict = customer_contract_detail_response_model_instance.to_dict()
# create an instance of CustomerContractDetailResponseModel from a dict
customer_contract_detail_response_model_form_dict = customer_contract_detail_response_model.from_dict(customer_contract_detail_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


