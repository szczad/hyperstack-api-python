# NewStockUpdateResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.new_stock_update_response_model import NewStockUpdateResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of NewStockUpdateResponseModel from a JSON string
new_stock_update_response_model_instance = NewStockUpdateResponseModel.from_json(json)
# print the JSON string representation of the object
print(NewStockUpdateResponseModel.to_json())

# convert the object into a dict
new_stock_update_response_model_dict = new_stock_update_response_model_instance.to_dict()
# create an instance of NewStockUpdateResponseModel from a dict
new_stock_update_response_model_form_dict = new_stock_update_response_model.from_dict(new_stock_update_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


