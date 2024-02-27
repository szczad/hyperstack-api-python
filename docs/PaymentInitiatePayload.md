# PaymentInitiatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.payment_initiate_payload import PaymentInitiatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInitiatePayload from a JSON string
payment_initiate_payload_instance = PaymentInitiatePayload.from_json(json)
# print the JSON string representation of the object
print PaymentInitiatePayload.to_json()

# convert the object into a dict
payment_initiate_payload_dict = payment_initiate_payload_instance.to_dict()
# create an instance of PaymentInitiatePayload from a dict
payment_initiate_payload_form_dict = payment_initiate_payload.from_dict(payment_initiate_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


