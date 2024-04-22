# NodeStockPayloadModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks** | [**List[NodePayloadModel]**](NodePayloadModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.node_stock_payload_model import NodeStockPayloadModel

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStockPayloadModel from a JSON string
node_stock_payload_model_instance = NodeStockPayloadModel.from_json(json)
# print the JSON string representation of the object
print(NodeStockPayloadModel.to_json())

# convert the object into a dict
node_stock_payload_model_dict = node_stock_payload_model_instance.to_dict()
# create an instance of NodeStockPayloadModel from a dict
node_stock_payload_model_form_dict = node_stock_payload_model.from_dict(node_stock_payload_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


