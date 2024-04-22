# FutureNodeStockModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**expected_amount** | **int** |  | 

## Example

```python
from hyperstack.models.future_node_stock_model import FutureNodeStockModel

# TODO update the JSON string below
json = "{}"
# create an instance of FutureNodeStockModel from a JSON string
future_node_stock_model_instance = FutureNodeStockModel.from_json(json)
# print the JSON string representation of the object
print(FutureNodeStockModel.to_json())

# convert the object into a dict
future_node_stock_model_dict = future_node_stock_model_instance.to_dict()
# create an instance of FutureNodeStockModel from a dict
future_node_stock_model_form_dict = future_node_stock_model.from_dict(future_node_stock_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


