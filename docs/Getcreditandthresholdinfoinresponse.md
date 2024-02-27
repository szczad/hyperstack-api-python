# Getcreditandthresholdinfoinresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**data** | [**Getcreditandthresholdinfo**](Getcreditandthresholdinfo.md) |  | [optional] 

## Example

```python
from hyperstack.models.getcreditandthresholdinfoinresponse import Getcreditandthresholdinfoinresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Getcreditandthresholdinfoinresponse from a JSON string
getcreditandthresholdinfoinresponse_instance = Getcreditandthresholdinfoinresponse.from_json(json)
# print the JSON string representation of the object
print Getcreditandthresholdinfoinresponse.to_json()

# convert the object into a dict
getcreditandthresholdinfoinresponse_dict = getcreditandthresholdinfoinresponse_instance.to_dict()
# create an instance of Getcreditandthresholdinfoinresponse from a dict
getcreditandthresholdinfoinresponse_form_dict = getcreditandthresholdinfoinresponse.from_dict(getcreditandthresholdinfoinresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


