# StockVisibilityUserPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[int]** |  | 

## Example

```python
from hyperstack.models.stock_visibility_user_payload import StockVisibilityUserPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StockVisibilityUserPayload from a JSON string
stock_visibility_user_payload_instance = StockVisibilityUserPayload.from_json(json)
# print the JSON string representation of the object
print(StockVisibilityUserPayload.to_json())

# convert the object into a dict
stock_visibility_user_payload_dict = stock_visibility_user_payload_instance.to_dict()
# create an instance of StockVisibilityUserPayload from a dict
stock_visibility_user_payload_form_dict = stock_visibility_user_payload.from_dict(stock_visibility_user_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


