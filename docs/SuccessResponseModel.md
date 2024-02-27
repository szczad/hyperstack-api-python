# SuccessResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] [default to False]
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.success_response_model import SuccessResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseModel from a JSON string
success_response_model_instance = SuccessResponseModel.from_json(json)
# print the JSON string representation of the object
print SuccessResponseModel.to_json()

# convert the object into a dict
success_response_model_dict = success_response_model_instance.to_dict()
# create an instance of SuccessResponseModel from a dict
success_response_model_form_dict = success_response_model.from_dict(success_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


