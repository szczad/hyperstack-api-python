# GetTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**token** | [**TokenFields**](TokenFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_token_response import GetTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokenResponse from a JSON string
get_token_response_instance = GetTokenResponse.from_json(json)
# print the JSON string representation of the object
print GetTokenResponse.to_json()

# convert the object into a dict
get_token_response_dict = get_token_response_instance.to_dict()
# create an instance of GetTokenResponse from a dict
get_token_response_form_dict = get_token_response.from_dict(get_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


