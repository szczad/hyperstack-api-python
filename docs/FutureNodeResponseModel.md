# FutureNodeResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**nodes** | [**List[FutureNodeModel]**](FutureNodeModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.future_node_response_model import FutureNodeResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of FutureNodeResponseModel from a JSON string
future_node_response_model_instance = FutureNodeResponseModel.from_json(json)
# print the JSON string representation of the object
print FutureNodeResponseModel.to_json()

# convert the object into a dict
future_node_response_model_dict = future_node_response_model_instance.to_dict()
# create an instance of FutureNodeResponseModel from a dict
future_node_response_model_form_dict = future_node_response_model.from_dict(future_node_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


