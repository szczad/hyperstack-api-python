# NewStockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**stock_type** | **str** |  | [optional] 
**models** | [**List[NewModelResponse]**](NewModelResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.new_stock_response import NewStockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewStockResponse from a JSON string
new_stock_response_instance = NewStockResponse.from_json(json)
# print the JSON string representation of the object
print NewStockResponse.to_json()

# convert the object into a dict
new_stock_response_dict = new_stock_response_instance.to_dict()
# create an instance of NewStockResponse from a dict
new_stock_response_form_dict = new_stock_response.from_dict(new_stock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


