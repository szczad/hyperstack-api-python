# AdminCreateContractResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**contract** | [**CreateContarctFields**](CreateContarctFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_create_contract_response_model import AdminCreateContractResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCreateContractResponseModel from a JSON string
admin_create_contract_response_model_instance = AdminCreateContractResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminCreateContractResponseModel.to_json())

# convert the object into a dict
admin_create_contract_response_model_dict = admin_create_contract_response_model_instance.to_dict()
# create an instance of AdminCreateContractResponseModel from a dict
admin_create_contract_response_model_form_dict = admin_create_contract_response_model.from_dict(admin_create_contract_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


