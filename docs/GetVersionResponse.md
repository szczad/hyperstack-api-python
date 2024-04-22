# GetVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.get_version_response import GetVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVersionResponse from a JSON string
get_version_response_instance = GetVersionResponse.from_json(json)
# print the JSON string representation of the object
print(GetVersionResponse.to_json())

# convert the object into a dict
get_version_response_dict = get_version_response_instance.to_dict()
# create an instance of GetVersionResponse from a dict
get_version_response_form_dict = get_version_response.from_dict(get_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


