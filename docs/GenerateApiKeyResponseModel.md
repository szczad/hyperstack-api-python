# GenerateApiKeyResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.generate_api_key_response_model import GenerateApiKeyResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateApiKeyResponseModel from a JSON string
generate_api_key_response_model_instance = GenerateApiKeyResponseModel.from_json(json)
# print the JSON string representation of the object
print(GenerateApiKeyResponseModel.to_json())

# convert the object into a dict
generate_api_key_response_model_dict = generate_api_key_response_model_instance.to_dict()
# create an instance of GenerateApiKeyResponseModel from a dict
generate_api_key_response_model_form_dict = generate_api_key_response_model.from_dict(generate_api_key_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


