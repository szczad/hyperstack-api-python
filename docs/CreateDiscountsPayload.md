# CreateDiscountsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**List[CustomerPayload]**](CustomerPayload.md) |  | 
**discount_resources** | [**List[ResourcePayload]**](ResourcePayload.md) |  | 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**discount_status** | **str** |  | 

## Example

```python
from hyperstack.models.create_discounts_payload import CreateDiscountsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiscountsPayload from a JSON string
create_discounts_payload_instance = CreateDiscountsPayload.from_json(json)
# print the JSON string representation of the object
print(CreateDiscountsPayload.to_json())

# convert the object into a dict
create_discounts_payload_dict = create_discounts_payload_instance.to_dict()
# create an instance of CreateDiscountsPayload from a dict
create_discounts_payload_form_dict = create_discounts_payload.from_dict(create_discounts_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


