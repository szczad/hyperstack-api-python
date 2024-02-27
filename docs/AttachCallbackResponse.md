# AttachCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.attach_callback_response import AttachCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachCallbackResponse from a JSON string
attach_callback_response_instance = AttachCallbackResponse.from_json(json)
# print the JSON string representation of the object
print AttachCallbackResponse.to_json()

# convert the object into a dict
attach_callback_response_dict = attach_callback_response_instance.to_dict()
# create an instance of AttachCallbackResponse from a dict
attach_callback_response_form_dict = attach_callback_response.from_dict(attach_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


