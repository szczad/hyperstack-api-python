# UpdateDiscountsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_resources** | [**List[ResourcePayload]**](ResourcePayload.md) |  | 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**discount_status** | **str** |  | 

## Example

```python
from hyperstack.models.update_discounts_payload import UpdateDiscountsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDiscountsPayload from a JSON string
update_discounts_payload_instance = UpdateDiscountsPayload.from_json(json)
# print the JSON string representation of the object
print(UpdateDiscountsPayload.to_json())

# convert the object into a dict
update_discounts_payload_dict = update_discounts_payload_instance.to_dict()
# create an instance of UpdateDiscountsPayload from a dict
update_discounts_payload_form_dict = update_discounts_payload.from_dict(update_discounts_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


