# CreateGPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**regions** | **List[str]** |  | [optional] 
**example_metadata** | **str** | A valid JSON string. | [optional] 

## Example

```python
from hyperstack.models.create_gpu import CreateGPU

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGPU from a JSON string
create_gpu_instance = CreateGPU.from_json(json)
# print the JSON string representation of the object
print(CreateGPU.to_json())

# convert the object into a dict
create_gpu_dict = create_gpu_instance.to_dict()
# create an instance of CreateGPU from a dict
create_gpu_form_dict = create_gpu.from_dict(create_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


