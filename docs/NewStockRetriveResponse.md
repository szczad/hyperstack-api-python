# NewStockRetriveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks** | [**List[NewStockResponse]**](NewStockResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.new_stock_retrive_response import NewStockRetriveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewStockRetriveResponse from a JSON string
new_stock_retrive_response_instance = NewStockRetriveResponse.from_json(json)
# print the JSON string representation of the object
print NewStockRetriveResponse.to_json()

# convert the object into a dict
new_stock_retrive_response_dict = new_stock_retrive_response_instance.to_dict()
# create an instance of NewStockRetriveResponse from a dict
new_stock_retrive_response_form_dict = new_stock_retrive_response.from_dict(new_stock_retrive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


