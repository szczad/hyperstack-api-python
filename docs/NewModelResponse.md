# NewModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**available** | **str** |  | [optional] 
**planned_7_days** | **str** |  | [optional] 
**planned_30_days** | **str** |  | [optional] 
**planned_100_days** | **str** |  | [optional] 
**configurations** | [**NewConfigurationsResponse**](NewConfigurationsResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.new_model_response import NewModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewModelResponse from a JSON string
new_model_response_instance = NewModelResponse.from_json(json)
# print the JSON string representation of the object
print(NewModelResponse.to_json())

# convert the object into a dict
new_model_response_dict = new_model_response_instance.to_dict()
# create an instance of NewModelResponse from a dict
new_model_response_form_dict = new_model_response.from_dict(new_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


