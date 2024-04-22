# NodePayloadModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**nodes** | [**List[NodePowerUsageModel]**](NodePowerUsageModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.node_payload_model import NodePayloadModel

# TODO update the JSON string below
json = "{}"
# create an instance of NodePayloadModel from a JSON string
node_payload_model_instance = NodePayloadModel.from_json(json)
# print the JSON string representation of the object
print(NodePayloadModel.to_json())

# convert the object into a dict
node_payload_model_dict = node_payload_model_instance.to_dict()
# create an instance of NodePayloadModel from a dict
node_payload_model_form_dict = node_payload_model.from_dict(node_payload_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


