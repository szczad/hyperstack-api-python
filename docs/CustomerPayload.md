# CustomerPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**plan_type** | **str** |  | 

## Example

```python
from hyperstack.models.customer_payload import CustomerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPayload from a JSON string
customer_payload_instance = CustomerPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerPayload.to_json())

# convert the object into a dict
customer_payload_dict = customer_payload_instance.to_dict()
# create an instance of CustomerPayload from a dict
customer_payload_form_dict = customer_payload.from_dict(customer_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


