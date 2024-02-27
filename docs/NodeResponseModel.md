# NodeResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**nodes** | [**List[NodeModel]**](NodeModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.node_response_model import NodeResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of NodeResponseModel from a JSON string
node_response_model_instance = NodeResponseModel.from_json(json)
# print the JSON string representation of the object
print NodeResponseModel.to_json()

# convert the object into a dict
node_response_model_dict = node_response_model_instance.to_dict()
# create an instance of NodeResponseModel from a dict
node_response_model_form_dict = node_response_model.from_dict(node_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


