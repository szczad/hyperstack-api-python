# ErrorResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] [default to False]
**message** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.error_response_model import ErrorResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseModel from a JSON string
error_response_model_instance = ErrorResponseModel.from_json(json)
# print the JSON string representation of the object
print ErrorResponseModel.to_json()

# convert the object into a dict
error_response_model_dict = error_response_model_instance.to_dict()
# create an instance of ErrorResponseModel from a dict
error_response_model_form_dict = error_response_model.from_dict(error_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


