# ResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.response_model import ResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseModel from a JSON string
response_model_instance = ResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResponseModel.to_json())

# convert the object into a dict
response_model_dict = response_model_instance.to_dict()
# create an instance of ResponseModel from a dict
response_model_form_dict = response_model.from_dict(response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


