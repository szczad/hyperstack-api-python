# FutureNodeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**openstack_name** | **str** |  | [optional] 
**nexgen_name** | **str** |  | [optional] 
**expected_provision_date** | **datetime** |  | 
**stocks** | [**List[FutureNodeStockModel]**](FutureNodeStockModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.future_node_model import FutureNodeModel

# TODO update the JSON string below
json = "{}"
# create an instance of FutureNodeModel from a JSON string
future_node_model_instance = FutureNodeModel.from_json(json)
# print the JSON string representation of the object
print FutureNodeModel.to_json()

# convert the object into a dict
future_node_model_dict = future_node_model_instance.to_dict()
# create an instance of FutureNodeModel from a dict
future_node_model_form_dict = future_node_model.from_dict(future_node_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


