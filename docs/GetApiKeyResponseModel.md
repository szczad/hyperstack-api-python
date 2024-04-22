# GetApiKeyResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**api_key** | [**ApiKeyFields**](ApiKeyFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_api_key_response_model import GetApiKeyResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiKeyResponseModel from a JSON string
get_api_key_response_model_instance = GetApiKeyResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetApiKeyResponseModel.to_json())

# convert the object into a dict
get_api_key_response_model_dict = get_api_key_response_model_instance.to_dict()
# create an instance of GetApiKeyResponseModel from a dict
get_api_key_response_model_form_dict = get_api_key_response_model.from_dict(get_api_key_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


