# CommonResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.common_response_model import CommonResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseModel from a JSON string
common_response_model_instance = CommonResponseModel.from_json(json)
# print the JSON string representation of the object
print(CommonResponseModel.to_json())

# convert the object into a dict
common_response_model_dict = common_response_model_instance.to_dict()
# create an instance of CommonResponseModel from a dict
common_response_model_form_dict = common_response_model.from_dict(common_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


