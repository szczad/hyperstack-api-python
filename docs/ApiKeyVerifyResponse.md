# ApiKeyVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**api_key** | [**ApiKeyVerifyFields**](ApiKeyVerifyFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.api_key_verify_response import ApiKeyVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyVerifyResponse from a JSON string
api_key_verify_response_instance = ApiKeyVerifyResponse.from_json(json)
# print the JSON string representation of the object
print ApiKeyVerifyResponse.to_json()

# convert the object into a dict
api_key_verify_response_dict = api_key_verify_response_instance.to_dict()
# create an instance of ApiKeyVerifyResponse from a dict
api_key_verify_response_form_dict = api_key_verify_response.from_dict(api_key_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


