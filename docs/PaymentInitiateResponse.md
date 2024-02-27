# PaymentInitiateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**data** | [**PaymentInitiateFields**](PaymentInitiateFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.payment_initiate_response import PaymentInitiateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInitiateResponse from a JSON string
payment_initiate_response_instance = PaymentInitiateResponse.from_json(json)
# print the JSON string representation of the object
print PaymentInitiateResponse.to_json()

# convert the object into a dict
payment_initiate_response_dict = payment_initiate_response_instance.to_dict()
# create an instance of PaymentInitiateResponse from a dict
payment_initiate_response_form_dict = payment_initiate_response.from_dict(payment_initiate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


