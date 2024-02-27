# GPUList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**gpu_list** | [**List[GPUFields]**](GPUFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.gpu_list import GPUList

# TODO update the JSON string below
json = "{}"
# create an instance of GPUList from a JSON string
gpu_list_instance = GPUList.from_json(json)
# print the JSON string representation of the object
print GPUList.to_json()

# convert the object into a dict
gpu_list_dict = gpu_list_instance.to_dict()
# create an instance of GPUList from a dict
gpu_list_form_dict = gpu_list.from_dict(gpu_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


