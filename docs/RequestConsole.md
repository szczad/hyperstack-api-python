# RequestConsole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.request_console import RequestConsole

# TODO update the JSON string below
json = "{}"
# create an instance of RequestConsole from a JSON string
request_console_instance = RequestConsole.from_json(json)
# print the JSON string representation of the object
print RequestConsole.to_json()

# convert the object into a dict
request_console_dict = request_console_instance.to_dict()
# create an instance of RequestConsole from a dict
request_console_form_dict = request_console.from_dict(request_console_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


