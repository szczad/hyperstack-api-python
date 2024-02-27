# LogoGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.logo_get_response import LogoGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogoGetResponse from a JSON string
logo_get_response_instance = LogoGetResponse.from_json(json)
# print the JSON string representation of the object
print LogoGetResponse.to_json()

# convert the object into a dict
logo_get_response_dict = logo_get_response_instance.to_dict()
# create an instance of LogoGetResponse from a dict
logo_get_response_form_dict = logo_get_response.from_dict(logo_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


