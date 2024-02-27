# PaymentDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**data** | [**PaymentDetailsFields**](PaymentDetailsFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.payment_details_response import PaymentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailsResponse from a JSON string
payment_details_response_instance = PaymentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print PaymentDetailsResponse.to_json()

# convert the object into a dict
payment_details_response_dict = payment_details_response_instance.to_dict()
# create an instance of PaymentDetailsResponse from a dict
payment_details_response_form_dict = payment_details_response.from_dict(payment_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


