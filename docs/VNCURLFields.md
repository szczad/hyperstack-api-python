# VNCURLFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**vnc_url** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.vncurl_fields import VNCURLFields

# TODO update the JSON string below
json = "{}"
# create an instance of VNCURLFields from a JSON string
vncurl_fields_instance = VNCURLFields.from_json(json)
# print the JSON string representation of the object
print(VNCURLFields.to_json())

# convert the object into a dict
vncurl_fields_dict = vncurl_fields_instance.to_dict()
# create an instance of VNCURLFields from a dict
vncurl_fields_form_dict = vncurl_fields.from_dict(vncurl_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


