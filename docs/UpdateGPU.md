# UpdateGPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**example_metadata** | **str** | A valid JSON string. | [optional] 

## Example

```python
from hyperstack.models.update_gpu import UpdateGPU

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGPU from a JSON string
update_gpu_instance = UpdateGPU.from_json(json)
# print the JSON string representation of the object
print(UpdateGPU.to_json())

# convert the object into a dict
update_gpu_dict = update_gpu_instance.to_dict()
# create an instance of UpdateGPU from a dict
update_gpu_form_dict = update_gpu.from_dict(update_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


