# PaymentInitiateFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.payment_initiate_fields import PaymentInitiateFields

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInitiateFields from a JSON string
payment_initiate_fields_instance = PaymentInitiateFields.from_json(json)
# print the JSON string representation of the object
print(PaymentInitiateFields.to_json())

# convert the object into a dict
payment_initiate_fields_dict = payment_initiate_fields_instance.to_dict()
# create an instance of PaymentInitiateFields from a dict
payment_initiate_fields_form_dict = payment_initiate_fields.from_dict(payment_initiate_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


