# Getcreditandthresholdinfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit** | **float** |  | [optional] 
**threshold** | **float** |  | [optional] 
**can_create_instance** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.getcreditandthresholdinfo import Getcreditandthresholdinfo

# TODO update the JSON string below
json = "{}"
# create an instance of Getcreditandthresholdinfo from a JSON string
getcreditandthresholdinfo_instance = Getcreditandthresholdinfo.from_json(json)
# print the JSON string representation of the object
print Getcreditandthresholdinfo.to_json()

# convert the object into a dict
getcreditandthresholdinfo_dict = getcreditandthresholdinfo_instance.to_dict()
# create an instance of Getcreditandthresholdinfo from a dict
getcreditandthresholdinfo_form_dict = getcreditandthresholdinfo.from_dict(getcreditandthresholdinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


