# CustomerFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**plan_type** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.customer_fields import CustomerFields

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFields from a JSON string
customer_fields_instance = CustomerFields.from_json(json)
# print the JSON string representation of the object
print(CustomerFields.to_json())

# convert the object into a dict
customer_fields_dict = customer_fields_instance.to_dict()
# create an instance of CustomerFields from a dict
customer_fields_form_dict = customer_fields.from_dict(customer_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


