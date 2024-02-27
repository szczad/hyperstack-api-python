# SingleVisibilityUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user_id** | **int** |  | 
**stock_visible** | **bool** |  | 

## Example

```python
from hyperstack.models.single_visibility_user_response import SingleVisibilityUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleVisibilityUserResponse from a JSON string
single_visibility_user_response_instance = SingleVisibilityUserResponse.from_json(json)
# print the JSON string representation of the object
print SingleVisibilityUserResponse.to_json()

# convert the object into a dict
single_visibility_user_response_dict = single_visibility_user_response_instance.to_dict()
# create an instance of SingleVisibilityUserResponse from a dict
single_visibility_user_response_form_dict = single_visibility_user_response.from_dict(single_visibility_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


