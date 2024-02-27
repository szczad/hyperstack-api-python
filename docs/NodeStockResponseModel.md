# NodeStockResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks** | [**List[NodeResponseModel]**](NodeResponseModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.node_stock_response_model import NodeStockResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStockResponseModel from a JSON string
node_stock_response_model_instance = NodeStockResponseModel.from_json(json)
# print the JSON string representation of the object
print NodeStockResponseModel.to_json()

# convert the object into a dict
node_stock_response_model_dict = node_stock_response_model_instance.to_dict()
# create an instance of NodeStockResponseModel from a dict
node_stock_response_model_form_dict = node_stock_response_model.from_dict(node_stock_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


