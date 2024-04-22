# NewConfigurationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1x** | **int** |  | [optional] 
**var_2x** | **int** |  | [optional] 
**var_4x** | **int** |  | [optional] 
**var_8x** | **int** |  | [optional] 
**var_10x** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.new_configurations_response import NewConfigurationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewConfigurationsResponse from a JSON string
new_configurations_response_instance = NewConfigurationsResponse.from_json(json)
# print the JSON string representation of the object
print(NewConfigurationsResponse.to_json())

# convert the object into a dict
new_configurations_response_dict = new_configurations_response_instance.to_dict()
# create an instance of NewConfigurationsResponse from a dict
new_configurations_response_form_dict = new_configurations_response.from_dict(new_configurations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


